import math
import os
import random
import time
from typing import Optional

import torch
import torch.nn as nn
from torch import optim
from torch.utils.data import DataLoader

from ys.language_model.config import Config
from ys.language_model.language_model import LanguageModel
from ys.tokenizer.tokenizer import Tokenizer
from ys.training.early_stopping import EarlyStopping
from ys.training.text_dataset import TextDataset


def get_base_path():
    base_path = os.getenv("YS_LLM_BASE_PATH", "./")
    return base_path


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


def train_model(model, train_loader: DataLoader, val_loader: Optional[DataLoader], optimizer, criterion, scheduler,
                epochs=100, max_grad_norm=1.0, patience=5, accumulation_steps=8):
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

    base_path = get_base_path()
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

        if val_loader is not None:
            model.eval()
            if device_name == "cuda":
                val_loss = cuda_validate(criterion, device, model, val_loader)
            else:
                val_loss = cpu_validate(criterion, device, model, val_loader)
            elapsed_time = time.time() - start_time

            print(
                f'Epoch {epoch + 1}, Loss: {epoch_loss:.3f}, Val Loss: {val_loss:.3f} - {pretty_time(elapsed_time)} elapsed')
            loss_to_check = val_loss

            if math.isnan(val_loss) or math.isinf(val_loss):
                print("Stopping due to numerical instability.")
                return False
        else:
            elapsed_time = time.time() - start_time
            print(
                f'Epoch {epoch + 1}, Loss: {epoch_loss:.3f} - {pretty_time(elapsed_time)} elapsed')
            loss_to_check = epoch_loss

        if math.isnan(epoch_loss) or math.isinf(epoch_loss):
            print("Stopping due to numerical instability.")
            return False

        if loss_to_check < best_loss:
            best_loss = loss_to_check
            model.save(f"{base_path}model/model_checkpoint.bin", f"{base_path}model/model_config.json")
            torch.save(optimizer.state_dict(), f'{base_path}model/optimizer_checkpoint.bin')
            torch.save(scheduler.state_dict(), f'{base_path}model/scheduler_checkpoint.bin')
            print(f"New best model saved at epoch {epoch + 1}")

        early_stopping.check(loss_to_check)
        if early_stopping.stop_training:
            print(f"Early stopping triggered at epoch {epoch + 1}")
            break

    return True


def cpu_validate(criterion, device, model, val_loader):
    val_loss = 0.0
    with torch.no_grad():
        for inputs, targets, masks in val_loader:
            inputs, targets, masks = inputs.to(device), targets.to(device), masks.to(device)
            loss = calc_val_loss(criterion, inputs, model, targets, masks)
            val_loss += loss.item()
    val_loss /= len(val_loader)
    return val_loss


def cuda_validate(criterion, device, model, val_loader):
    val_loss = 0.0
    with torch.no_grad():
        for inputs, targets, masks in val_loader:
            inputs, targets, masks = inputs.to(device), targets.to(device), masks.to(device)
            with torch.amp.autocast('cuda'):
                loss = calc_val_loss(criterion, inputs, model, targets, masks)
            val_loss += loss.item()
    val_loss /= len(val_loader)
    return val_loss


def calc_val_loss(criterion, inputs, model, targets, masks):
    outputs = model(inputs)
    outputs = outputs.view(-1, outputs.size(-1))
    targets = targets.view(-1)
    masks = masks.view(-1)
    loss = criterion(outputs, targets)
    loss = (loss * masks).sum() / masks.sum()
    return loss


