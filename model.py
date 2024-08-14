import torch
import torch.nn as nn

from state_space_model import StateSpaceModel
from tokenizer import SimpleTokenizer


class LanguageModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim=256, state_dim=256, output_dim=256):
        super(LanguageModel, self).__init__()
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim)
        self.state_space_model = StateSpaceModel(state_dim=state_dim, input_dim=embedding_dim, output_dim=output_dim)
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

    def predict_next_token(self, input_tokens):
        output = self.forward(input_tokens)
        next_token_id = torch.argmax(output[:, -1, :], dim=-1).squeeze()
        return next_token_id.item()

    def predict_next_token_softmax(self, input_tokens, top_p=0.9):
        output = self.forward(input_tokens)

        logits = output[:, -1, :].squeeze()
        probs = torch.softmax(logits, dim=-1)
        sorted_probs, sorted_indices = torch.sort(probs, descending=True)
        cumulative_probs = torch.cumsum(sorted_probs, dim=-1)
        cutoff_index = torch.searchsorted(cumulative_probs, top_p)
        top_p_probs = sorted_probs[:cutoff_index + 1]
        top_p_indices = sorted_indices[:cutoff_index + 1]
        next_token_id = torch.multinomial(top_p_probs, 1)

        return top_p_indices[next_token_id].item()


class ModelInterface:
    def __init__(self, model_save_path="model.bin", tokenizer_save_path="tokenizer.pkl"):
        self.tokenizer = SimpleTokenizer()
        self.tokenizer.load(tokenizer_save_path)
        self.end_token = self.tokenizer.get_end_token()
        self.model = LanguageModel(vocab_size=self.tokenizer.vocab_size())
        self.model.load_state_dict(torch.load(model_save_path, weights_only=True))
        self.model.eval()
        self.device_name = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using {self.device_name}")
        self.device = torch.device(self.device_name)
        self.model.to(self.device)

    def complete(self, current_context: str, top_p: float = 0.9, max_tokens: int = 100000):
        tokens = self.tokenizer.tokenize(current_context)
        for i in range(max_tokens):
            input_tokens = torch.tensor(tokens).to(self.device)
            if top_p >= 1.0 or top_p <= 0.0:
                next_token = self.model.predict_next_token(input_tokens)
            else:
                next_token = self.model.predict_next_token_softmax(input_tokens, top_p)
            tokens.append(next_token)
            if next_token == self.end_token:
                break
        result = self.tokenizer.detokenize(tokens)
        return result

    def prompt(self, prompt: str, top_p: float = 0.9, max_tokens: int = 100000):
        new_prompt = prompt
        if '<start>' not in prompt:
            new_prompt = prompt + '<start>'

        result = self.complete(new_prompt, top_p, max_tokens)
        return result.replace('<end>', '').strip()
