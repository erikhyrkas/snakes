import time

import torch
import torch.nn as nn

ATTENTION_DEBUG = False


class Attention(nn.Module):
    def __init__(self, state_dim=448, input_dim=448, output_dim=448, block_size=32, num_heads=4, dropout_rate=0.1):
        super(Attention, self).__init__()
        assert state_dim % num_heads == 0, "State dimension must be divisible by the number of heads."

        self.num_heads = num_heads
        self.head_dim = state_dim // num_heads
        self.block_size = block_size

        # Initialize matrices using identity with added noise
        self.A = nn.Parameter(
            torch.eye(self.head_dim).repeat(num_heads, 1, 1) * 0.1 + torch.randn(num_heads, self.head_dim,
                                                                                 self.head_dim) * 0.01)
        self.B = nn.Parameter(
            torch.eye(self.head_dim, input_dim).repeat(num_heads, 1, 1) * 0.1 + torch.randn(num_heads, self.head_dim,
                                                                                            input_dim) * 0.01)
        self.C = nn.Parameter(
            torch.eye(output_dim // num_heads, self.head_dim).repeat(num_heads, 1, 1) * 0.1 + torch.randn(num_heads,
                                                                                                          output_dim // num_heads,
                                                                                                          self.head_dim) * 0.01)

        self.dropout = nn.Dropout(dropout_rate)
        self.layer_norm = nn.LayerNorm(state_dim)  # Layer normalization
        self.final_linear = nn.Linear(state_dim, output_dim)

    def forward(self, x):
        batch_size, seq_len, _ = x.size()

        # Number of blocks
        num_blocks = (seq_len + self.block_size - 1) // self.block_size

        # Reshape input to add the head dimension
        x = x.unsqueeze(1).repeat(1, self.num_heads, 1, 1)  # Shape: (batch_size, num_heads, seq_len, input_dim)

        # Precompute transposes for efficiency
        B_transpose = self.B.transpose(1, 2)
        C_transpose = self.C.transpose(1, 2)

        y = torch.zeros(batch_size, self.num_heads, seq_len, self.head_dim).to(x.device)

        for i in range(num_blocks):
            start = i * self.block_size
            end = min(start + self.block_size, seq_len)

            x_block = x[:, :, start:end, :]  # Shape: (batch_size, num_heads, block_size, input_dim)

            h_block = torch.einsum('bhij,hjk->bhik', x_block,
                                   B_transpose)  # Shape: (batch_size, num_heads, block_size, head_dim)

            intermediate_result = torch.einsum('bhik,hkj->bhij', h_block, self.A)

            y_block = torch.einsum('bhij,hjk->bhik', intermediate_result, C_transpose)

            y_block = self.dropout(y_block)

            y[:, :, start:end, :].add_(y_block)

        # Concatenate across the head dimension
        y = y.reshape(batch_size, seq_len, -1)  # Shape: (batch_size, seq_len, num_heads * head_dim)

        # Apply layer normalization before the final linear transformation
        y = self.layer_norm(y)

        # Apply final linear transformation and dropout
        final_output = self.final_linear(y)
        final_output = self.dropout(final_output)

        if ATTENTION_DEBUG:
            if torch.isnan(final_output).any():
                raise ValueError("NaN detected in final output")
            if torch.isinf(final_output).any():
                raise ValueError("Infinity detected in final output")

            final_output_norm = torch.norm(final_output, p=2, dim=-1)
            if torch.any(final_output_norm > 1e5):
                print(f"Exploding final output detected with norm: {final_output_norm.max().item()}")
            elif torch.any(final_output_norm < 1e-5):
                print(f"Vanishing final output detected with norm: {final_output_norm.min().item()}")

        return final_output


def example_model():
    model = Attention(state_dim=10, input_dim=5, output_dim=2)
    x = torch.randn(1, 100, 5)  # Batch size of 1, sequence length of 100, input dimension of 5
    output = model(x)
    print(output.shape)  # Expected shape: (1, 100, 2)


def benchmark_model(model, x):
    start_time = time.time()
    output = model(x)
    end_time = time.time()
    return output, end_time - start_time


def test_model():
    state_dim = 10
    input_dim = 5
    output_dim = 2
    sequence_length = 1000
    batch_size = 32

    # random input data
    x = torch.randn(batch_size, sequence_length, input_dim)

    quadratic_model = Attention(state_dim, input_dim, output_dim)

    # Benchmark quadratic model
    quadratic_output, quadratic_time = benchmark_model(quadratic_model, x)

    print(f"Quadratic mode time: {quadratic_time:.6f} seconds")
    print(f"Output shape (Quadratic): {quadratic_output.shape}")


def test_correctness():
    model = Attention(state_dim=10, input_dim=5, output_dim=2)
    x = torch.randn(1, 10, 5)  # A small batch of 10 sequences

    expected_output_shape = (1, 10, 2)  # Expecting output to match input sequence length

    # Run the model
    output = model(x)
    print(f"Output shape: {output.shape}")

    assert output.shape == expected_output_shape, "Output shape does not match expected shape"
    print("Output shape is correct.")


if __name__ == "__main__":
    example_model()
    test_model()
    test_correctness()
