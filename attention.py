import time
import torch
import torch.nn as nn

ATTENTION_DEBUG = False


class Attention(nn.Module):
    def __init__(self, state_dim, input_dim, output_dim, block_size=50):
        super(Attention, self).__init__()
        self.state_dim = state_dim
        self.block_size = block_size
        self.P = nn.Parameter(torch.eye(state_dim).repeat(state_dim, 1, 1) * 0.1 + 0.01)
        self.Q = nn.Parameter(torch.eye(state_dim, input_dim) * 0.1 + 0.01)
        self.R = nn.Parameter(torch.eye(output_dim, state_dim) * 0.1 + 0.01)
        self.S = nn.Parameter(torch.eye(output_dim, input_dim) * 0.1 + 0.01)
        self.layer_norm = nn.LayerNorm(state_dim)

    def forward(self, x):
        device = x.device
        batch_size, sequence_length, input_dim = x.shape
        outputs = []
        state = torch.zeros(batch_size, self.state_dim, device=device)

        p_expanded = self.P.unsqueeze(0)
        q_expanded = self.Q.expand(batch_size, -1, -1)
        s_expanded = self.S.expand(batch_size, -1, -1)

        for start in range(0, sequence_length, self.block_size):
            end = min(start + self.block_size, sequence_length)
            x_block = x[:, start:end, :]

            for t in range(x_block.shape[1]):
                input_t = x_block[:, t, :].unsqueeze(-1)

                state_quad = torch.matmul(state.unsqueeze(-1), state.unsqueeze(-2))
                state = torch.einsum('bij,bijk->bk', state_quad, p_expanded) + \
                        torch.matmul(q_expanded, input_t).squeeze(-1)

                # Apply layer normalization
                state = self.layer_norm(state)

                output_t = torch.matmul(self.R, state.unsqueeze(-1)).squeeze(-1) + \
                           torch.matmul(s_expanded, input_t).squeeze(-1)
                outputs.append(output_t.unsqueeze(1))

            if ATTENTION_DEBUG and torch.isnan(state).any():
                print(f"NaN detected at step {start}-{end} in state.")
                raise ValueError("NaN detected in state after block processing")

            state = state.detach()

        final_output = torch.cat(outputs, dim=1)

        if ATTENTION_DEBUG and torch.isnan(final_output).any():
            raise ValueError("NaN detected in final output")

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
