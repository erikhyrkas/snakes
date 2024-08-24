import torch
import torch.nn as nn


class LinearSSMAttention(nn.Module):
    def __init__(self, state_dim=448, input_dim=448, output_dim=448):
        super(LinearSSMAttention, self).__init__()
        self.A = nn.Parameter(torch.randn(state_dim, state_dim) * 0.1 + 0.001)
        self.B = nn.Parameter(torch.randn(state_dim, input_dim) * 0.1 + 0.001)
        self.C = nn.Parameter(torch.randn(output_dim, state_dim) * 0.1 + 0.001)

    def forward(self, x):
        # x is of shape (batch_size, seq_len, input_size)
        batch_size, seq_len, _ = x.size()
        h = torch.zeros(batch_size, self.A.size(0)).to(x.device)
        y = []

        for t in range(seq_len):
            h = torch.matmul(h, self.A) + torch.matmul(x[:, t, :], self.B)
            y_t = torch.matmul(self.C, h.T).T
            y.append(y_t)

        y = torch.stack(y, dim=1)
        return y
