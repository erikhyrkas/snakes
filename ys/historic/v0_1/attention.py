import torch
import torch.nn as nn

from ys.historic.v0_1.config import Config


class Attention(nn.Module):
    """
    This was the original attention mechanism of YS-120M-base-v0.1.
    It was trained with state_dim=448, input_dim=448, output_dim=448

    This class (originally called `StructuredStateAttention`) is a custom implementation inspired by the principles
    of state space models (SSMs) and attention mechanisms discussed in the Mamba-2 architecture. This class leverages
    structured state space duality (SSD), which connects the efficiency of SSMs with the expressiveness of attention
    mechanisms. Key techniques include the use of semiseparable matrices and block decompositions, enabling efficient
    computation while maintaining the ability to handle complex sequences. The `P`, `Q`, `R`, and `S` matrices in this
    class are initialized in a structured manner to ensure that the state transitions are computationally efficient
    and stable.
    """
    def __init__(self, config: Config):
        super(Attention, self).__init__()
        # Note: I think that state_dim must equal input_dim and output_dim.
        #  I didn't test with other options, but there might be shape issues if you try to diverge.
        self.state_dim = config.state_dim
        self.block_length = config.block_size
        # Initializing structured matrices with small values ensures stability in the model, echoing the use of
        # semiseparable matrices in the Mamba-2 approach.

        # P can be thought of as analogous to the "query" matrix, though it operates on the state space itself.
        # It helps in determining how the current state interacts with itself.
        self.P = nn.Parameter(torch.eye(self.state_dim).repeat(self.state_dim, 1, 1) * 0.1 + 0.01)

        # Q is analogous to the "key" matrix, determining how the input interacts with the state.
        # It transforms the input into a space where it can be integrated into the state update.
        self.Q = nn.Parameter(torch.eye(self.state_dim, config.embedding_dim) * 0.1 + 0.01)

        # R is analogous to the "value" matrix, where the state is transformed into the output space.
        # It maps the updated state to the output, which would be the value in traditional attention.
        self.R = nn.Parameter(torch.eye(config.output_dim, self.state_dim) * 0.1 + 0.01)

        # S acts as an additional transformation, modifying the input directly in the output space.
        # This can be seen as an auxiliary value transformation that works alongside R.
        self.S = nn.Parameter(torch.eye(config.output_dim, config.embedding_dim) * 0.1 + 0.01)

        # Layer normalization is used to maintain numerical stability during state updates, a technique aligned with
        # ensuring structured operations remain efficient.
        self.layer_norm = nn.LayerNorm(self.state_dim)

        # Dropout layers to introduce regularization, preventing overfitting while training the model.
        self.input_dropout = nn.Dropout(p=config.dropout)
        self.output_dropout = nn.Dropout(p=config.dropout)

    def forward(self, x):
        device = x.device
        batch_size, sequence_length, _ = x.shape
        outputs = []
        state = torch.zeros(batch_size, self.state_dim, device=device)

        # Applying dropout to the inputs, an operation used to stabilize training in structured models.
        x = self.input_dropout(x)

        # Expand structured matrices for batch processing, maintaining the analogy to how queries and keys are
        # expanded in traditional attention.
        p_expanded = self.P.unsqueeze(0)
        q_expanded = self.Q.expand(batch_size, -1, -1)
        s_expanded = self.S.expand(batch_size, -1, -1)

        for start in range(0, sequence_length, self.block_length):
            end = min(start + self.block_length, sequence_length)
            x_block = x[:, start:end, :]

            for t in range(x_block.shape[1]):
                input_t = x_block[:, t, :].unsqueeze(-1)

                # Quadratic computation based on state interactions, aligning with the semiseparable matrix
                # multiplications in SSMs.

                # The current state is updated based on its previous interactions (analogous
                # to how queries interact with keys).
                state_quad = torch.matmul(state.unsqueeze(-1), state.unsqueeze(-2))
                state = torch.einsum('bij,bijk->bk', state_quad, p_expanded) + \
                        torch.matmul(q_expanded, input_t).squeeze(-1)

                # Normalizing the state to maintain stability and ensure structured operations.
                state = self.layer_norm(state)

                # Combining state and input to produce the output, mirroring structured matrix operations in dual
                # forms of attention.
                output_t = torch.matmul(self.R, state.unsqueeze(-1)).squeeze(-1) + \
                           torch.matmul(s_expanded, input_t).squeeze(-1)
                outputs.append(output_t.unsqueeze(1))

            # Detaching the state to prevent gradients from propagating through the sequence, which helps manage long
            # sequences efficiently.
            state = state.detach()

        # Concatenating outputs and applying dropout, final steps for output regularization.
        final_output = torch.cat(outputs, dim=1)

        final_output = self.output_dropout(final_output)

        return final_output
