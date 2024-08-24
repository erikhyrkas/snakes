import torch
from torch import nn


#  Good ole rotary positional embeddings
class RoPE(nn.Module):
    def __init__(self, embedding_dim):
        super(RoPE, self).__init__()
        self.embedding_dim = embedding_dim
        self.theta = 10000.0 ** (torch.arange(0, embedding_dim, 2).float() / embedding_dim)

    def forward(self, x):
        device = x.device  # Get the device of the input tensor
        theta = self.theta.to(device)  # Move self.theta to the correct device

        seq_len = x.size(1)
        pos = torch.arange(seq_len, dtype=torch.float32, device=device).unsqueeze(1)
        angle_rates = pos / theta
        cos_pos = torch.cos(angle_rates)
        sin_pos = torch.sin(angle_rates)

        x1 = x[..., 0::2] * cos_pos - x[..., 1::2] * sin_pos
        x2 = x[..., 0::2] * sin_pos + x[..., 1::2] * cos_pos

        return torch.cat([x1, x2], dim=-1)