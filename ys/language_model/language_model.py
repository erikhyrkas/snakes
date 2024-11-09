import torch
import torch.nn as nn

from ys.language_model.attention import Attention
from ys.language_model.config import Config


class LanguageModel(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.embedding = nn.Embedding(config.vocab_size, config.embedding_dim)
        self.attention = Attention(config)
        self.output_layer = nn.Linear(config.embedding_dim, config.vocab_size)

    def forward(self, input_tokens):
        embedded = self.embedding(input_tokens)
        context_representation = self.attention(embedded)
        output = self.output_layer(context_representation)
        return output

    @classmethod
    def load(cls, model_path, config_path):
        config = Config.load(config_path)
        model = cls(config)
        model.load_state_dict(torch.load(model_path, weights_only=False))
        return model

    def save(self, model_path, config_path):
        self.config.save(config_path)
        torch.save(self.state_dict(), model_path)

    def count_parameters(self):
        return sum(p.numel() for p in self.parameters() if p.requires_grad)