def cuda_train(accumulation_steps, criterion, device, max_grad_norm, model, optimizer,
               scaler: torch.amp.GradScaler, train_loader, total_steps, scheduler):
    epoch_loss = torch.tensor(0.0)
    grad_norm = torch.tensor(0.0)
    start_time = time.time()
    step = 1
    lr = scheduler.get_last_lr()[0]
    blank_line = ' ' * 80
    for i, (inputs, targets, masks) in enumerate(train_loader):
        inputs, targets, masks = inputs.to(device), targets.to(device), masks.to(device)

        with torch.amp.autocast('cuda'):
            outputs = model(inputs)
            loss = calculate_loss(criterion, masks, outputs, targets)

        # Loss scaling
        scaled_loss = scaler.scale(loss)

        # Gradient accumulation
        scaled_loss = scaled_loss / accumulation_steps
        scaled_loss.backward()

        step = i + 1

        if step % accumulation_steps == 0 or step == len(train_loader):
            # Unscale gradients
            # scaler.unscale_(optimizer)  #optional?

            # Clip gradients
            grad_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), max_grad_norm)

            if torch.isfinite(grad_norm):
                scaler.step(optimizer)
                scaler.update()
            else:
                print(f"\nGradient norm is {grad_norm}. Skipping this batch.")

            optimizer.zero_grad(set_to_none=True)

            if scheduler.last_epoch < scheduler.total_steps:
                scheduler.step()

        epoch_loss += loss.item()
        if step % 10 == 0:  # Log every 10 steps
            elapsed_time = time.time() - start_time
            estimated_completion = (elapsed_time / step) * total_steps
            estimated_remaining = estimated_completion - elapsed_time
            lr = scheduler.get_last_lr()[0]
            print(
                f'Step {step}/{total_steps} Loss: {epoch_loss / step:.3f} LR: {lr:.5f} Grad Norm: {grad_norm:.3f} - {pretty_time(elapsed_time)} '
                f'elapsed/~{pretty_time(estimated_remaining)} remaining{blank_line}', end='\r', flush=True)

        if not torch.isfinite(epoch_loss):
            print(f"\nStopping epoch early due to non-finite loss: {epoch_loss}")
            return float('inf')

    elapsed_time = time.time() - start_time
    print(f'Step {step}/{total_steps} Loss: {epoch_loss / step:.3f} LR: {lr:.5f} - {pretty_time(elapsed_time)} '
          f'elapsed{blank_line}')
    return epoch_loss / total_steps


def cpu_train(accumulation_steps, criterion, device, max_grad_norm, model, optimizer, train_loader, total_steps,
              scheduler):
    epoch_loss = 0.0
    start_time = time.time()
    for i, (inputs, targets, masks) in enumerate(train_loader):
        inputs, targets, masks = inputs.to(device), targets.to(device), masks.to(device)

        outputs = model(inputs)
        loss = calculate_loss(criterion, masks, outputs, targets)
        normalized_loss = loss / accumulation_steps
        normalized_loss.backward()

        step = i + 1
        if step % accumulation_steps == 0:
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_grad_norm)
            optimizer.step()
            if scheduler.last_epoch < scheduler.total_steps:
                scheduler.step()
            optimizer.zero_grad()

        epoch_loss += loss.item()
        elapsed_time = time.time() - start_time
        estimated_completion = (elapsed_time / step) * total_steps
        estimated_remaining = estimated_completion - elapsed_time
        print(f'Step {step}/{total_steps} Loss: {epoch_loss / step:.3f} - {pretty_time(elapsed_time)} '
              f'elapsed/~{pretty_time(estimated_remaining)} remaining', end='\r', flush=True)
        if math.isnan(epoch_loss) or math.isinf(epoch_loss):
            break
    print()
    return epoch_loss / total_steps


def calculate_loss(criterion, masks, outputs, targets):
    batch_size, sequence_length, vocab_size = outputs.shape
    outputs = outputs.view(batch_size * sequence_length, vocab_size)
    targets = targets.view(batch_size * sequence_length)
    masks = masks.view(batch_size * sequence_length)
    loss = criterion(outputs, targets)
    loss = (loss * masks).sum() / masks.sum()
    return loss


def get_training_file_names(directory="training_data"):
    base_path = get_base_path()
    file_names = []
    for filename in os.listdir(f"{base_path}{directory}"):
        if filename.endswith(".txt") or filename.endswith(".md"):
            filepath = os.path.join(f"{base_path}{directory}", filename)
            file_names.append(filepath)
    return file_names


