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

        self.local_summary_state_control = nn.Parameter(
            torch.zeros(self.state_dim, self.state_dim))
        self.local_summary_state_influence = nn.Parameter(
            torch.zeros(self.state_dim, self.state_dim))
        self.local_summary_output_shaper = nn.Parameter(
            torch.zeros(self.state_dim, self.state_dim))

        self.global_summary_state_control = nn.Parameter(
            torch.zeros(self.state_dim, self.state_dim))
        self.global_summary_state_influence = nn.Parameter(
            torch.zeros(self.state_dim, self.state_dim))
        self.global_summary_output_shaper = nn.Parameter(
            torch.zeros(self.state_dim, self.state_dim))

        # Layer normalization to prevent exploding/vanishing gradients
        self.layer_norm = nn.LayerNorm(self.state_dim)

        self.embedding_to_state = nn.Linear(self.embedding_size, self.state_dim)
        self.state_to_output = nn.Linear(self.state_dim, self.output_dim)

        torch.nn.init.xavier_uniform_(self.global_state_control)
        torch.nn.init.xavier_uniform_(self.global_output_shaper)
        torch.nn.init.xavier_uniform_(self.global_input_influence)

        torch.nn.init.xavier_uniform_(self.global_summary_state_control)
        torch.nn.init.xavier_uniform_(self.global_summary_output_shaper)
        torch.nn.init.xavier_uniform_(self.global_summary_state_influence)

        torch.nn.init.xavier_uniform_(self.local_summary_state_control)
        torch.nn.init.xavier_uniform_(self.local_summary_output_shaper)
        torch.nn.init.xavier_uniform_(self.local_summary_state_influence)

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
        global_summary_state = torch.zeros(batch_size, self.state_dim, device=device)
        global_frequency_trigger = (self.config.global_summary_frequency - 1)
        local_summary_state = torch.zeros(batch_size, self.state_dim, device=device)
        local_frequency_trigger = (self.config.local_summary_frequency - 1)
        for time_step in range(sequence_len):
            next_token_batch = embedded_tokens[:, time_step, :]  # [batch, embedding_dim]
            next_token_in_state_space = self.embedding_to_state(next_token_batch)  # [batch, state_dim]

            global_state = (global_state @ self.global_state_control) + (
                    next_token_in_state_space @ self.global_input_influence) + global_summary_state + local_summary_state
            global_state = self.layer_norm(global_state)
            global_time_step_output = (global_state @ self.global_output_shaper)

            global_time_step_output_in_embedding_space = self.state_to_output(
                global_time_step_output)  # [batch, embedding_dim]
            global_output.append(global_time_step_output_in_embedding_space)

            if time_step % self.config.global_summary_frequency == global_frequency_trigger:
                global_summary_state = (global_summary_state @ self.global_summary_state_control) + (
                        global_time_step_output @ self.global_summary_state_influence)
                global_summary_state = self.layer_norm(global_summary_state)
                global_summary_state = (global_summary_state @ self.global_summary_output_shaper)

            if time_step % self.config.local_summary_frequency == local_frequency_trigger:
                local_summary_state = (local_summary_state @ self.local_summary_state_control) + (
                        global_time_step_output @ self.local_summary_state_influence)
                local_summary_state = self.layer_norm(local_summary_state)
                local_summary_state = (local_summary_state @ self.local_summary_output_shaper)

        stacked_global_output = torch.stack(global_output, dim=1)

        output = self.dropout_end(stacked_global_output)

        return output  # Output shape: [batch_size, sequence_len, embedding_size]
