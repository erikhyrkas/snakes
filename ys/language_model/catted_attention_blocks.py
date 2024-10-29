import torch
from torch import nn

from ys.language_model.attention_block import AttentionBlock
from ys.language_model.config import Config


# This isn't exactly multi-head attention, but it runs multiple attentions,
# concats their outputs, and them projects their outputs back to the correct shape.
# True multi-head attention is more efficient because it would calculate the heads concurrently,
# where this does much of the work in sequence. However, this is easy to experiment with for the
# time being.
class CattedAttentionBlocks(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.attention_layers = nn.ModuleList([AttentionBlock(config) for _ in range(config.num_layers)])
        self.embedding_dim = config.embedding_dim
        self.attention_shaper = nn.Linear(self.embedding_dim * config.num_layers, self.embedding_dim)
        self.dropout = nn.Dropout(config.dropout_rate)
        self.layer_norm = nn.LayerNorm(self.embedding_dim)

    def forward(self, embedded_input):
        # embedded_input shape: [batch_size, sequence_len, embedding_dim]
        outputs = []
        for attention in self.attention_layers:
            next_output = attention(embedded_input)  # Each output has shape [batch_size, sequence_len, embedding_dim]
            outputs.append(next_output)

        # Concatenate along the feature dimension (dim=2)
        concatenated_attention = torch.cat(outputs,
                                           dim=2)  # shape: [batch_size, sequence_len, embedding_dim * num_layers]

        # Project concatenated output back to original embedding size
        reshaped_attention = self.attention_shaper(
            concatenated_attention)  # shape: [batch_size, sequence_len, embedding_dim]

        # Apply dropout and layer normalization
        reshaped_attention = self.layer_norm(reshaped_attention + embedded_input)  # Residual connection and normalize

        return reshaped_attention
