import math
import os
import random
import time
from typing import Optional

import torch
import torch.nn as nn
from torch import optim
from torch.utils.data import DataLoader

from early_stopping import EarlyStopping
from model import LanguageModel
from text_dataset import TextDataset
from tokenizer import Tokenizer


def pretty_time(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:0.3f} seconds"
    minutes = int(seconds // 60)
    seconds %= 60
    seconds = int(seconds)
    if minutes < 60:
        return f"{minutes}:{seconds:02d} minutes"
    hours = int(minutes // 60)
    minutes %= 60
    if hours < 24:
        return f"{hours}:{minutes:02d}:{seconds:02d} hours"
    days = int(hours // 24)
    hours %= 24
    return f"{days}:{hours:02d}:{minutes:02d}:{seconds:02d} days"


def train_model(model, train_loader: DataLoader, val_loader: DataLoader, optimizer, criterion, scheduler, epochs=100,
                max_grad_norm=1.0, patience=5, accumulation_steps=4):
    print("Training model...")
    device_name = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using {device_name}")
    device = torch.device(device_name)

    model.to(device)
    early_stopping = EarlyStopping(patience=patience)

    scaler: Optional[torch.amp.GradScaler] = None
    if device_name == "cuda":
        # Initialize GradScaler for mixed precision if using GPU
        scaler = torch.amp.GradScaler('cuda')

    base_path = os.getenv("YS_LLM_BASE_PATH", "./")
    start_time = time.time()

    total_steps = len(train_loader)
    print("First epoch starting...")
    best_loss = float('inf')
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()

        if device_name == "cuda":
            epoch_loss = cuda_train(accumulation_steps, criterion, device, max_grad_norm, model, optimizer,
                                    scaler, train_loader, total_steps, scheduler)
        else:
            epoch_loss = cpu_train(accumulation_steps, criterion, device, max_grad_norm, model, optimizer,
                                   train_loader, total_steps, scheduler)

        if val_loader:
            model.eval()
            if device_name == "cuda":
                val_loss = cuda_validate(criterion, device, model, val_loader)
            else:
                val_loss = cpu_validate(criterion, device, model, val_loader)
            elapsed_time = time.time() - start_time

            print(
                f'Epoch {epoch + 1}, Loss: {epoch_loss / len(train_loader):.3f}, Val Loss: {val_loss} - {pretty_time(elapsed_time)} elapsed')
            loss_to_check = val_loss

            if math.isnan(val_loss) or math.isinf(val_loss):
                print("Stopping due to numerical instability.")
                return False
        else:
            elapsed_time = time.time() - start_time
            print(
                f'Epoch {epoch + 1}, Loss: {epoch_loss / len(train_loader):.3f} - {pretty_time(elapsed_time)} elapsed')
            loss_to_check = epoch_loss

        if math.isnan(epoch_loss) or math.isinf(epoch_loss):
            print("Stopping due to numerical instability.")
            return False

        if loss_to_check < best_loss:
            best_loss = loss_to_check
            torch.save(model.state_dict(), f"{base_path}model_checkpoint.bin")
            torch.save(optimizer.state_dict(), f'{base_path}optimizer_checkpoint.bin')
            torch.save(scheduler.state_dict(), f'{base_path}scheduler_checkpoint.bin')
            print(f"New best model saved at epoch {epoch + 1}")

        early_stopping.check(loss_to_check)
        if early_stopping.stop_training:
            print(f"Early stopping triggered at epoch {epoch + 1}")
            break

    return True


def cpu_validate(criterion, device, model, val_loader):
    val_loss = 0.0
    with torch.no_grad():
        for inputs, targets in val_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            loss = calc_val_loss(criterion, inputs, model, targets)
            val_loss += loss.item()
    val_loss /= len(val_loader)
    return val_loss


def cuda_validate(criterion, device, model, val_loader):
    val_loss = 0.0
    with torch.no_grad():
        for inputs, targets in val_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            with torch.amp.autocast('cuda'):  # Use autocast for validation as well on GPU
                loss = calc_val_loss(criterion, inputs, model, targets)
            val_loss += loss.item()
    val_loss /= len(val_loader)
    return val_loss


def calc_val_loss(criterion, inputs, model, targets):
    outputs = model(inputs)
    outputs = outputs.view(-1, outputs.size(-1))
    targets = targets.view(-1)
    return criterion(outputs, targets)


def cuda_train(accumulation_steps, criterion, device, max_grad_norm, model, optimizer,
               scaler: torch.amp.GradScaler, train_loader, total_steps, scheduler):
    epoch_loss = 0.0
    start_time = time.time()
    for i, (inputs, targets, masks) in enumerate(train_loader):
        inputs, targets, masks = inputs.to(device), targets.to(device), masks.to(device)

        # Use autocast for mixed precision on GPU
        with torch.amp.autocast('cuda'):
            outputs = model(inputs)
            loss = calculate_loss(accumulation_steps, criterion, masks, outputs, targets)
        scaler.scale(loss).backward()

        step = i + 1

        # Accumulate gradients and update model after a certain number of steps
        if step % accumulation_steps == 0:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_grad_norm)
            optimizer.step()
            scaler.update()
            if scheduler.last_epoch < scheduler.total_steps:
                scheduler.step()  # Update learning rate after optimizer step
            optimizer.zero_grad()  # Reset gradients for the next accumulation cycle

        epoch_loss += loss.item() * accumulation_steps  # Multiply to undo the earlier division
        elapsed_time = time.time() - start_time
        estimated_completion = (elapsed_time / step) * total_steps
        estimated_remaining = estimated_completion - elapsed_time
        print(f'Step {step}/{total_steps} Loss: {epoch_loss / step:.3f} - {pretty_time(elapsed_time)} '
              f'elapsed/~{pretty_time(estimated_remaining)} remaining                        ',
              end='\r', flush=True)
        if math.isnan(epoch_loss) or math.isinf(epoch_loss):
            break
    print()
    return epoch_loss


def cpu_train(accumulation_steps, criterion, device, max_grad_norm, model, optimizer, train_loader, total_steps,
              scheduler):
    epoch_loss = 0.0
    start_time = time.time()
    for i, (inputs, targets, masks) in enumerate(train_loader):
        inputs, targets, masks = inputs.to(device), targets.to(device), masks.to(device)

        # Full precision for CPU
        outputs = model(inputs)
        loss = calculate_loss(accumulation_steps, criterion, masks, outputs, targets)
        loss.backward()

        step = i + 1
        # Accumulate gradients and update model after a certain number of steps
        if step % accumulation_steps == 0:
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_grad_norm)
            optimizer.step()
            if scheduler.last_epoch < scheduler.total_steps:
                scheduler.step()  # Update learning rate after optimizer step
            optimizer.zero_grad()  # Reset gradients for the next accumulation cycle

        epoch_loss += loss.item() * accumulation_steps  # Multiply to undo the earlier division
        elapsed_time = time.time() - start_time
        estimated_completion = (elapsed_time / step) * total_steps
        estimated_remaining = estimated_completion - elapsed_time
        print(f'Step {step}/{total_steps} Loss: {epoch_loss / step:.3f} - {pretty_time(elapsed_time)} '
              f'elapsed/~{pretty_time(estimated_remaining)} remaining                        ',
              end='\r', flush=True)
        if math.isnan(epoch_loss) or math.isinf(epoch_loss):
            break
    print()
    return epoch_loss


def calculate_loss(accumulation_steps, criterion, masks, outputs, targets):
    batch_size, sequence_length, vocab_size = outputs.shape
    outputs = outputs.view(batch_size * sequence_length, vocab_size)
    targets = targets.view(batch_size * sequence_length)
    masks = masks.view(batch_size * sequence_length)
    loss = criterion(outputs, targets)
    loss = (loss * masks).sum() / masks.sum()
    loss = loss / accumulation_steps
    return loss


def get_training_file_names(directory="training_data"):
    base_path = os.getenv("YS_LLM_BASE_PATH", "./")
    file_names = []
    for filename in os.listdir(f"{base_path}{directory}"):
        if filename.endswith(".txt") or filename.endswith(".md"):
            filepath = os.path.join(f"{base_path}{directory}", filename)
            file_names.append(filepath)
    return file_names


def base_model_train(learning_rate, training_sequence_length, batch_size, max_epochs,
                     training_folder="training_data", patience=10, use_validation_split=True,
                     block_length=32):
    print(
        f"LR: {learning_rate} Training Sequence Length: {training_sequence_length} Batch Size: {batch_size} Epochs: {max_epochs} training folder: {training_folder}")
    base_path = os.getenv("YS_LLM_BASE_PATH", "./")
    model_path = f"{base_path}model.bin"

    tokenizer = train_or_load_tokenizer(training_folder)

    training_file_names = get_training_file_names(training_folder)
    # Split file names for training and validation
    random.shuffle(training_file_names)
    if use_validation_split:
        split_index = int(0.8 * len(training_file_names))
        train_files = training_file_names[:split_index]
        val_files = training_file_names[split_index:]
    else:
        train_files = training_file_names
        val_files = []

    # DataLoader for batching (shuffle is done within the TextDataset)
    train_dataset = TextDataset(train_files, tokenizer, training_sequence_length, batch_size,
                                cache_dir='./training_data_cache', block_length=block_length)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=False)

    if use_validation_split:
        val_loader = None
    else:
        val_dataset = TextDataset(val_files, tokenizer, training_sequence_length, batch_size,
                                  cache_dir='./validation_data_cache', block_length=block_length)
        val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    number_of_samples = len(train_dataset)
    print(f"Number of training samples: {number_of_samples} for sequence length: {training_sequence_length}")

    vocab_size = tokenizer.vocab_size()
    print(f"Vocabulary size: {vocab_size}")

    model = LanguageModel(tokenizer.vocab_size(), block_length=block_length)
    print(f"Number of parameters: {model.count_parameters()}")

    base_path = os.getenv("YS_LLM_BASE_PATH", "./")
    if os.path.exists(f"{base_path}model_checkpoint.bin"):
        model.load_state_dict(torch.load(f"{base_path}model_checkpoint.bin", weights_only=False))
        print(f"Resumed training from {base_path}model_checkpoint.bin")

    accumulation_steps = 4
    steps_per_epoch = math.ceil(number_of_samples / batch_size)
    total_training_steps = (math.ceil(steps_per_epoch / accumulation_steps) * max_epochs) + 1

    # total_training_steps = (number_of_samples // (batch_size * accumulation_steps)) * max_epochs
    # if number_of_samples % (batch_size * accumulation_steps) != 0:
    #     # Add one step for each epoch to cover the last incomplete batch
    #     total_training_steps += max_epochs

    optimizer = optim.AdamW(model.parameters(), lr=learning_rate, weight_decay=1e-5)
    scheduler = optim.lr_scheduler.OneCycleLR(optimizer, max_lr=0.0005, total_steps=total_training_steps)
    criterion = nn.CrossEntropyLoss()

    if os.path.exists(f'{base_path}optimizer_checkpoint.bin'):
        optimizer.load_state_dict(torch.load(f'{base_path}optimizer_checkpoint.bin', weights_only=False))
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # Ensure all optimizer states are on the correct device
        for state in optimizer.state.values():
            for k, v in state.items():
                if isinstance(v, torch.Tensor):
                    state[k] = v.to(device)
    if os.path.exists(f'{base_path}scheduler_checkpoint.bin'):
        scheduler.load_state_dict(torch.load(f'{base_path}scheduler_checkpoint.bin', weights_only=False))

    model_trained = train_model(model, train_loader, val_loader, optimizer, criterion, scheduler, epochs=max_epochs,
                                patience=patience, accumulation_steps=accumulation_steps)
    if model_trained:
        print("Saving model...")
        torch.save(model.state_dict(), model_path)
        print(f"Model saved to {model_path}")
        print(f"Number of parameters: {model.count_parameters()}")
        print(f"Vocabulary size: {vocab_size}")
    return model_trained


