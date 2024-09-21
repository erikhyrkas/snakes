import torch
from torch import nn

from ys.language_model.config import Config


class Attention(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.embedding_size = config.embedding_dim
        self.state_dim = config.state_dim

        # # State-space model parameters (learnable)
        self.local_state_control = nn.Parameter(
            0.1 * torch.randn(self.state_dim, self.state_dim) + 0.01)  # A: State transition matrix
        self.local_input_influence = nn.Parameter(
            0.1 * torch.randn(self.embedding_size, self.state_dim) + 0.01)  # B: Input matrix
        self.local_blend_shaper = nn.Parameter(0.1 * torch.randn(self.state_dim,
                                                                 self.state_dim) + 0.01)  # sort of C: tweaked Output shaping matrix

        self.global_summary_state_control = nn.Parameter(
            0.1 * torch.randn(self.state_dim, self.state_dim) + 0.01)
        self.global_summary_state_influence = nn.Parameter(
            0.1 * torch.randn(self.embedding_size, self.state_dim) + 0.01)
        self.global_summary_output_shaper = nn.Parameter(
            0.1 * torch.randn(self.state_dim, self.state_dim) + 0.01)

        self.global_state_control = nn.Parameter(
            0.1 * torch.randn(self.state_dim, self.state_dim) + 0.01)  # A: State transition matrix
        self.global_input_influence = nn.Parameter(
            0.1 * torch.randn(self.embedding_size, self.state_dim) + 0.01)  # B: Input matrix
        self.global_output_shaper = nn.Parameter(
            0.1 * torch.randn(self.state_dim, self.embedding_size) + 0.01)  # C: Output shaping matrix

        # Layer normalization to prevent exploding/vanishing gradients
        self.layer_norm = nn.LayerNorm(self.state_dim)

        # Linear layer to reshape cumulative context to match input shape
        self.linear_output = nn.Linear(self.embedding_size, self.embedding_size)
        self.dropout_start = nn.Dropout(config.dropout_rate)
        self.dropout_end = nn.Dropout(config.dropout_rate)

    def forward(self, embedded_tokens):
        device = embedded_tokens.device
        batch_size, sequence_len, embedding_size = embedded_tokens.size()
        embedded_tokens = self.dropout_start(embedded_tokens)

        # My intuition here is that if we iterate tokens forward in standard state-space model fashion,
        # we'll prefer recent tokens, while having less of an impact on more distant tokens.
        #
        # I figure that by having a local state, that represents information about the recent tokens -- though
        # still arranged to prefer the most distant local state, I am freeing up the global state to remember
        # more details about the overall conversation. I feel like the local tokens heavily influence the next
        # token, but we still need to know about the overall conversation. My hope is that the local state
        # will keep the output text coherent, while the global state makes it sensible and logical.
        #
        # I figure that by adding a global summary that is updated less frequently, I may lose fewer relevant
        # conversation details. My intuition is that the global state prefers information near the end of the
        # conversation at the point it is calculated, by adding it to the summary infrequently, I'm going to
        # retain more details that mattered to each summary span.
        #
        # All of my intuition relies on the idea that by creating opportunities for the model to learn in
        # specific areas, I'm freeing up the other aspects to learn about their own areas.
        global_output = []
        global_state = torch.zeros(batch_size, self.state_dim, device=device)
        global_summary_state = torch.zeros(batch_size, self.state_dim, device=device)
        for time_step in range(sequence_len):
            local_beginning = max(0, time_step - self.config.local_size)
            local_length = time_step - local_beginning
            local_state = torch.zeros(batch_size, self.state_dim, device=device)
            if local_length > 0:
                local_end = local_beginning + local_length
                local_tokens = embedded_tokens[:, local_beginning:local_end, :]
                # reverse iterate to avoid the decay of information for "distant" tokens -- the global state already has a bias toward the "near" tokens
                for local_time_step in range(local_length - 1, -1, -1):
                    local_token = local_tokens[:, local_time_step, :]
                    local_state = (local_state @ self.local_state_control) + (local_token @ self.local_input_influence)
                    local_state = self.layer_norm(local_state)
            blended_local_influence = (local_state @ self.local_blend_shaper)

            next_token = embedded_tokens[:, time_step, :]
            global_state = (global_state @ self.global_state_control) + (
                        next_token @ self.global_input_influence) + blended_local_influence + global_summary_state
            global_state = self.layer_norm(global_state)
            global_time_step_output = (global_state @ self.global_output_shaper)
            global_output.append(global_time_step_output)
            if time_step % self.config.summary_frequency == (self.config.summary_frequency - 1):
                global_summary_state = (global_summary_state @ self.global_summary_state_control) + (
                            global_time_step_output @ self.global_summary_state_influence)
                global_summary_state = self.layer_norm(global_summary_state)
                global_summary_state = (global_summary_state @ self.global_summary_output_shaper)

        stacked_global_output = torch.stack(global_output, dim=1)

        # Pass through linear layer and apply dropout
        output = self.linear_output(stacked_global_output)
        output = self.dropout_end(output)

        return output  # Output shape: [batch_size, sequence_len, embedding_size]
