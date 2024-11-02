import torch.nn as nn

from ys.language_model.attention import Attention
from ys.language_model.config import Config


# After attention, apply a non-linear transformation.
class AttentionBlock(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.attention = Attention(config)
        self.feed_forward = nn.Sequential(
            nn.Linear(config.embedding_dim, config.state_dim),
            nn.GELU(),
            nn.Linear(config.state_dim, config.embedding_dim)
        )
        # Apply weight initialization
        self.apply(self._init_weights)

    @staticmethod
    def _init_weights(m):
        if isinstance(m, nn.Linear):
            nn.init.xavier_uniform_(m.weight)
            if m.bias is not None:
                nn.init.constant_(m.bias, 0)

    def forward(self, x):
        # Attention block with residual connection and normalization
        attn_out = self.attention(x)
        # Feed-forward block with residual connection and normalization
        return self.feed_forward(attn_out)
