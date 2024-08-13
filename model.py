import os
import torch
import torch.nn as nn
from torch import optim
from torch.utils.data import TensorDataset, DataLoader

from state_space_model import StateSpaceModel
from tokenizer import SimpleTokenizer
import numpy as np

from torch.utils.data import random_split


class LanguageModel(nn.Module):
    def __init__(self, vocab_size, mode='quadratic', embedding_dim=256, state_dim=256, output_dim=256):
        super(LanguageModel, self).__init__()
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim)
        self.state_space_model = StateSpaceModel(state_dim=state_dim, input_dim=embedding_dim, output_dim=output_dim,
                                                 mode=mode)
        self.layer_norm = nn.LayerNorm(output_dim)
        self.output_layer = nn.Linear(output_dim, vocab_size)

    def forward(self, input_tokens):
        embedded = self.embedding(input_tokens)
        if len(embedded.shape) == 2:
            embedded = embedded.unsqueeze(0)
        context_representation = self.state_space_model(embedded)
        context_representation = self.layer_norm(context_representation)
        output = self.output_layer(context_representation)
        return output

    def predict_next_token(self, input_tokens, tokenizer):
        output = self.forward(input_tokens)
        next_token_id = torch.argmax(output[:, -1, :], dim=-1).squeeze()
        return tokenizer.detokenize([next_token_id.item()])


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


def train_model(model, train_loader, val_loader, optimizer, criterion, scheduler, epochs=200, max_grad_norm=1.0,
                patience=5):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    early_stopping = EarlyStopping(patience=patience)

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


def prepare_training_data(texts, tokenizer, sequence_length=5):
    x_train, y_train = [], []
    for text in texts:
        tokens = tokenizer.tokenize(text)
        if len(tokens) < sequence_length + 1:
            continue  # Skip sequences that are too short
        for i in range(len(tokens) - sequence_length):
            x_train.append(tokens[i:i + sequence_length])  # Input sequence
            y_train.append(tokens[i + 1:i + sequence_length + 1])  # Target sequence

    x_train = torch.tensor(x_train, dtype=torch.long)
    y_train = torch.tensor(y_train, dtype=torch.long)

    # print(f"x_train shape: {x_train.shape}")  # Expect (num_sequences, sequence_length)
    # print(f"y_train shape: {y_train.shape}")  # Expect (num_sequences, sequence_length)

    return x_train, y_train


def split_dataset(dataset, val_split=0.2):
    val_size = int(len(dataset) * val_split)
    train_size = len(dataset) - val_size
    train_dataset, val_dataset = random_split(dataset, [train_size, val_size])
    return train_dataset, val_dataset


# Note on mode: mamba 2 is quadratic, mamba 1 is linear
def do_train(mode='quadratic', model_save_path="model.bin", tokenizer_save_path="tokenizer.pkl"):
    tokenizer = SimpleTokenizer()
    all_text = read_all_documents()
    tokenizer.build_vocabulary(all_text)

    x_train, y_train = prepare_training_data(all_text, tokenizer, sequence_length=20)
    dataset = TensorDataset(x_train, y_train)
    train_dataset, val_dataset = split_dataset(dataset, val_split=0.2)

    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False)

    model = LanguageModel(tokenizer.vocab_size(), mode=mode)
    optimizer = optim.Adam(model.parameters(), lr=0.0005, weight_decay=1e-5)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=3)
    criterion = nn.CrossEntropyLoss()

    train_model(model, train_loader, val_loader, optimizer, criterion, scheduler, epochs=100, patience=5)

    torch.save(model.state_dict(), model_save_path)
    tokenizer.save(tokenizer_save_path)
    print(f"Model saved to {model_save_path}")
    print(f"Tokenizer saved to {tokenizer_save_path}")


class Completer:
    def __init__(self, mode='quadratic', model_save_path="model.bin", tokenizer_save_path="tokenizer.pkl"):
        self.tokenizer = SimpleTokenizer()
        self.tokenizer.load(tokenizer_save_path)
        self.model = LanguageModel(vocab_size=self.tokenizer.vocab_size(), mode=mode)
        self.model.load_state_dict(torch.load(model_save_path, weights_only=True))
        self.model.eval()

    def complete(self, current_context: str, max_tokens: int = 100):
        result = current_context
        for i in range(max_tokens):
            input_tokens = torch.tensor([self.tokenizer.tokenize(result)])
            next_token = self.model.predict_next_token(input_tokens, self.tokenizer)
            result += next_token
        return result


def read_all_documents(directory="."):
    texts = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt") or filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                texts.append(content)
    return texts


if __name__ == "__main__":
    do_train()
