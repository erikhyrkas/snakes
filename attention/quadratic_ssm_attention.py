import torch
import torch.nn as nn


class QuadraticSSMAttention(nn.Module):
    def __init__(self, state_dim=448, input_dim=448, output_dim=448):
        super(QuadraticSSMAttention, self).__init__()
        self.state_size = state_dim
        self.input_size = input_dim
        self.output_size = output_dim

        # A, B, and C will be defined dynamically based on the sequence length during forward pass
        self.A = nn.Parameter(torch.randn(state_dim, state_dim) * 0.1 + 0.001)
        self.B = nn.Parameter(torch.randn(state_dim, input_dim) * 0.1 + 0.001)
        self.C = nn.Parameter(torch.randn(output_dim, state_dim) * 0.1 + 0.001)

    def forward(self, x):
        # x is of shape (batch_size, seq_len, input_size)
        batch_size, seq_len, _ = x.size()

        # Compute h_s for all s in batch at once
        h = torch.matmul(x, self.B.T)  # Shape (batch_size, seq_len, state_size)

        # Use broadcasting for batched matrix multiplication
        y = torch.einsum('bts,st,os->bto', h, self.A, self.C)

        return y