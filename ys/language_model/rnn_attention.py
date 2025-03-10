import torch
import torch.nn as nn
import torch.nn.functional as F
from ys.language_model.config import Config

class MinimalRNNAttention(nn.Module):
    """
    A drop-in replacement for the SSM-based Attention class that uses a MinimalRNN
    for sequence processing. It retains the same feed-forward, multi-head attention
    aggregation, and normalization steps so it can be used with the same config.
    """
    def __init__(self, config: Config):
        super().__init__()
        self.num_heads = config.num_heads
        self.embedding_dim = config.embedding_dim
        self.state_dim = config.state_dim

        # ---- MinimalRNN parameters (per head) ----
        # Input -> hidden-state encoder (maps embedding_dim -> state_dim * num_heads).
        self.embedding_to_z = nn.Linear(self.embedding_dim, self.num_heads * self.state_dim)

        # MinimalRNN core parameters:
        #   U_h, U_z : shape (num_heads, state_dim, state_dim)
        #   b_u      : shape (num_heads, state_dim)
        self.U_h = nn.Parameter(torch.Tensor(self.num_heads, self.state_dim, self.state_dim))
        self.U_z = nn.Parameter(torch.Tensor(self.num_heads, self.state_dim, self.state_dim))
        self.b_u = nn.Parameter(torch.Tensor(self.num_heads, self.state_dim))

        # Output shaper for each head (analogous to 'output_shaper' in the SSM version).
        # Maps the hidden state dimension back into the same dimension for the feed-forward.
        self.output_shaper = nn.Parameter(torch.Tensor(self.num_heads, self.state_dim, self.state_dim))

        # ---- Feed-forward layers & aggregator ----
        self.feed_forward_layers = nn.ModuleList([
            nn.Sequential(
                nn.LayerNorm(self.state_dim),
                nn.Linear(self.state_dim, self.state_dim),
                nn.GELU(),
                nn.Linear(self.state_dim, self.embedding_dim),  # back to embedding_dim
            ) for _ in range(self.num_heads)
        ])

        # Single linear to compute one attention weight per layer per token
        self.layer_attention_weights = nn.Linear(self.embedding_dim, 1)

        # Separate LayerNorms
        self.layer_norm_output = nn.LayerNorm(self.embedding_dim)
        self.layer_norm_state = nn.LayerNorm(self.state_dim)

        # input dropout
        self.dropout_start = nn.Dropout(config.dropout_rate)

        # Initialize all weights
        self._initialize_weights()

    def _initialize_weights(self):
        """Custom initialization for MinimalRNN and other layers."""
        # Orthogonal or Xavier init for the MinimalRNN parameters
        nn.init.xavier_uniform_(self.U_h)
        nn.init.xavier_uniform_(self.U_z)
        nn.init.zeros_(self.b_u)
        nn.init.xavier_uniform_(self.output_shaper)

        # Initialize embedding->z projection
        nn.init.xavier_uniform_(self.embedding_to_z.weight)
        nn.init.zeros_(self.embedding_to_z.bias)

        # Initialize feed-forward layers
        for ff in self.feed_forward_layers:
            # The feed-forward is a Sequential of [LN, Linear, GELU, Linear].
            # We'll just do a Xavier init for the linear layers.
            for module in ff:
                if isinstance(module, nn.Linear):
                    nn.init.xavier_uniform_(module.weight)
                    nn.init.zeros_(module.bias)

        # Initialize attention weight projection
        nn.init.xavier_uniform_(self.layer_attention_weights.weight)
        nn.init.zeros_(self.layer_attention_weights.bias)

    def forward(self, embedded_input):
        """
        Args:
            embedded_input: (batch_size, sequence_len, embedding_dim)
        Returns:
            reshaped_attention: (batch_size, sequence_len, embedding_dim)
        """
        batch_size, sequence_len, _ = embedded_input.size()
        device = embedded_input.device

        # 1) dropout on input
        embedded_input = self.dropout_start(embedded_input)

        # 2) Encode embeddings to z-space for all heads at once => (B, S, H, D)
        #    where H = num_heads, D = state_dim
        z_tokens = self.embedding_to_z(embedded_input)            # (B, S, H*D)
        z_tokens = z_tokens.view(batch_size, sequence_len, self.num_heads, self.state_dim)
        z_tokens = torch.tanh(z_tokens)  # MinimalRNN uses tanh on input encoding

        # 3) Allocate space for states: next_states[:, t] will store h_t for each head
        #    We'll shift indexing by +1 so that next_states[:, 1] = h_1, ...
        next_states = torch.zeros(batch_size, sequence_len + 1, self.num_heads, self.state_dim,
                                  device=device)
        # h_0 = 0 by default
        last_state = torch.zeros(batch_size, self.num_heads, self.state_dim, device=device)

        # 4) Main time-step loop for MinimalRNN
        for t in range(sequence_len):
            # (B, H, D) => gating
            # We'll do a parallel matmul per head using einsum:
            #   h_{t-1} * U_h^T + z_t * U_z^T + b_u
            # shapes:
            #   last_state: (B, H, D)
            #   U_h: (H, D, D)
            # So each head i: last_state[:,i] @ U_h[i], similarly for z_t
            u_t = torch.einsum('bhd,hdd->bhd', last_state, self.U_h) \
                  + torch.einsum('bhd,hdd->bhd', z_tokens[:, t], self.U_z)
            u_t = u_t + self.b_u  # add bias (B, H, D)
            u_t = torch.sigmoid(u_t)

            # MinimalRNN hidden state update:
            # h_t = u_t * h_{t-1} + (1 - u_t) * z_t
            h_t = u_t * last_state + (1.0 - u_t) * z_tokens[:, t]

            # layer normalization of the new state
            # We'll do it per-head:
            h_t = h_t.view(batch_size * self.num_heads, self.state_dim)
            h_t = self.layer_norm_state(h_t)
            h_t = h_t.view(batch_size, self.num_heads, self.state_dim)

            # Update tracked states
            next_states[:, t + 1] = h_t
            last_state = h_t

        # 5) "Attention output" for each head by shaping h_t -> feed-forward
        # next_states[:, 1:] => shape (B, S, H, D)
        # We can do a linear transform (output_shaper) first, akin to original ssm code.
        # shape: (B, S, H, D) => multiply by (H, D, D) => (B, S, H, D)
        shaped_output = torch.einsum('bshd,hdd->bshd', next_states[:, 1:], self.output_shaper)

        # 6) Per-head feed-forward
        # shaped_output: (B, S, H, D)
        # We'll feed each head's output into its own feed-forward layer:
        # result => (B, H, S, embedding_dim), then we swap dimensions back
        layer_outputs = []
        for i, ff in enumerate(self.feed_forward_layers):
            # shaped_output[:, :, i, :] => (B, S, D)
            out = ff(shaped_output[:, :, i, :])  # (B, S, embedding_dim)
            layer_outputs.append(out)

        # Stack: => (B, H, S, embedding_dim)
        layer_outputs = torch.stack(layer_outputs, dim=1)  # (B, H, S, E)

        # We want (B, S, H, E) so we can apply an attention weight per layer
        layer_outputs = layer_outputs.permute(0, 2, 1, 3)  # (B, S, H, E)

        # 7) Attention weighting across heads
        # Compute scores => shape (B, S, H, 1)
        attention_scores = self.layer_attention_weights(layer_outputs)  # linear from E->1
        attention_scores = F.softmax(attention_scores, dim=2)           # softmax over H

        # Weighted sum over heads
        weighted = layer_outputs * attention_scores  # (B, S, H, E)
        # Summation across heads => (B, S, E)
        weighted_output = weighted.sum(dim=2)

        # 8) Final normalization => (B, S, E)
        reshaped_attention = self.layer_norm_output(weighted_output)

        return reshaped_attention
