from torch import nn

from ys.language_model.attention import Attention


class StackedAttention(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.layers = nn.ModuleList([Attention(config) for _ in range(config.num_layers)])
        self.layer_norm = nn.LayerNorm(config.embedding_dim)

    def forward(self, x):
        for layer in self.layers:
            x = layer(x) + x  # Residual connection
            x = self.layer_norm(x)
        return x
