import torch
import torch.nn as nn
import torch.nn.functional as F


class SSDAttention(nn.Module):
    def __init__(self, state_dim=448, input_dim=448, output_dim=448, sequence_length_threshold=256, num_heads=8,
                 dropout=0.1):
        super(SSDAttention, self).__init__()

        self.sequence_length_threshold = sequence_length_threshold
        self.state_dim = state_dim
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.num_heads = num_heads
        self.dropout = dropout
        self.head_dim = state_dim // num_heads

        # Parameters for linear (SSM) and quadratic (Attention) forms
        self.register_parameter('log_A', nn.Parameter(torch.randn(num_heads, self.head_dim) * 0.1 + 0.1))
        self.B = nn.Parameter(torch.randn(num_heads, self.head_dim) * 0.1 + 0.1)
        self.C = nn.Parameter(torch.randn(num_heads, self.head_dim) * 0.1 + 0.1)

        # Linear and output transformations
        self.input_linear = nn.Linear(input_dim, state_dim)
        self.output_linear = nn.Linear(state_dim, output_dim)
        self.dropout_layer = nn.Dropout(dropout)
        self.layer_norm = nn.LayerNorm(output_dim)

    def forward(self, x):
        batch_size, seq_len, _ = x.size()

        # Linear transformation of input
        x = self.input_linear(x)
        x = x.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

        if seq_len <= self.sequence_length_threshold:
            # Use quadratic (attention-like) computation for shorter sequences
            outputs = self._quadratic_attention(x)
        else:
            # Use linear (state-space) computation for longer sequences
            outputs = self._linear_ssm(x)

        # Apply output transformation and normalization
        outputs = self.output_linear(outputs)
        outputs = self.dropout_layer(outputs)
        outputs = self.layer_norm(outputs)

        return outputs

    def _quadratic_attention(self, x):
        # Implement quadratic (attention-like) computation here
        s = torch.zeros_like(x[:, :, 0, :])
        outputs = []
        for t in range(x.size(2)):
            s = s * torch.exp(-F.softplus(self.log_A)) + self.B * x[:, :, t]
            outputs.append(self.C * s)
        return torch.stack(outputs, dim=2).transpose(1, 2).contiguous().view(x.size(0), x.size(2), -1)

    def _linear_ssm(self, x):
        # Implement linear (state-space) computation here
        s = torch.zeros_like(x[:, :, 0, :])
        outputs = []
        for t in range(x.size(2)):
            s = s * torch.exp(-F.softplus(self.log_A)) + self.B * x[:, :, t]
            outputs.append(self.C * s)
        return torch.stack(outputs, dim=2).transpose(1, 2).contiguous().view(x.size(0), x.size(2), -1)

