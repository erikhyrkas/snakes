import torch
import torch.nn as nn

from attention.v0_2.ssd_attention import SSDAttention


# Embedding: 960
# State: 16,384
# Output: 768
# block length: 32
# heads: 8
# Vocab: 56,668
# Parameters: 98,980,708
# Trained on an A100 (80 gb of memory)
# warm up training for stability
# learning rate: 0.00005
# sequence length: 32
# batch size: 128
# patience: 3
# final
# learning rate: 0.00005
# sequence length: 512
# batch size: 8
# patience: 3
class LanguageModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim=960, state_dim=16384, output_dim=768,
                 block_length=32, number_of_heads=8, dropout=0.1):
        super(LanguageModel, self).__init__()
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim)
        self.dropout = nn.Dropout(dropout)
        self.attention = SSDAttention(input_dim=embedding_dim, state_dim=state_dim,
                                      output_dim=output_dim, block_length=block_length,
                                      number_of_heads=number_of_heads)

        self.layer_norm = nn.LayerNorm(output_dim)
        self.output_layer = nn.Linear(output_dim, vocab_size)

    def forward(self, input_tokens):
        embedded = self.embedding(input_tokens)  # Shape: (batch_size, seq_len, embedding_dim)
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
