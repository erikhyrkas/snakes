class Config:
    def __init__(self, vocab_size, pad_token_id, embedding_dim=8096, state_dim=1024,
                 num_heads=5, num_layers=4, dropout_rate=0.01):
        self.pad_token_id = pad_token_id
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.state_dim = state_dim
        self.num_heads = num_heads
        self.num_layers = num_layers
        self.dropout_rate = dropout_rate
        self._validate_shapes()

    def _validate_shapes(self):
        assert self.vocab_size > 0, "Vocabulary size must be positive"
        assert self.embedding_dim > 0, "Embedding dimension must be positive"
        assert self.state_dim > 0, "State dimension must be positive"
        assert 0 <= self.dropout_rate < 1, "Dropout rate must be between 0 and 1"
        assert self.num_layers > 0, "Number of layers must be greater than 0"
        assert self.num_heads > 0, "Number of heads must be greater than 0"
        assert self.pad_token_id > -1, "Pad token id must be positive"

    def to_dict(self):
        return {
            "vocab_size": self.vocab_size,
            "embedding_dim": self.embedding_dim,
            "state_dim": self.state_dim,
            "num_heads": self.num_heads,
            "num_layers": self.num_layers,
            "pad_token_id": self.pad_token_id,
            "dropout_rate": self.dropout_rate,
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
