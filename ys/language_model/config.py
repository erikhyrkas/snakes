class Config:
    def __init__(self, vocab_size, embedding_dim=768, state_dim=4048, local_summary_frequency=16,
                 global_summary_frequency=64, num_layers=8, dropout_rate=0.1):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.state_dim = state_dim
        self.local_summary_frequency = local_summary_frequency
        self.global_summary_frequency = global_summary_frequency
        self.num_layers = num_layers
        self.dropout_rate = dropout_rate
        self._validate_shapes()

    def _validate_shapes(self):
        assert self.vocab_size > 0, "Vocabulary size must be positive"
        assert self.embedding_dim > 0, "Embedding dimension must be positive"
        assert self.state_dim > 0, "State dimension must be positive"
        assert 0 <= self.dropout_rate < 1, "Dropout rate must be between 0 and 1"
        assert self.num_layers > 0, "Number of layers must be greater than 0"

    def to_dict(self):
        return {
            "vocab_size": self.vocab_size,
            "embedding_dim": self.embedding_dim,
            "state_dim": self.state_dim,
            "local_summary_frequency": self.local_summary_frequency,
            "global_summary_frequency": self.global_summary_frequency,
            "num_layers": self.num_layers,
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
