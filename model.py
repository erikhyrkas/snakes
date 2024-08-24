import torch
import torch.nn as nn

from attention.ssd_attention import StateSpaceModelAttentionWithSSD
from rope import RoPE


class LanguageModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim=768, state_dim=8192, output_dim=768, dropout=0.1):
        super(LanguageModel, self).__init__()
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim)
        self.rope = RoPE(embedding_dim)
        self.dropout = nn.Dropout(dropout)
        self.attention = StateSpaceModelAttentionWithSSD(state_dim=state_dim, input_dim=embedding_dim,
                                                         output_dim=output_dim)
        self.layer_norm = nn.LayerNorm(output_dim)
        self.output_layer = nn.Linear(output_dim, vocab_size)

    def forward(self, input_tokens):
        embedded = self.embedding(input_tokens)  # Shape: (batch_size, seq_len, embedding_dim)
        embedded = self.rope(embedded)  # Apply RoPE
        embedded = self.dropout(embedded)
        context_representation = self.attention(embedded)  # Shape: (batch_size, seq_len, output_dim)
        context_representation = self.layer_norm(context_representation)
        output = self.output_layer(context_representation)  # Shape: (batch_size, seq_len, vocab_size)
        return output

    def predict_next_token(self, input_tokens):
        with torch.no_grad():  # Disable gradient calculation
            # add a batch dimension if missing
            if input_tokens.dim() == 1:
                input_tokens = input_tokens.unsqueeze(0)
            output = self.forward(input_tokens)
            next_token_id = torch.argmax(output[:, -1, :], dim=-1).squeeze()
            return next_token_id.item()

    def predict_next_token_softmax(self, input_tokens, top_p=0.9):
        with torch.no_grad():  # Disable gradient calculation
            # add a batch dimension if missing
            if input_tokens.dim() == 1:
                input_tokens = input_tokens.unsqueeze(0)
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

    def count_parameters(self):
        return sum(p.numel() for p in self.parameters() if p.requires_grad)
