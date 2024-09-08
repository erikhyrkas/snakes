import torch
from torch import nn


class StructuredMasking(nn.Module):
    """
    Replaces positional encoding with structured masking.
    The mask is now adaptive, not limited by a fixed max length.
    """
    def __init__(self, embedding_dim, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.embedding_dim = embedding_dim
        self.mask = nn.Parameter(torch.ones(1, embedding_dim))

    def forward(self, x):
        seq_len = x.size(1)  # Adapt the mask to the current sequence length
        mask = self.mask.repeat(seq_len, 1)  # Extend mask dynamically based on the sequence length
        return x * mask


class QuadraticStateSpaceLayer(nn.Module):
    """
    Optimized Quadratic State Space Layer using semiseparable matrix operations.
    Now adapted for potentially unlimited context size.
    """
    def __init__(self, embedding_dim, state_dim):
        super().__init__()
        self.state_dim = state_dim
        self.A = nn.Linear(state_dim, state_dim)
        self.B = nn.Linear(embedding_dim, state_dim)
        self.C = nn.Linear(state_dim, embedding_dim)
        self.semiseparable_matrix = nn.Parameter(torch.rand(state_dim, embedding_dim))

    def forward(self, x, state):
        new_state = self.A(state) + torch.matmul(self.semiseparable_matrix, x.transpose(-1, -2)).transpose(-1, -2)
        output = self.C(new_state)
        return output, new_state


class MultiHeadQuadraticStateSpaceAttention(nn.Module):
    def __init__(self, embedding_dim, state_dim, num_heads, use_quadratic=True):
        super().__init__()
        self.num_heads = num_heads
        self.embedding_dim = embedding_dim
        self.state_dim = state_dim
        self.head_dim = embedding_dim // num_heads
        assert self.head_dim * num_heads == embedding_dim, "embedding_dim must be divisible by num_heads"

        self.heads = nn.ModuleList([
            QuadraticStateSpaceLayer(self.head_dim, state_dim) if use_quadratic
            else nn.GRU(self.head_dim, state_dim, batch_first=True)
            for _ in range(num_heads)
        ])

        self.output_projection = nn.Linear(embedding_dim, embedding_dim)

    def forward(self, x, state):
        batch_size, seq_len, _ = x.size()
        assert batch_size > 0, "Batch size should never be less than 1."

        if state is None:
            state = torch.zeros(self.num_heads, batch_size, self.state_dim, device=x.device)

        # Split input into heads without altering the batch size
        x_heads = x.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(2, 1)

        # Check if batch size remains consistent
        assert x_heads.size(0) == batch_size, f"Expected batch size {batch_size}, but got {x_heads.size(0)}."

        outputs = []
        new_states = []
        for i, head in enumerate(self.heads):
            # Get the i-th head input with batch_size unchanged (batch_size, seq_len, head_dim)
            x_head = x_heads[:, i]  # shape: (batch_size, seq_len, head_dim)

            # Ensure hidden state matches the batch size for GRU
            if isinstance(head, nn.GRU):
                head_output, new_state = head(x_head, state[i].unsqueeze(0).detach())
                new_state = new_state.squeeze(0)
            else:
                head_output, new_state = head(x_head, state[i].detach())  # Detach state

            outputs.append(head_output)
            new_states.append(new_state)

        # Concatenate outputs from all heads
        output = torch.cat(outputs, dim=-1)
        new_state = torch.stack(new_states)

        # Project back to the original embedding dimension
        output = self.output_projection(output)
        return output, new_state


class LayerNormalization(nn.Module):
    def __init__(self, embedding_dim, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.norm = nn.LayerNorm(embedding_dim)

    def forward(self, x):
        return self.norm(x)


class AttentionBlock(nn.Module):
    """
    This block supports unlimited context size by adapting to dynamic sequence lengths.
    """

    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.structured_masking = StructuredMasking(config.embedding_dim) if config.use_structured_mask else None
        self.state_space_attention = MultiHeadQuadraticStateSpaceAttention(
            embedding_dim=config.embedding_dim,
            state_dim=config.state_dim,
            num_heads=config.num_heads,
            use_quadratic=config.use_quadratic
        )
        self.layer_norm = LayerNormalization(config.embedding_dim) if config.use_layer_norm else None
        self.residual = config.use_residual
        self.state = None

    def forward(self, x):
        if self.structured_masking:
            x = self.structured_masking(x)
        attention_output, self.state = self.state_space_attention(x, self.state)

        # Add residual connection if enabled, but detach x to prevent retaining the computational graph
        if self.residual:
            attention_output = attention_output + x.detach()

        if self.layer_norm:
            attention_output = self.layer_norm(attention_output)

        return attention_output
