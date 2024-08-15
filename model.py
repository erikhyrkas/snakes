import torch
import torch.nn as nn

from attention import Attention


class LanguageModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim=368, state_dim=368, output_dim=368):
        super(LanguageModel, self).__init__()
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim)
        self.state_space_model = Attention(state_dim=state_dim, input_dim=embedding_dim, output_dim=output_dim)
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
