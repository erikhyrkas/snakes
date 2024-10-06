import torch
from torch import nn

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

        # Layer normalization to prevent exploding/vanishing gradients
        self.layer_norm = nn.LayerNorm(self.state_dim)

        self.embedding_to_state = nn.Linear(self.embedding_size, self.state_dim)
        self.state_to_output = nn.Linear(self.state_dim, self.output_dim)

        torch.nn.init.xavier_uniform_(self.global_state_control)
        torch.nn.init.xavier_uniform_(self.global_output_shaper)
        torch.nn.init.xavier_uniform_(self.global_input_influence)

        torch.nn.init.xavier_uniform_(self.embedding_to_state.weight)
        torch.nn.init.xavier_uniform_(self.state_to_output.weight)

        self.dropout_start = nn.Dropout(config.dropout_rate)
        self.dropout_end = nn.Dropout(config.dropout_rate)

    def forward(self, embedded_tokens):
        device = embedded_tokens.device
        batch_size, sequence_len, embedding_size = embedded_tokens.size()
        embedded_tokens = self.dropout_start(embedded_tokens)

        global_output = []
        global_state = torch.zeros(batch_size, self.state_dim, device=device)
        for time_step in range(sequence_len):
            next_token_batch = embedded_tokens[:, time_step, :]  # [batch, embedding_dim]
            next_token_in_state_space = self.embedding_to_state(next_token_batch)  # [batch, state_dim]

            global_state = (global_state @ self.global_state_control) + (
                    next_token_in_state_space @ self.global_input_influence)
            global_state = self.layer_norm(global_state)
            global_time_step_output = (global_state @ self.global_output_shaper)

            global_time_step_output_in_embedding_space = self.state_to_output(
                global_time_step_output)  # [batch, embedding_dim]
            global_output.append(global_time_step_output_in_embedding_space)

        stacked_global_output = torch.stack(global_output, dim=1)

        output = self.dropout_end(stacked_global_output)

        return output  # Output shape: [batch_size, sequence_len, embedding_size]
