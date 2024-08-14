import os
import random

import torch
import torch.nn as nn
from torch import optim
from torch.utils.data import DataLoader, random_split

from early_stopping import EarlyStopping
from model import LanguageModel
from text_dataset import TextDataset
from tokenizer import Tokenizer


def train_model(model, train_loader, val_loader, optimizer, criterion, scheduler, epochs=100, max_grad_norm=1.0,
                patience=5, accumulation_steps=4):
    print("Training model...")
    device_name = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using {device_name}")
    device = torch.device(device_name)

    model.to(device)
    early_stopping = EarlyStopping(patience=patience)

    if device_name == "cuda":
        # Initialize GradScaler for mixed precision if using GPU
        scaler = torch.cuda.amp.GradScaler()
    else:
        scaler = None  # No scaler needed for CPU

    base_path = os.getenv("YS_LLM_BASE_PATH", "./")

    print("First epoch starting...")
    for epoch in range(epochs):
        model.train()
        epoch_loss = 0.0
        optimizer.zero_grad()  # Initialize the optimizer at the start of each epoch

        for i, (inputs, targets) in enumerate(train_loader):
            inputs, targets = inputs.to(device), targets.to(device)

            if device_name == "cuda":
                # Use autocast for mixed precision on GPU
                with torch.cuda.amp.autocast():
                    outputs = model(inputs)
                    batch_size, sequence_length, vocab_size = outputs.shape
                    outputs = outputs.view(batch_size * sequence_length, vocab_size)
                    targets = targets.view(batch_size * sequence_length)

                    loss = criterion(outputs, targets) / accumulation_steps
                # Scale the loss before backpropagation
                scaler.scale(loss).backward()
            else:
                # Full precision for CPU
                outputs = model(inputs)
                batch_size, sequence_length, vocab_size = outputs.shape
                outputs = outputs.view(batch_size * sequence_length, vocab_size)
                targets = targets.view(batch_size * sequence_length)

                loss = criterion(outputs, targets) / accumulation_steps
                loss.backward()

            # Accumulate gradients and update model after a certain number of steps
            if (i + 1) % accumulation_steps == 0:
                if device_name == "cuda":
                    scaler.unscale_(optimizer)
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_grad_norm)
                optimizer.step()
                if device_name == "cuda":
                    scaler.update()
                optimizer.zero_grad()  # Reset gradients for the next accumulation cycle

            epoch_loss += loss.item() * accumulation_steps  # Multiply to undo the earlier division

        # validation loss
        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for inputs, targets in val_loader:
                inputs, targets = inputs.to(device), targets.to(device)
                if device_name == "cuda":
                    with torch.cuda.amp.autocast():  # Use autocast for validation as well on GPU
                        outputs = model(inputs)
                        outputs = outputs.view(-1, outputs.size(-1))
                        targets = targets.view(-1)
                        loss = criterion(outputs, targets)
                else:
                    outputs = model(inputs)
                    outputs = outputs.view(-1, outputs.size(-1))
                    targets = targets.view(-1)
                    loss = criterion(outputs, targets)

                val_loss += loss.item()

        val_loss /= len(val_loader)
        print(f'Epoch {epoch + 1}, Loss: {epoch_loss / len(train_loader)}, Val Loss: {val_loss}')
        scheduler.step()

        early_stopping.check(val_loss)
        if early_stopping.stop_training:
            print(f"Early stopping triggered at epoch {epoch + 1}")
            break

        # Save model checkpoint every 5 epochs
        if epoch % 5 == 0:
            torch.save(model.state_dict(), f"{base_path}model_checkpoint.bin")
            print(f"Checkpoint saved at epoch {epoch + 1} to {base_path}model_checkpoint.bin")


def safe_tensor_conversion(data_list, dtype=torch.long):
    try:
        tensor = torch.tensor(data_list, dtype=dtype)
        return tensor
    except Exception as e:
        print(f"Error during tensor conversion: {e}")
        previous_len = None
        for i, data in enumerate(data_list):
            data_len = len(data)
            if previous_len is None:
                print(f"Data length at index {i}: {data_len}")
                previous_len = data_len
            if data_len != previous_len:
                print(f"Data length at index {i}: {data_len}")
                print(f"Data at index {i}: {data}")
            for token in data:
                if token is not None:
                    print(f"None found in data at index {i}: {data}")
        raise e


