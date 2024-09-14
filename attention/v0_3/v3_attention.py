import torch
import torch.nn as nn


class SelectiveSSM(nn.Module):
    def __init__(self, config):
        super(SelectiveSSM, self).__init__()
        self.config = config
        self.head_dim = config.state_dim // config.num_heads

        # Input projections
        self.W_A = nn.Parameter(torch.Tensor(config.num_heads, config.embedding_dim, self.head_dim))
        self.W_B = nn.Parameter(torch.Tensor(config.num_heads, config.embedding_dim, self.head_dim))
        self.W_C = nn.Parameter(torch.Tensor(config.num_heads, config.embedding_dim, self.head_dim))
        self.W_D = nn.Parameter(torch.Tensor(config.num_heads, config.embedding_dim, self.head_dim))

        # Selective mechanism
        self.W_gate = nn.Linear(config.embedding_dim, config.num_heads)

        # Output projection
        self.W_out = nn.Linear(config.state_dim, config.output_dim)

        # Dropout and layer normalization
        self.dropout = nn.Dropout(config.dropout)
        self.layer_norm1 = nn.LayerNorm(config.embedding_dim)
        self.layer_norm2 = nn.LayerNorm(config.output_dim)

        self._reset_parameters()

    def _reset_parameters(self):
        # Initialize attention weights close to zero but slightly positive
        for param in [self.W_A, self.W_B, self.W_C, self.W_D]:
            nn.init.xavier_uniform_(param)
            with torch.no_grad():
                param.mul_(0.05).add_(0.005)
        nn.init.xavier_uniform_(self.W_gate.weight)
        nn.init.zeros_(self.W_gate.bias)
        nn.init.xavier_uniform_(self.W_out.weight)
        nn.init.zeros_(self.W_out.bias)

    def forward(self, x):
        batch_size, seq_len, _ = x.shape

        # Project inputs
        A = torch.einsum('bsi,hio->bhso', x, self.W_A)
        B = torch.einsum('bsi,hio->bhso', x, self.W_B)
        C = torch.einsum('bsi,hio->bhso', x, self.W_C)
        D = torch.einsum('bsi,hio->bhso', x, self.W_D)

        x = self.layer_norm1(x)
        # Compute selective gate
        gate = torch.tanh(self.W_gate(x))

        # Initialize output and state
        output = torch.zeros(batch_size, self.config.num_heads, seq_len, self.head_dim, device=x.device)
        state = torch.zeros(batch_size, self.config.num_heads, self.head_dim, device=x.device)

        # Process sequence in blocks
        for i in range(0, seq_len, self.config.block_size):
            block_end = min(i + self.config.block_size, seq_len)
            block_size = block_end - i

            # Compute S (semiseparable matrix) for the block
            S = torch.tril(torch.ones(block_size, block_size, device=x.device))
            S = S.unsqueeze(0).unsqueeze(0).expand(batch_size, self.config.num_heads, -1, -1)

            a_block = A[:, :, i:block_end]
            b_block = B[:, :, i:block_end]
            block_einsum = torch.einsum('bhij,bhkj->bhik', a_block, b_block)
            block_exp = torch.exp(block_einsum - block_einsum.max())  # Stability trick
            S = block_exp * S

            # Update state and compute output for the block
            for j in range(block_size):
                state = state * torch.sigmoid(D[:, :, i + j]) + C[:, :, i + j] * gate[:, i + j, :, None]
                state = state / (1e-6 + state.norm(dim=-1, keepdim=True))
                S_part = S[:, :, j, :]
                output_part = torch.einsum('bhd,bhj->bhjd', state, S_part)
                output[:, :, i + j] = output_part[:, :, j]

            # Detach state to prevent gradient accumulation
            state = state.detach()

        # Reshape output and apply output projection
        output = output.permute(0, 2, 1, 3).contiguous().view(batch_size, seq_len, -1)
        output = self.W_out(output)
        output = self.dropout(output)
        output = self.layer_norm2(output + x)  # Residual connection

        return output