def base_model_train(learning_rate, training_sequence_length, batch_size, max_epochs,
                     training_folder="training_data", patience=10, use_validation_split: bool = True):
    print(
        f"LR: {learning_rate:.5f} Training Sequence Length: {training_sequence_length:,} Batch Size: {batch_size} Epochs: {max_epochs} training folder: {training_folder}")
    print(f"Use Validation Split: {use_validation_split}")
    base_path = get_base_path()
    model_path = f"{base_path}model/model.bin"
    config_path = f"{base_path}model/model_config.json"

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
                                cache_dir='./training_data_cache')
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=False)

    if not use_validation_split:
        val_loader = None
    else:
        val_dataset = TextDataset(val_files, tokenizer, training_sequence_length, batch_size,
                                  cache_dir='./validation_data_cache')
        val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    number_of_samples = len(train_dataset)
    print(f"Number of training samples: {number_of_samples:,} for sequence length: {training_sequence_length:,}")

    vocab_size = tokenizer.vocab_size()
    print(f"Vocabulary size: {vocab_size:,}")


    base_path = get_base_path()
    if os.path.exists(f"{base_path}model/model_checkpoint.bin"):
        model = LanguageModel.load(f"{base_path}model/model_checkpoint.bin", config_path)
        print(f"Resumed training from {base_path}model/model_checkpoint.bin")
    else:
        model = LanguageModel(Config(vocab_size=tokenizer.vocab_size()))

    print(f"Number of parameters: {model.count_parameters():,}")

    accumulation_steps = 16
    steps_per_epoch = math.ceil(number_of_samples / batch_size)
    total_training_steps = (math.ceil(steps_per_epoch / accumulation_steps) * max_epochs) + 1
    warmup_steps = int(0.1 * total_training_steps)

    optimizer = optim.AdamW(model.parameters(), lr=learning_rate, weight_decay=0.01, eps=1e-8)
    scheduler = optim.lr_scheduler.OneCycleLR(
        optimizer,
        max_lr=learning_rate,
        total_steps=total_training_steps,
        pct_start=warmup_steps / total_training_steps,
        anneal_strategy='linear',
        cycle_momentum=False,
        div_factor=25,  # Starts the learning rate at max_lr / 25
        final_div_factor=10000  # Ends the learning rate at max_lr / 10000
    )
    criterion = nn.CrossEntropyLoss(reduction='none')

    if os.path.exists(f'{base_path}model/optimizer_checkpoint.bin'):
        optimizer.load_state_dict(torch.load(f'{base_path}model/optimizer_checkpoint.bin', weights_only=False))
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # Ensure all optimizer states are on the correct device
        for state in optimizer.state.values():
            for k, v in state.items():
                if isinstance(v, torch.Tensor):
                    state[k] = v.to(device)
    if os.path.exists(f'{base_path}model/scheduler_checkpoint.bin'):
        scheduler.load_state_dict(torch.load(f'{base_path}model/scheduler_checkpoint.bin', weights_only=False))

    model_trained = train_model(model, train_loader, val_loader, optimizer, criterion, scheduler, epochs=max_epochs,
                                patience=patience, accumulation_steps=accumulation_steps)
    if model_trained:
        print("Saving model...")
        model.save(model_path, config_path)
        print(f"Model saved to {model_path}")
        print(f"Number of parameters: {model.count_parameters():,}")
        print(f"Vocabulary size: {vocab_size:,}")
    return model_trained


def train_or_load_tokenizer(training_folder, tokenizer_file_name='tokenizer.pkl'):
    base_path = get_base_path()
    tokenizer_path = f"{base_path}model/{tokenizer_file_name}"

    print("Loading and tokenizing training data...")
    training_file_names = get_training_file_names(training_folder)
    random.shuffle(training_file_names)
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

        tokenizer.save(tokenizer_path)
    return tokenizer