def train_or_load_tokenizer(training_folder, tokenizer_file_name='tokenizer.pkl'):
    base_path = os.getenv("YS_LLM_BASE_PATH", "./")
    tokenizer_path = f"{base_path}{tokenizer_file_name}"

    print("Loading and tokenizing training data...")
    training_file_names = get_training_file_names(training_folder)
    # Split file names for training and validation
    random.shuffle(training_file_names)
    # Initialize the tokenizer
    tokenizer = Tokenizer()
    if os.path.exists(tokenizer_path):
        tokenizer.load(tokenizer_path)
        print("Loaded existing tokenizer.")
    else:
        # Update tokenizer vocab by iterating over each document
        for file_path in training_file_names:
            with open(file_path, 'r', encoding='utf-8') as file:
                document = file.read()
                tokenizer.learn_new_vocab(document)  # Add document content to vocab
                del document  # Free memory as soon as possible

        # Save the tokenizer with the built vocabulary
        tokenizer.save(tokenizer_path)
    return tokenizer


def cleanup_old_bins(remove_tokenizer=False, clear_cache=False):
    if os.path.exists("scheduler_checkpoint.bin"):
        os.remove("scheduler_checkpoint.bin")
    if os.path.exists("optimizer_checkpoint.bin"):
        os.remove("optimizer_checkpoint.bin")
    if os.path.exists("model_checkpoint.bin"):
        os.remove("model_checkpoint.bin")
    if os.path.exists("model.bin"):
        os.remove("model.bin")
    if clear_cache and os.path.exists("fine_tuning"):
        os.removedirs("fine_tuning")
    if clear_cache and os.path.exists("training_data_cache"):
        os.removedirs("training_data_cache")
    if clear_cache and os.path.exists("validation_data_cache"):
        os.removedirs("validation_data_cache")
    if remove_tokenizer and os.path.exists("tokenizer.pkl"):
        os.remove("tokenizer.pkl")


if __name__ == "__main__":
    # cleanup_old_bins()

    train_or_load_tokenizer("training_data")
    TRAIN_FOLDER = "training_data"

    trained = False
    while not trained:
        trained = base_model_train(0.0005, 32, 128, 30, patience=3, training_folder=TRAIN_FOLDER,
                                   use_validation_split=False)

    # we don't want to keep the model from warm up.
    # if os.path.exists("model.bin"):
    #     os.remove("model.bin")

    # we might have numerical instability, but we're determined.
    while not trained:
        trained = base_model_train(0.0005, 96, 64, 200, patience=5, training_folder=TRAIN_FOLDER,
                                   use_validation_split=False)

    # base_model_train(0.0005, 512, 8, 20, patience=2, training_folder=TRAIN_FOLDER,
    #                  use_validation_split=False, block_length=64)
