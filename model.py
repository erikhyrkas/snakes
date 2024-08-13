import torch
import torch.nn as nn

from state_space_model import StateSpaceModel
from tokenizer import SimpleTokenizer


class LanguageModel(nn.Module):
    def __init__(self, vocab_size, mode='quadratic', embedding_dim=256, state_dim=256, output_dim=256):
        super(LanguageModel, self).__init__()
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim)
        self.state_space_model = StateSpaceModel(state_dim=state_dim, input_dim=embedding_dim, output_dim=output_dim,
                                                 mode=mode)
        self.layer_norm = nn.LayerNorm(output_dim)
        self.output_layer = nn.Linear(output_dim, vocab_size)

    def forward(self, input_tokens):
        embedded = self.embedding(input_tokens)
        if len(embedded.shape) == 2:
            embedded = embedded.unsqueeze(0)
        context_representation = self.state_space_model(embedded)
        context_representation = self.layer_norm(context_representation)
        output = self.output_layer(context_representation)
        return output

    def predict_next_token(self, input_tokens, tokenizer):
        output = self.forward(input_tokens)
        next_token_id = torch.argmax(output[:, -1, :], dim=-1).squeeze()
        return tokenizer.detokenize([next_token_id.item()])


class Completer:
    def __init__(self, mode='quadratic', model_save_path="model.bin", tokenizer_save_path="tokenizer.pkl"):
        self.tokenizer = SimpleTokenizer()
        self.tokenizer.load(tokenizer_save_path)
        self.model = LanguageModel(vocab_size=self.tokenizer.vocab_size(), mode=mode)
        self.model.load_state_dict(torch.load(model_save_path, weights_only=True))
        self.model.eval()
        self.device_name = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using {self.device_name}")
        self.device = torch.device(self.device_name)
        self.model.to(self.device)

    def complete(self, current_context: str, max_tokens: int = 100):
        result = current_context
        for i in range(max_tokens):
            input_tokens = torch.tensor([self.tokenizer.tokenize(result)]).to(self.device)
            next_token = self.model.predict_next_token(input_tokens, self.tokenizer)
            result += next_token
        return result
