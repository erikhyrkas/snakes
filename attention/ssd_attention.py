import torch
import torch.nn as nn


class StateSpaceModelAttentionWithSSD(nn.Module):
    """
    Implementation Summary:
    -----------------------
    * State Space Model Focused -- Prioritizes sequential processing for hardware efficiency.
    * State Space Duality -- Balances linear and quadratic SSMs for efficiency vs. quality flexibility.
    * Structured Processing for Quadratic SSMs -- Applies structured methods to efficiently manage quadratic operations.
    * Block Decomposition of Semiseparable Matrices -- Optimizes memory usage by breaking down large matrices.
    * Layer Normalization -- Stabilizes outputs across sequential and attention layers.
    * Memory and Numerical Stability -- Uses small random initialization with added constants to ensure stability.
    * Dropout Regularization -- Prevents overfitting, particularly important in sequential models with SSMs.

    This class is optimized for efficient, sequential attention processing using structured state space models (SSMs),
    tailored for environments with limited hardware resources.
    """

    def __init__(self, state_dim=448, input_dim=448, output_dim=448, sequence_length_threshold=256,
                 dropout=0.1, block_size=32):
        super(StateSpaceModelAttentionWithSSD, self).__init__()

        # Store parameters
        self.state_dim = state_dim
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.sequence_length_threshold = sequence_length_threshold
        self.dropout = dropout
        self.block_size = block_size

        # Initialize attention matrices with Xavier uniform
        self.W_q = nn.Parameter(torch.empty(input_dim, state_dim))
        nn.init.xavier_uniform_(self.W_q)
        self.W_k = nn.Parameter(torch.empty(input_dim, state_dim))
        nn.init.xavier_uniform_(self.W_k)
        self.W_v = nn.Parameter(torch.empty(input_dim, state_dim))
        nn.init.xavier_uniform_(self.W_v)
        self.W_o = nn.Parameter(torch.empty(state_dim, output_dim))
        nn.init.xavier_uniform_(self.W_o)

        # Initialize semiseparable matrices directly in this class
        self.SSM_A = nn.Parameter(torch.tril(torch.randn(state_dim, state_dim) * 0.001))  # Increased scale slightly
        self.SSM_B = nn.Parameter(torch.tril(torch.randn(state_dim, input_dim) * 0.001))
        self.SSM_C = nn.Parameter(torch.tril(torch.randn(output_dim, state_dim) * 0.001))

        # Learnable dynamic weight
        self.dynamic_weight = nn.Parameter(torch.tensor(0.5))  # Initialized at 0.5 (neutral)

        # Dropout layer for regularization
        self.dropout_layer = nn.Dropout(dropout)

        # Layer normalization layers with increased epsilon
        self.layer_norm = nn.LayerNorm(self.state_dim, eps=1e-5)

    def forward(self, x):
        device = x.device  # Get the device of the input tensor

        # Move LayerNorm and dynamic weight to the same device as the input tensor
        self.layer_norm = self.layer_norm.to(device)
        self.dynamic_weight = self.dynamic_weight.to(device)

        batch_size, seq_len, _ = x.size()

        # Compute queries, keys, and values using einsum notation
        q = torch.einsum('bsi,id->bsd', x, self.W_q)
        k = torch.einsum('bsi,id->bsd', x, self.W_k)
        v = torch.einsum('bsi,id->bsd', x, self.W_v)

        dynamic_weight_clamped = torch.sigmoid(self.dynamic_weight)  # Ensure the weight stays within [0, 1]

        if seq_len <= self.sequence_length_threshold and dynamic_weight_clamped > 0.99:
            # Only perform quadratic calculation
            ssm_output = self.quadratic_transform(q, self.SSM_A) + self.quadratic_transform(k,
                                                                                            self.SSM_B) + self.quadratic_transform(
                v, self.SSM_C)
            ssm_output = self.layer_norm(ssm_output)
        elif seq_len > self.sequence_length_threshold or dynamic_weight_clamped < 0.01:
            # Only perform linear calculation
            ssm_output = self.linear_transform(q, self.SSM_A) + self.linear_transform(k,
                                                                                      self.SSM_B) + self.linear_transform(
                v, self.SSM_C)
            ssm_output = self.layer_norm(ssm_output)
        else:
            # Weighted blend between linear and quadratic transforms
            ssm_linear = self.linear_transform(q, self.SSM_A) + self.linear_transform(k,
                                                                                      self.SSM_B) + self.linear_transform(
                v, self.SSM_C)
            ssm_linear = self.layer_norm(ssm_linear)

            ssm_quadratic = self.quadratic_transform(q, self.SSM_A) + self.quadratic_transform(k,
                                                                                               self.SSM_B) + self.quadratic_transform(
                v, self.SSM_C)
            ssm_quadratic = self.layer_norm(ssm_quadratic)

            ssm_output = dynamic_weight_clamped * ssm_quadratic + (1 - dynamic_weight_clamped) * ssm_linear

        # Add residual connection to help with stability
        ssm_output += x

        # Apply dropout and final transformation
        ssm_output = self.dropout_layer(ssm_output)
        output = torch.einsum('bsd,do->bso', ssm_output, self.W_o)

        # Check for numerical stability
        # if torch.any(torch.isnan(ssm_output)) or torch.any(torch.isinf(ssm_output)):
        #     print("Numerical instability detected.")

        return output

    def block_decomposition(self, x, matrix):
        """
        Apply block decomposition to matrix operations for better memory efficiency.
        """
        output = torch.zeros_like(x)
        num_blocks = x.size(-1) // self.block_size

        for i in range(num_blocks):
            start = i * self.block_size
            end = start + self.block_size
            output[..., start:end] = torch.einsum('bsi,ij->bsj', x[..., start:end], matrix[start:end, start:end])

        return output

    def linear_transform(self, x, matrix):
        """
        Apply the linear (recurrent) form of the transformation using block decomposition.
        """
        return self.block_decomposition(x, matrix)

    def quadratic_transform(self, x, matrix):
        """
        Apply the quadratic (attention-like) form of the transformation using block decomposition.
        This uses the structured matrix in a way similar to attention mechanisms.
        """
        output = torch.zeros_like(x)
        num_blocks = x.size(-1) // self.block_size

        for i in range(num_blocks):
            start = i * self.block_size
            end = start + self.block_size
            output[..., start:end] = torch.einsum('bsi,ij,bsk->bsj', x[..., start:end], matrix[start:end, start:end],
                                                  x[..., start:end]) * 0.1

        return output