def prepare_training_data(texts, tokenizer, sequence_length=5):
    x_train_list, y_train_list = [], []
    for text in texts:
        tokens = tokenizer.tokenize(text)
        if len(tokens) < sequence_length + 1:
            continue  # Skip sequences that are too short
        for i in range(len(tokens) - sequence_length):
            intput_sequence = tokens[i:i + sequence_length]
            target_sequence = tokens[i + 1:i + sequence_length + 1]
            if len(intput_sequence) == sequence_length and len(target_sequence) == sequence_length:
                x_train_list.append(intput_sequence)  # Input sequence
                y_train_list.append(target_sequence)  # Target sequence
            else:
                print(
                    f"Skipping a sequence with incorrect length: x_seq={len(intput_sequence)}, y_seq={len(target_sequence)}")

    x_train = safe_tensor_conversion(x_train_list)
    y_train = safe_tensor_conversion(y_train_list)

    # print(f"x_train shape: {x_train.shape}")  # Expect (num_sequences, sequence_length)
    # print(f"y_train shape: {y_train.shape}")  # Expect (num_sequences, sequence_length)

    return x_train, y_train


def split_dataset(dataset, val_split=0.2):
    val_size = int(len(dataset) * val_split)
    train_size = len(dataset) - val_size
    train_dataset, val_dataset = random_split(dataset, [train_size, val_size])
    return train_dataset, val_dataset


def do_train(context_length=5, batch_size=64, max_epochs=100, patience=5, model_save_path="model.bin",
             tokenizer_save_path="tokenizer.pkl"):
    tokenizer, train_loader, val_loader, number_of_samples = build_tokenizer_and_load_tokens(context_length, batch_size,
                                                                                             tokenizer_save_path)

    model = LanguageModel(tokenizer.vocab_size())

    base_path = os.getenv("YS_LLM_BASE_PATH", "./")
    if os.path.exists(f"{base_path}model_checkpoint.bin"):
        model.load_state_dict(torch.load(f"{base_path}model_checkpoint.bin"))
        print(f"Resumed training from {base_path}model_checkpoint.bin")

    total_training_steps = (number_of_samples // batch_size) * max_epochs
    if number_of_samples % batch_size != 0:
        # Add one step for each epoch to cover the last incomplete batch
        total_training_steps += max_epochs

    optimizer = optim.AdamW(model.parameters(), lr=0.00001)
    # optimizer = optim.Adam(model.parameters(), lr=0.0005, weight_decay=1e-5)
    scheduler = optim.lr_scheduler.OneCycleLR(optimizer, max_lr=0.0005, total_steps=total_training_steps)
    criterion = nn.CrossEntropyLoss()

    train_model(model, train_loader, val_loader, optimizer, criterion, scheduler, epochs=max_epochs, patience=patience)

    print("Saving model...")
    torch.save(model.state_dict(), model_save_path)
    print(f"Model saved to {model_save_path}")


def build_tokenizer_and_load_tokens(context_length, batch_size, tokenizer_save_path):
    print("Loading and tokenizing training data...")
    training_file_names = get_training_file_names()
    # Split file names for training and validation
    random.shuffle(training_file_names)
    split_index = int(0.8 * len(training_file_names))
    train_files = training_file_names[:split_index]
    val_files = training_file_names[split_index:]

    # Initialize the tokenizer
    tokenizer = Tokenizer()

    # Update tokenizer vocab by iterating over each document
    for file_path in training_file_names:
        with open(file_path, 'r', encoding='utf-8') as file:
            document = file.read()
            tokenizer.learn_new_vocab(document)  # Add document content to vocab
            del document  # Free memory as soon as possible

    # Save the tokenizer with the built vocabulary
    tokenizer.save(tokenizer_save_path)

    # Create the TextDataset using file names, allowing on-the-fly loading
    train_dataset = TextDataset(train_files, tokenizer, context_length)
    val_dataset = TextDataset(val_files, tokenizer, context_length)

    # DataLoader for batching (shuffle is done within the TextDataset)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=False)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    number_of_samples = len(train_dataset)

    return tokenizer, train_loader, val_loader, number_of_samples


def get_training_file_names(directory="training_data"):
    base_path = os.getenv("YS_LLM_BASE_PATH", "./")
    file_names = []
    for filename in os.listdir(f"{base_path}{directory}"):
        if filename.endswith(".txt") or filename.endswith(".md"):
            filepath = os.path.join(f"{base_path}{directory}", filename)
            file_names.append(filepath)
    return file_names


def notebook_do_train():
    base_path = os.getenv("YS_LLM_BASE_PATH", "./")
    model_path = f"{base_path}model.bin"
    tokenizer_path = f"{base_path}tokenizer.pkl"
    do_train(context_length=256, batch_size=64,
             max_epochs=100, patience=2,
             model_save_path=model_path,
             tokenizer_save_path=tokenizer_path)


if __name__ == "__main__":
    notebook_do_train()
