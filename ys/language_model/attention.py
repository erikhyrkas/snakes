import torch
import torch.nn as nn
import torch.nn.functional as F
from ys.language_model.config import Config

# Combining catted_attention_blocks, attention_block, and attention, and then optimizing with einsum.
# there have been a few other optimizations and improvements since the original combining, in the
# interest of speed, but also in an attempt to improve the quality of the results.
class Attention(nn.Module):
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
        self.glu_projection = nn.ModuleList([
            nn.Linear(self.state_dim, 2 * self.state_dim) for _ in range(self.num_layers)
        ])
        self.embedding_to_state = nn.Linear(self.embedding_dim, self.state_dim * self.num_layers)

        # Feed-forward layer, separate per layer
        self.feed_forward_layers = nn.ModuleList([
            nn.Sequential(
                nn.LayerNorm(self.state_dim),
                nn.Linear(self.state_dim, self.state_dim),
                nn.GELU(),
                nn.Linear(self.state_dim, self.embedding_dim),  # Output back to embedding_dim
            ) for _ in range(self.num_layers)
        ])

        # Attention-based aggregation layer
        self.layer_attention_weights = nn.Linear(self.embedding_dim, 1)  # One score per layer per token

        # Separate LayerNorm for embedding and state
        self.layer_norm_embedding = nn.LayerNorm(self.embedding_dim)
        self.layer_norm_state = nn.LayerNorm(self.state_dim)
        self.layer_norm_glu = nn.LayerNorm(self.state_dim)  # Optional for GLU inputs

        self.dropout_start = nn.Dropout(config.dropout_rate)

        # Initialize weights with custom initialization for GLU
        self._initialize_weights()

    def _initialize_weights(self):
        nn.init.xavier_uniform_(self.state_control)
        nn.init.xavier_uniform_(self.input_influence)
        nn.init.xavier_uniform_(self.output_shaper)
        for glu_layer in self.glu_projection:
            nn.init.kaiming_uniform_(glu_layer.weight, nonlinearity='linear')

    def forward(self, embedded_input):
        batch_size, sequence_len, embedding_dim = embedded_input.size()
        device = embedded_input.device

        # Apply dropout to input
        embedded_input = self.dropout_start(embedded_input)

        # Project embeddings to state dimensions, reshaped for all layers
        state_tokens = self.embedding_to_state(embedded_input)
        state_tokens = state_tokens.view(batch_size, sequence_len, self.num_layers, self.state_dim)

        # Initialize the cached state for each layer
        last_state = torch.zeros(batch_size, self.num_layers, self.state_dim, device=device)
        next_states = torch.zeros(batch_size, sequence_len + 1, self.num_layers, self.state_dim, device=device)

        # Recurrent update loop, using last_state to cache previous results
        for t in range(sequence_len):
            # Calculate the control and influence components based on the last state and current input
            next_state_control = torch.einsum('bld,lds->bld', last_state, self.state_control)
            next_state_influence = torch.einsum('bld,lds->bld', state_tokens[:, t], self.input_influence)
            next_state = next_state_control + next_state_influence

            # Temporary variable to store GLU results for each layer
            glu_outputs = []
            for layer in range(self.num_layers):
                normalized_input = self.layer_norm_glu(next_state[:, layer, :])
                glu_result = F.glu(self.glu_projection[layer](normalized_input), dim=-1)
                glu_outputs.append(glu_result)

            # Stack the results and reshape back to (batch_size, num_layers, state_dim)
            next_state = torch.stack(glu_outputs, dim=1)

            # Apply layer normalization
            next_state = self.layer_norm_state(next_state.view(-1, self.state_dim)).view(batch_size, self.num_layers, self.state_dim)

            # Update cached state and store current state
            last_state = next_state
            next_states[:, t + 1] = next_state

        # Compute outputs for each layer without flattening the layer dimension
        attention_output = torch.einsum('btld,lds->btld', next_states[:, 1:], self.output_shaper)

        # Apply feed-forward layer separately for each layer's output
        # (batch_size, sequence_len, num_layers, state_dim) -> (batch_size, num_layers, sequence_len, embedding_dim)
        layer_outputs = torch.stack([ff(attention_output[:, :, i, :]) for i, ff in enumerate(self.feed_forward_layers)], dim=1)

        # Calculate attention scores for each layer
        attention_scores = F.softmax(self.layer_attention_weights(layer_outputs).squeeze(-1), dim=1)

        # Apply attention scores to layer outputs and sum
        weighted_layer_outputs = (layer_outputs * attention_scores.unsqueeze(-1)).sum(dim=1)

        # Normalize final output
        reshaped_attention = self.layer_norm_embedding(weighted_layer_outputs)

        return reshaped_attention # Shape: batch_size, sequence_len, embedding_dim

    def orthogonality_penalty(self, lambda_orthogonality = 0.001):
        """Encourage diversity in the heads by penalizing similar weight matrices."""
        penalty = 0
        if self.num_layers < 2:
            return penalty
        for i in range(self.num_layers):
            for j in range(i + 1, self.num_layers):
                # State control orthogonality penalty
                # penalty += torch.sum((self.state_control[i] @ self.state_control[j].T).pow(2))
                # Input influence orthogonality penalty
                penalty += torch.sum((self.input_influence[i] @ self.input_influence[j].T).pow(2))
                # # Output shaper orthogonality penalty
                # penalty += torch.sum((self.output_shaper[i] @ self.output_shaper[j].T).pow(2))
        # Normalize penalty based on the number of layers
        penalty /= (self.num_layers * (self.num_layers - 1)) / 2
        return penalty * lambda_orthogonality
