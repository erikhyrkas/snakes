import torch
from torch import nn
from torch.nn import functional as F

from ys.language_model.config import Config


class Attention(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.embedding_size = config.embedding_dim
        self.state_dim = config.state_dim
        self.output_dim = config.embedding_dim

        # State-space model parameters (learnable)
        self.global_state_control = nn.Parameter(
            torch.zeros(self.state_dim, self.state_dim))  # A: State transition matrix
        self.global_input_influence = nn.Parameter(
            torch.zeros(self.state_dim, self.state_dim))  # B: Input matrix
        self.global_output_shaper = nn.Parameter(
            torch.zeros(self.state_dim, self.state_dim))  # C: Output shaping matrix

        self.glu_projection = nn.Linear(self.state_dim, 2 * self.state_dim)

        # Layer normalization to prevent exploding/vanishing gradients
        self.layer_norm = nn.LayerNorm(self.state_dim)

        self.embedding_to_state = nn.Linear(self.embedding_size, self.state_dim)
        self.state_to_output = nn.Linear(self.state_dim, self.output_dim)

        # Initialize parameters using context manager
        with torch.no_grad():
            nn.init.uniform_(self.global_state_control, a=0.01, b=0.05)
            nn.init.uniform_(self.global_input_influence, a=0.01, b=0.05)
            nn.init.xavier_uniform_(self.global_input_influence)
            nn.init.xavier_uniform_(self.embedding_to_state.weight)
            nn.init.xavier_uniform_(self.state_to_output.weight)
            if self.embedding_to_state.bias is not None:
                nn.init.zeros_(self.embedding_to_state.bias)
            if self.state_to_output.bias is not None:
                nn.init.zeros_(self.state_to_output.bias)

        self.dropout_start = nn.Dropout(config.dropout_rate)
        self.dropout_end = nn.Dropout(config.dropout_rate)

    def forward(self, embedded_tokens):
        batch_size, sequence_len, embedding_size = embedded_tokens.size()
        device = embedded_tokens.device

        embedded_tokens = self.dropout_start(embedded_tokens)

        # Convert to state space
        state_tokens = self.embedding_to_state(embedded_tokens)  # [batch, seq, state_dim]

        # Initialize states
        next_states = torch.zeros(batch_size, sequence_len + 1, self.state_dim, device=device)

        # Compute all states at once
        for t in range(sequence_len):
            # Create the next state
            next_state = (next_states[:, t] @ self.global_state_control +
                          state_tokens[:, t] @ self.global_input_influence)

            next_state = self.glu_projection(next_state)  # [batch, 2 * state_dim]
            # Apply GLU, which will reduce it back to [batch, state_dim]
            next_state = F.glu(next_state, dim=-1)

            next_states[:, t + 1] = self.layer_norm(next_state)

        # Compute outputs
        global_outputs = next_states[:, 1:] @ self.global_output_shaper
        output = self.state_to_output(global_outputs)

        return self.dropout_end(output)