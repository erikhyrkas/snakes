import torch.nn as nn

from ys.language_model.attention import Attention
from ys.language_model.config import Config

# After attention, apply a non-linear transformation.
class AttentionBlock(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.attention = Attention(config)
        self.feed_forward = nn.Sequential(
            nn.Linear(config.embedding_dim, config.embedding_dim),
            nn.GELU(),
            nn.Linear(config.embedding_dim, config.embedding_dim)
        )
        self.layer_norm1 = nn.LayerNorm(config.embedding_dim)  # For attention
        self.layer_norm2 = nn.LayerNorm(config.embedding_dim)  # For FFN
        # self.dropout = nn.Dropout(config.dropout_rate)

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
        attn_out = self.layer_norm1(attn_out + x)

        # Feed-forward block with residual connection and normalization
        ff_out = self.feed_forward(attn_out)
        return self.layer_norm2(ff_out + x)
