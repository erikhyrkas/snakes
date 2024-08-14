import torch

from model import LanguageModel
from tokenizer import Tokenizer


class ModelInterface:
    def __init__(self, model_save_path="model.bin", tokenizer_save_path="tokenizer.pkl"):
        self.tokenizer = Tokenizer()
        self.tokenizer.load(tokenizer_save_path)
        self.end_token = self.tokenizer.get_end_token()
        self.model = LanguageModel(vocab_size=self.tokenizer.vocab_size())
        self.model.load_state_dict(torch.load(model_save_path), strict=False)
        self.model.eval()
        self.device_name = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using {self.device_name}")
        self.device = torch.device(self.device_name)
        self.model.to(self.device)

    def count_parameters(self):
        total_params = sum(p.numel() for p in self.model.parameters())
        return total_params

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
            new_prompt = prompt + '\n<start>'

        result = self.complete(new_prompt, top_p, max_tokens)
        return result.replace('<end>', '').strip()
