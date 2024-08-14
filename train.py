import os
import torch
import numpy as np
import torch.nn as nn
from torch import optim
from torch.utils.data import TensorDataset, DataLoader, random_split

from model import LanguageModel
from tokenizer import SimpleTokenizer
import faulthandler


class EarlyStopping:
    def __init__(self, patience=5, min_delta=0.001):
        self.patience = patience
        self.min_delta = min_delta
        self.best_loss = np.inf
        self.wait = 0
        self.stop_training = False

    def check(self, current_loss):
        if (self.best_loss - current_loss) > self.min_delta:
            self.best_loss = current_loss
            self.wait = 0
        else:
            self.wait += 1
            if self.wait >= self.patience:
                self.stop_training = True


def train_model(model, train_loader, val_loader, optimizer, criterion, scheduler, epochs=100, max_grad_norm=1.0,
                patience=5):
    print("Training model...")
    device_name = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using {device_name}")
    device = torch.device(device_name)

    model.to(device)
    early_stopping = EarlyStopping(patience=patience)

    print("First epoch starting...")
    for epoch in range(epochs):
        model.train()
        epoch_loss = 0.0
        for inputs, targets in train_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            optimizer.zero_grad()

            outputs = model(inputs)
            batch_size, sequence_length, vocab_size = outputs.shape
            outputs = outputs.view(batch_size * sequence_length, vocab_size)
            targets = targets.view(batch_size * sequence_length)

            loss = criterion(outputs, targets)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_grad_norm)
            optimizer.step()
            epoch_loss += loss.item()

        # validation loss
        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for inputs, targets in val_loader:
                inputs, targets = inputs.to(device), targets.to(device)
                outputs = model(inputs)
                outputs = outputs.view(-1, outputs.size(-1))
                targets = targets.view(-1)
                loss = criterion(outputs, targets)
                val_loss += loss.item()

        val_loss /= len(val_loader)
        print(f'Epoch {epoch + 1}, Loss: {epoch_loss / len(train_loader)}, Val Loss: {val_loss}')
        scheduler.step(val_loss)

        early_stopping.check(val_loss)
        if early_stopping.stop_training:
            print(f"Early stopping triggered at epoch {epoch + 1}")
            break


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
    tokenizer, train_loader, val_loader = build_tokenizer_and_load_tokens(context_length, batch_size,
                                                                          tokenizer_save_path)

    model = LanguageModel(tokenizer.vocab_size())
    optimizer = optim.Adam(model.parameters(), lr=0.0005, weight_decay=1e-5)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=3)
    criterion = nn.CrossEntropyLoss()

    train_model(model, train_loader, val_loader, optimizer, criterion, scheduler, epochs=max_epochs, patience=patience)

    print("Saving model...")
    torch.save(model.state_dict(), model_save_path)
    print(f"Model saved to {model_save_path}")


def build_tokenizer_and_load_tokens(context_length, batch_size, tokenizer_save_path):
    # we do this in a separate function to allow python to free up memory when we no longer need the text.
    print("Loading training data...")
    all_text = read_all_documents()
    print("Training tokenizer...")
    tokenizer = SimpleTokenizer()
    tokenizer.append_documents_to_vocabulary(all_text)
    print("Saving tokenizer...")
    tokenizer.save(tokenizer_save_path)
    print("Tokenizer vocabulary size: ", tokenizer.vocab_size())
    print(f"Tokenizer saved to {tokenizer_save_path}")
    print("Tokenizing training data...")
    x_train, y_train = prepare_training_data(all_text, tokenizer, sequence_length=context_length)
    dataset = TensorDataset(x_train, y_train)
    train_dataset, val_dataset = split_dataset(dataset, val_split=0.2)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    return tokenizer, train_loader, val_loader


def read_all_documents(directory="training_data"):
    texts = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt") or filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                texts.append(content)
    return texts


if __name__ == "__main__":
    faulthandler.enable()
    do_train(context_length=768, batch_size=64, max_epochs=15, patience=2)
