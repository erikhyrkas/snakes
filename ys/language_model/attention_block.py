
import torch.nn as nn

from ys.language_model.attention import Attention
from ys.language_model.config import Config


class AttentionBlock(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.attention = Attention(config)
        self.feed_forward = nn.Sequential(
            nn.Linear(config.embedding_dim, config.state_dim),
            nn.GELU(),
            nn.Linear(config.state_dim, config.embedding_dim)
        )
        self.layer_norm1 = nn.LayerNorm(config.embedding_dim)  # For attention
        self.layer_norm2 = nn.LayerNorm(config.embedding_dim)  # For FFN
        self.dropout = nn.Dropout(config.dropout_rate)

    def forward(self, x):
        # Attention block with residual connection and normalization
        attn_out = self.attention(x)
        x = self.layer_norm1(attn_out + x)  # Residual connection and LayerNorm

        # Feed-forward block with residual connection and normalization
        ff_out = self.feed_forward(x)
        x = self.layer_norm2(ff_out + x)  # Residual connection and LayerNorm

        return x
