import torch
import torch.nn as nn


class BlockDecomposedSSMAttention(nn.Module):
    def __init__(self, state_dim=448, input_dim=448, output_dim=448, block_size=32, dropout_rate=0.1):
        super(BlockDecomposedSSMAttention, self).__init__()
        self.state_size = state_dim
        self.input_size = input_dim
        self.output_size = output_dim
        self.block_size = block_size

        # Initialize matrices with adjusted initialization
        self.A = nn.Parameter(torch.randn(state_dim, state_dim) * 0.1 + 0.001)
        self.B = nn.Parameter(torch.randn(state_dim, input_dim) * 0.1 + 0.001)
        self.C = nn.Parameter(torch.randn(output_dim, state_dim) * 0.1 + 0.001)
        self.dropout = nn.Dropout(dropout_rate)

    def forward(self, x):
        # x is of shape (batch_size, seq_len, input_size)
        batch_size, seq_len, _ = x.size()

        # Number of blocks
        num_blocks = (seq_len + self.block_size - 1) // self.block_size

        # Precompute transposes for efficiency
        B_transpose = self.B.T
        C_transpose = self.C.T

        y = torch.zeros(batch_size, seq_len, self.output_size).to(x.device)

        for i in range(num_blocks):
            # Define the start and end of the block
            start = i * self.block_size
            end = min(start + self.block_size, seq_len)

            # Extract the block
            x_block = x[:, start:end, :]  # x_block shape: (batch_size, block_size, input_size)

            # Compute h_block: (batch_size, block_size, state_size)
            h_block = torch.bmm(x_block, B_transpose.unsqueeze(0).expand(batch_size, -1, -1))

            # Compute intermediate_result: (batch_size, block_size, state_size)
            intermediate_result = torch.bmm(h_block, self.A.unsqueeze(0).expand(batch_size, -1, -1))

            # Compute y_block: (batch_size, block_size, output_size)
            y_block = torch.bmm(intermediate_result, C_transpose.unsqueeze(0).expand(batch_size, -1, -1))

            y_block = self.dropout(y_block)  # Apply dropout

            # Store the result in the corresponding positions using in-place addition
            y[:, start:end, :].add_(y_block)

        return y
