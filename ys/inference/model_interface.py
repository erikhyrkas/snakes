import torch

from ys.language_model.language_model import LanguageModel
from ys.tokenizer.tokenizer import Tokenizer
import torch.nn.functional as F


class ModelInterface:
    def __init__(self, model_save_path="model.bin", tokenizer_save_path="tokenizer.pkl",
                 config_save_path="model_config.json"):
        self.tokenizer = Tokenizer()
        self.tokenizer.load(tokenizer_save_path)
        self.end_token = self.tokenizer.get_end_token()
        self.model = LanguageModel.load(model_save_path, config_save_path)
        if self.model.config.vocab_size != self.tokenizer.vocab_size():
            raise ValueError(
                f"Model trained with a vocab of {self.model.config.vocab_size}, but the current tokenizer has a vocab of {self.tokenizer.vocab_size()}.")
        self.model.eval()
        self.device_name = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using {self.device_name}")
        self.device = torch.device(self.device_name)
        self.model.to(self.device)

    def count_parameters(self):
        total_params = sum(p.numel() for p in self.model.parameters())
        return total_params

    def vocab_size(self):
        return self.tokenizer.vocab_size()

    def _next_logits(self, input_tokens):
        with torch.no_grad():
            if input_tokens.dim() == 1:
                input_tokens = input_tokens.unsqueeze(0)
            logits = self.model(input_tokens)
            return logits

    def _predict_next_token(self, input_tokens):
        logits = self._next_logits(input_tokens)
        next_token_id = torch.argmax(logits[:, -1, :], dim=-1).squeeze()
        return next_token_id.item()


    def _predict_next_token_logits(self, input_tokens, top_p=0.9):
        logits = self._next_logits(input_tokens)
        logits = logits[:, -1, :].view(-1)  # Ensure 1D tensor

        # Apply Top-P filtering directly on logits
        sorted_logits, sorted_indices = torch.sort(logits, descending=True)
        sorted_probs = F.softmax(sorted_logits, dim=-1)
        cumulative_probs = torch.cumsum(sorted_probs, dim=-1)

        # Find cutoff and clamp
        cutoff_index = torch.searchsorted(cumulative_probs, top_p).item()
        cutoff_index = min(cutoff_index, sorted_probs.size(0) - 1)

        # Sample from filtered logits using Gumbel noise
        top_p_logits = sorted_logits[:cutoff_index + 1]
        top_p_indices = sorted_indices[:cutoff_index + 1]
        next_token_id = torch.multinomial(F.softmax(top_p_logits, dim=-1), 1)

        return top_p_indices[next_token_id].item()

    def _predict_next_token_softmax(self, input_tokens, top_p=0.9):
        logits = self._next_logits(input_tokens)
        probs = torch.softmax(logits[:, -1, :], dim=-1).view(-1)

        # Sort probabilities in descending order
        sorted_probs, sorted_indices = torch.sort(probs, descending=True)
        cumulative_probs = torch.cumsum(sorted_probs, dim=-1)
        cumulative_probs = torch.clamp(cumulative_probs, max=1.0)  # Floating-point safety

        # Find cutoff index and clamp to avoid out-of-bounds errors
        cutoff_index = torch.searchsorted(cumulative_probs, top_p).item()
        cutoff_index = min(cutoff_index, sorted_probs.size(0) - 1)

        # Select only the tokens within the top-p probability mass
        top_p_probs = sorted_probs[:cutoff_index + 1]
        top_p_indices = sorted_indices[:cutoff_index + 1]

        # Sample from the filtered set
        next_token_id = torch.multinomial(top_p_probs, 1)

        return top_p_indices[next_token_id].item()

    def complete(self, current_context: str, top_p: float = 0.9, max_tokens: int = 100000) -> str:
        tokens = self.tokenizer.encode(current_context)
        original_length = len(tokens)
        for i in range(max_tokens):
            input_tokens = torch.tensor(tokens, device=self.device)
            if 0.0 < top_p < 1.0:
                next_token = self._predict_next_token_logits(input_tokens, top_p)
            else:
                next_token = self._predict_next_token(input_tokens)
            tokens.append(next_token)
            if next_token == self.end_token:
                break
        new_tokens = tokens[original_length:]
        result = self.tokenizer.decode(new_tokens)
        return result

    def instruct(self, prompt: str, top_p: float = 0.9, max_tokens: int = 100000) -> str:
        new_prompt = prompt
        if '<start>' not in prompt:
            new_prompt = prompt + '\n<start>'

        result = self.complete(new_prompt, top_p, max_tokens)
        return result.replace('<end>', '').strip()
