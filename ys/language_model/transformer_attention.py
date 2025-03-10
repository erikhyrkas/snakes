import torch
import torch.nn as nn

from ys.language_model.config import Config


class TransformerBlock(nn.Module):
    """
    A single Transformer block that includes:
      1) Multi-Head Self-Attention (using PyTorch's nn.MultiheadAttention)
      2) A feed-forward sub-layer with a non-linear activation
      3) Residual connections + LayerNorm on both sub-layers (Pre-Norm variant)
    """

    def __init__(self, config: Config):
        super().__init__()

        self.embedding_dim = config.embedding_dim
        self.num_heads = config.num_transformer_heads
        self.dropout = config.dropout_rate

        # If not provided, default feed-forward dimension to 4x embedding (common in literature)
        feedforward_dim = 4 * self.embedding_dim

        # Multi-Head Self-Attention layer
        self.attention = nn.MultiheadAttention(
            embed_dim=self.embedding_dim,
            num_heads=self.num_heads,
            dropout=self.dropout,
            batch_first=True
        )

        # Layer norms (Pre-Norm style)
        self.norm1 = nn.LayerNorm(self.embedding_dim)
        self.norm2 = nn.LayerNorm(self.embedding_dim)

        # Feed-forward sub-layer
        self.feed_forward = nn.Sequential(
            nn.Linear(self.embedding_dim, feedforward_dim),
            nn.GELU(),  # or nn.ReLU() or nn.SiLU(), etc.
            nn.Dropout(self.dropout),
            nn.Linear(feedforward_dim, self.embedding_dim),
        )

        self.dropout_layer = nn.Dropout(self.dropout)

    def forward(self, x, key_padding_mask=None, attn_mask=None):
        """
        Args:
            x: Tensor of shape (batch_size, seq_len, embedding_dim).
            key_padding_mask: (Optional) Boolean mask with shape (batch_size, seq_len),
                              where True means "ignore this token".
            attn_mask: (Optional) Custom attention mask of shape (seq_len, seq_len).
        Returns:
            Output of shape (batch_size, seq_len, embedding_dim) after attention + feed-forward.
        """
        seq_len = x.shape[1]

        # Ensure causal mask for autoregressive models
        if attn_mask is None:
            attn_mask = torch.triu(torch.ones(seq_len, seq_len, device=x.device), diagonal=1).bool()

        # -----------------------
        # 1) Multi-Head Attention (Pre-Norm)
        # -----------------------
        x_norm = self.norm1(x)
        attn_output, _ = self.attention(
            x_norm,  # query
            x_norm,  # key
            x_norm,  # value
            key_padding_mask=key_padding_mask,  # shape (batch_size, seq_len)
            attn_mask=attn_mask  # shape (seq_len, seq_len)
        )

        # Apply dropout before residual connection
        x = x + self.dropout_layer(attn_output)

        # ----------------------
        # 2) Feed-Forward Layer (Pre-Norm)
        # ----------------------
        x_norm = self.norm2(x)
        ff_output = self.feed_forward(x_norm)

        # Apply dropout before residual connection
        x = x + self.dropout_layer(ff_output)

        return x
