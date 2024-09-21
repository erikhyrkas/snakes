import math

import torch
from torch import nn


# The original sinusoidal positional encoding
# add to __init__():
# self.positional_encoding = PositionalEncoding(config.embedding_dim)
# add to forward():
# embedded = self.positional_encoding(embedded)
class PositionalEncoding(nn.Module):
    def __init__(self, embedding_dim, max_len=512):
        super().__init__()
        self.embedding_dim = embedding_dim
        self.register_buffer('pe', self.create_positional_encodings(max_len))

    def create_positional_encodings(self, max_len):
        pe = torch.zeros(max_len, self.embedding_dim)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, self.embedding_dim, 2).float() * (-math.log(10000.0) / self.embedding_dim))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        return pe.unsqueeze(0)  # Shape [1, max_len, embedding_dim]

    def forward(self, x):
        # Dynamically extend the positional encodings if necessary
        seq_len = x.size(1)
        if seq_len > self.pe.size(1):  # If sequence length is greater than current positional encodings
            self.pe = self.create_positional_encodings(seq_len).to(self.pe.device)  # Extend the positional encodings

        # Add positional encoding to the input tensor
        x = x + self.pe[:, :seq_len, :]
        return x