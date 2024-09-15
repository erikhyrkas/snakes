import torch
import torch.nn as nn

from ys.language_model.attention import Attention
from ys.language_model.config import Config


class LanguageModel(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.embedding = nn.Embedding(config.vocab_size, config.embedding_dim)
        self.ssm = Attention(config)
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
