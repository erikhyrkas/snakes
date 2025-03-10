import torch
import torch.nn as nn
import torch.nn.functional as F
from ys.language_model.config import Config


class MinimalRNNSimple(nn.Module):
    """
    A simplified version of MinimalRNN-based sequence layer:
      - Single 'head' (no multi-head).
      - Minimal gating: h_t = u_t * h_{t-1} + (1-u_t)*z_t
      - One final projection to embedding dimension (optional).
    """

    def __init__(self, config: Config):
        super().__init__()
        self.embedding_dim = config.embedding_dim
        self.state_dim = config.state_dim

        # Project input embeddings to 'z' dimension (same as state_dim).
        self.embedding_to_z = nn.Linear(self.embedding_dim, self.state_dim)

        # MinimalRNN parameters for gating:
        #   h_{t-1} -> gate, z_t -> gate
        self.U_h = nn.Parameter(torch.Tensor(self.state_dim, self.state_dim))
        self.U_z = nn.Parameter(torch.Tensor(self.state_dim, self.state_dim))
        self.b_u = nn.Parameter(torch.Tensor(self.state_dim))

        # Optional final projection from state_dim -> embedding_dim
        # (So the output shape matches your embedding size.)
        self.output_projection = nn.Linear(self.state_dim, self.embedding_dim)

        # Normalizations
        self.layer_norm_state = nn.LayerNorm(self.state_dim)
        self.layer_norm_output = nn.LayerNorm(self.embedding_dim)

        # Dropout on input if desired
        self.dropout_start = nn.Dropout(config.dropout_rate)

        # Weight initialization
        self._initialize_weights()

    def _initialize_weights(self):
        nn.init.xavier_uniform_(self.embedding_to_z.weight)
        nn.init.zeros_(self.embedding_to_z.bias)

        nn.init.xavier_uniform_(self.U_h)
        nn.init.xavier_uniform_(self.U_z)
        nn.init.zeros_(self.b_u)

        nn.init.xavier_uniform_(self.output_projection.weight)
        nn.init.zeros_(self.output_projection.bias)

    def forward(self, embedded_input):
        """
        Inputs:
          embedded_input: (batch_size, seq_len, embedding_dim)
        Returns:
          output: (batch_size, seq_len, embedding_dim)
        """
        batch_size, seq_len, _ = embedded_input.size()
        device = embedded_input.device

        # 1) Optional dropout
        x = self.dropout_start(embedded_input)

        # 2) Map embeddings to z-space
        #    shape => (B, S, state_dim)
        z = torch.tanh(self.embedding_to_z(x))

        # 3) Allocate hidden states for each time-step
        #    We'll store them to do a final projection
        states = torch.zeros(batch_size, seq_len + 1, self.state_dim, device=device)

        # h_0 = zero
        h_t = torch.zeros(batch_size, self.state_dim, device=device)

        # 4) MinimalRNN time-step
        for t in range(seq_len):
            # gate u_t = sigmoid( h_{t-1} * U_h + z_t * U_z + b_u )
            # shapes:
            #   h_t: (B, D)
            #   U_h: (D, D)
            # => h_t @ U_h => (B, D)
            # similarly for z_t
            gate_input = h_t @ self.U_h + z[:, t, :] @ self.U_z + self.b_u
            u_t = torch.sigmoid(gate_input)

            # h_t = u_t * h_{t-1} + (1-u_t)*z_t
            h_t = u_t * h_t + (1 - u_t) * z[:, t, :]

            # Optionally normalize each step
            h_t = self.layer_norm_state(h_t)

            # Store the new state
            states[:, t + 1, :] = h_t

        # 5) (Optional) Output projection from state_dim -> embedding_dim
        # We typically want the same shape as the input embedding
        # states[:, 1:] => (B, S, D)
        output_states = states[:, 1:, :]
        output_emb = self.output_projection(output_states)  # (B, S, E)

        # 6) Final normalization
        output_emb = self.layer_norm_output(output_emb)

        return output_emb  # shape => (B, S, embedding_dim)
