import torch
import torch.nn as nn

from ys.historic.v0_1.attention import Attention
from ys.historic.v0_1.config import Config


class LanguageModel(nn.Module):
    def __init__(self, config: Config):
        super(LanguageModel, self).__init__()
        self.embedding = nn.Embedding(num_embeddings=config.vocab_size, embedding_dim=config.embedding_dim)
        self.state_space_model = Attention(config)
        self.layer_norm = nn.LayerNorm(config.output_dim)
        self.output_layer = nn.Linear(config.output_dim, config.vocab_size)

    def forward(self, input_tokens):
        embedded = self.embedding(input_tokens)
        if len(embedded.shape) == 2:
            embedded = embedded.unsqueeze(0)
        context_representation = self.state_space_model(embedded)
        context_representation = self.layer_norm(context_representation)
        output = self.output_layer(context_representation)
        return output
