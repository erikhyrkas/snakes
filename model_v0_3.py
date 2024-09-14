import torch
import torch.nn as nn

from attention.v0_3.v3_attention import SelectiveSSM


class Config:
    def __init__(self, vocab_size, embedding_dim=768, state_dim=1024, output_dim=768, num_heads=4, block_size=64,
                 dropout=0.1):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.state_dim = state_dim
        self.output_dim = output_dim
        self.num_heads = num_heads
        self.block_size = block_size
        self.dropout = dropout
        self._validate_shapes()

    def _validate_shapes(self):
        assert self.vocab_size > 0, "Vocabulary size must be positive"
        assert self.embedding_dim > 0, "Embedding dimension must be positive"
        assert self.state_dim > 0, "State dimension must be positive"
        assert self.output_dim > 0, "Output dimension must be positive"
        assert self.num_heads > 0, "Number of heads must be positive"
        assert self.block_size > 0, "Block size must be positive"
        assert 0 <= self.dropout < 1, "Dropout must be between 0 and 1"
        assert self.state_dim % self.num_heads == 0, "State dimension must be divisible by number of heads"
        assert self.embedding_dim % self.num_heads == 0, "Embedding dimension must be divisible by number of heads"

    def to_dict(self):
        return {
            "vocab_size": self.vocab_size,
            "embedding_dim": self.embedding_dim,
            "state_dim": self.state_dim,
            "output_dim": self.output_dim,
            "num_heads": self.num_heads,
            "block_size": self.block_size,
            "dropout": self.dropout,
        }

    @classmethod
    def from_dict(cls, config_dict):
        return cls(**config_dict)

    def save(self, filepath):
        import json
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @classmethod
    def load(cls, filepath):
        import json
        with open(filepath, 'r') as f:
            config_dict = json.load(f)
        return cls.from_dict(config_dict)


class LanguageModel(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.embedding = nn.Embedding(config.vocab_size, config.embedding_dim)
        self.ssm = SelectiveSSM(config)
        self.output_layer = nn.Linear(config.output_dim, config.vocab_size)

    def forward(self, input_tokens):
        embedded = self.embedding(input_tokens)
        context_representation = self.ssm(embedded)
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

    def predict_next_token(self, input_tokens):
        with torch.no_grad():
            if input_tokens.dim() == 1:
                input_tokens = input_tokens.unsqueeze(0)
            logits = self.forward(input_tokens)
            next_token_id = torch.argmax(logits[:, -1, :], dim=-1).squeeze()
            return next_token_id.item()

    def predict_next_token_softmax(self, input_tokens, top_p=0.9):
        with torch.no_grad():
            if input_tokens.dim() == 1:
                input_tokens = input_tokens.unsqueeze(0)
            logits = self.forward(input_tokens)
            probs = torch.softmax(logits[:, -1, :].squeeze(), dim=-1)
            sorted_probs, sorted_indices = torch.sort(probs, descending=True)
            cumulative_probs = torch.cumsum(sorted_probs, dim=-1)
            cutoff_index = torch.searchsorted(cumulative_probs, top_p)
            top_p_probs = sorted_probs[:cutoff_index + 1]
            top_p_indices = sorted_indices[:cutoff_index + 1]
            next_token_id = torch.multinomial(top_p_probs, 1)
            return top_p_indices[next_token_id].item()
