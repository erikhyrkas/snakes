import torch.nn as nn
import json

from attention.v0_3.v3_attention import AttentionBlock


class Config:
    def __init__(self, vocab_size, embedding_dim=448, state_dim=448,
                 num_heads=1, use_structured_mask=False, use_quadratic=False,
                 use_layer_norm=False, use_residual=False):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.state_dim = state_dim
        self.use_structured_mask = use_structured_mask
        self.num_heads = num_heads
        self.use_quadratic = use_quadratic
        self.use_layer_norm = use_layer_norm
        self.use_residual = use_residual


class LanguageModel(nn.Module):
    def __init__(self, config: Config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = config
        self.embedding = nn.Embedding(self.config.vocab_size, self.config.embedding_dim)
        self.attention_block = AttentionBlock(self.config)
        self.output_layer = nn.Linear(self.config.embedding_dim, self.config.vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        x = self.attention_block(x)
        logits = self.output_layer(x)
        return logits

    def save_config(self, filepath):
        with open(filepath, 'w') as f:
            json.dump(vars(self.config), f)

    @staticmethod
    def load_config(filepath):
        with open(filepath, 'r') as f:
            config_dict = json.load(f)
        return Config(**config_dict)

    def count_parameters(self):
        return sum(p.numel() for p in self.parameters() if p.requires_grad)

