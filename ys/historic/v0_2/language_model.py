import torch
import torch.nn as nn

from ys.historic.v0_2.attention import Attention
from ys.historic.v0_2.config import Config


class LanguageModel(nn.Module):
    def __init__(self, config: Config):
        super(LanguageModel, self).__init__()
        self.embedding = nn.Embedding(num_embeddings=config.vocab_size, embedding_dim=config.embedding_dim)
        self.dropout = nn.Dropout(config.dropout)
        self.attention = Attention(config)

        self.layer_norm = nn.LayerNorm(config.output_dim)
        self.output_layer = nn.Linear(config.output_dim, config.vocab_size)

    def forward(self, input_tokens):
        embedded = self.embedding(input_tokens)  # Shape: (batch_size, seq_len, embedding_dim)
        embedded = self.dropout(embedded)
        context_representation = self.attention(embedded)  # Shape: (batch_size, seq_len, output_dim)
        context_representation = self.layer_norm(context_representation)
        output = self.output_layer(context_representation)  # Shape: (batch_size, seq_len, vocab_size)
        return output

    def count_parameters(self):
        return sum(p.numel() for p in self.parameters() if p.requires_grad)
