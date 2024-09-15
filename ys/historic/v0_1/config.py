
class Config:
    def __init__(self, vocab_size, embedding_dim=768, state_dim=1024, output_dim=768, block_size=64,
                 dropout=0.1):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.state_dim = state_dim
        self.output_dim = output_dim
        self.block_size = block_size
        self.dropout = dropout
        self._validate_shapes()

    def _validate_shapes(self):
        assert self.vocab_size > 0, "Vocabulary size must be positive"
        assert self.embedding_dim > 0, "Embedding dimension must be positive"
        assert self.state_dim > 0, "State dimension must be positive"
        assert self.output_dim > 0, "Output dimension must be positive"
        assert self.block_size > 0, "Block size must be positive"
        assert 0 <= self.dropout < 1, "Dropout must be between 0 and 1"

    def to_dict(self):
        return {
            "vocab_size": self.vocab_size,
            "embedding_dim": self.embedding_dim,
            "state_dim": self.state_dim,
            "output_dim": self.output_dim,
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
