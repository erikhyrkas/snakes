import torch
import torch.nn as nn
import torch.nn.functional as F
from ys.language_model.config import Config

# Combining catted_attention_blocks, attention_block, and attention, and then optimizing with einsum.
# there have been a few other optimizations and improvements since the original combining, in the
# interest of speed, but also in an attempt to improve the quality of the results.
class ParallelAttention(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.num_layers = config.num_layers
        self.embedding_dim = config.embedding_dim
        self.state_dim = config.state_dim

        # Stacked parameters for each layer in the state-space model
        self.state_control = nn.Parameter(torch.zeros(self.num_layers, self.state_dim, self.state_dim))
        self.input_influence = nn.Parameter(torch.zeros(self.num_layers, self.state_dim, self.state_dim))
        self.output_shaper = nn.Parameter(torch.zeros(self.num_layers, self.state_dim, self.state_dim))

        # GLU and linear projections with layer-specific weights stacked
        self.glu_projection = nn.Linear(self.state_dim * self.num_layers, 2 * self.state_dim * self.num_layers)
        self.embedding_to_state = nn.Linear(self.embedding_dim, self.state_dim * self.num_layers)
        self.state_to_output = nn.Linear(self.state_dim * self.num_layers, self.embedding_dim)

        # Feed-forward layer, separate per layer
        self.feed_forward_layers = nn.ModuleList([
            nn.Sequential(
                nn.Linear(self.embedding_dim, self.state_dim),
                nn.GELU(),
                nn.Linear(self.state_dim, self.embedding_dim)
            ) for _ in range(self.num_layers)
        ])

        # Projection layer to reshape concatenated outputs back to embedding size
        self.attention_shaper = nn.Linear(self.state_dim * self.num_layers, self.embedding_dim)

        # Separate LayerNorm for embedding and state
        self.layer_norm_embedding = nn.LayerNorm(self.embedding_dim)
        self.layer_norm_state = nn.LayerNorm(self.state_dim)

        self.dropout_start = nn.Dropout(config.dropout_rate)
        self.dropout_end = nn.Dropout(config.dropout_rate)

        # Initialize weights with custom initialization for GLU
        self._initialize_weights()

    def _initialize_weights(self):
        nn.init.xavier_uniform_(self.state_control)
        nn.init.xavier_uniform_(self.input_influence)
        nn.init.xavier_uniform_(self.output_shaper)
        nn.init.kaiming_uniform_(self.glu_projection.weight, nonlinearity='linear')

    def forward(self, embedded_input):
        batch_size, sequence_len, embedding_dim = embedded_input.size()
        device = embedded_input.device

        # Apply dropout to input
        embedded_input = self.dropout_start(embedded_input)

        # Project embeddings to state dimensions, reshaped for all layers
        state_tokens = self.embedding_to_state(embedded_input)
        state_tokens = state_tokens.view(batch_size, sequence_len, self.num_layers, self.state_dim)

        # Initialize the tensor for next states with zeros
        next_states = torch.zeros(batch_size, sequence_len + 1, self.num_layers, self.state_dim, device=device)

        # Optimized split for control and influence
        next_state_control = torch.einsum('btld,lds->btld', next_states[:, :-1], self.state_control)
        next_state_influence = torch.einsum('btld,lds->btld', state_tokens, self.input_influence)
        next_state = next_state_control + next_state_influence

        # Apply GLU projection in parallel for all layers
        next_state = self.glu_projection(next_state.view(batch_size, sequence_len, -1))
        next_state = F.glu(next_state, dim=-1)
        next_state = next_state.view(batch_size, sequence_len, self.num_layers, self.state_dim)

        # Apply layer normalization for each layer in the state dimension
        next_state = self.layer_norm_state(next_state.view(-1, self.state_dim)).view(
            batch_size, sequence_len, self.num_layers, self.state_dim)

        # Update states tensor
        next_states[:, 1:] = next_state

        # Compute outputs for each layer without flattening the layer dimension
        global_outputs = torch.einsum('btld,lds->btld', next_states[:, 1:], self.output_shaper)

        # Flatten the layer dimension for concatenation and reshaping
        global_outputs = global_outputs.reshape(batch_size, sequence_len, self.num_layers * self.state_dim)

        # Project concatenated output back to original embedding size
        reshaped_attention = self.attention_shaper(global_outputs)

        # Apply per-layer feed-forward layers, normalization, and end dropout
        reshaped_attention = self.layer_norm_embedding(reshaped_attention)
        reshaped_attention = sum([ff(reshaped_attention) for ff in self.feed_forward_layers]) / self.num_layers
        reshaped_attention = self.dropout_end(reshaped_attention)

        return reshaped_attention

    def orthogonality_penalty(self, lambda_orthogonality = 0.01):
        """Encourage diversity in the heads by penalizing similar weight matrices."""
        penalty = 0
        for i in range(self.num_layers):
            for j in range(i + 1, self.num_layers):
                # State control orthogonality penalty
                penalty += torch.sum((self.state_control[i] @ self.state_control[j].T).pow(2))
                # Input influence orthogonality penalty
                penalty += torch.sum((self.input_influence[i] @ self.input_influence[j].T).pow(2))
                # Output shaper orthogonality penalty
                penalty += torch.sum((self.output_shaper[i] @ self.output_shaper[j].T).pow(2))
        # Normalize penalty based on the number of layers
        penalty /= (self.num_layers * (self.num_layers - 1)) / 2
        return penalty * lambda_orthogonality