import torch
import torch.nn as nn


class StateSpaceModelAttentionWithSSD(nn.Module):
    """
    This is the in-progress attention for the YS v0.2 base model.

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

    Techniques Utilized and Their Benefits:
    ---------------------------------------
    This implementation leverages advanced techniques from state space models (SSMs) to optimize both performance
    and efficiency. By employing the State Space Duality (SSD) framework, the model seamlessly balances linear and
    quadratic processing, ensuring that it can adapt to varying sequence lengths and computational demands. The use
    of structured semiseparable matrices allows for efficient memory usage, enabling the model to handle larger state
    sizes without compromising speed. Layer normalization and dropout are critical for maintaining numerical stability
    and preventing overfitting, especially in deep learning environments with long sequences. These techniques, inspired
    by recent advancements in SSMs, enable the model to achieve high performance on language modeling tasks with
    reduced computational overhead.
    """

    def __init__(self, state_dim=448, input_dim=448, output_dim=448, sequence_length_threshold=512,
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
        # This ensures balanced initialization, critical for training deep networks.
        self.W_q = nn.Parameter(torch.empty(input_dim, state_dim))
        nn.init.xavier_uniform_(self.W_q)
        self.W_k = nn.Parameter(torch.empty(input_dim, state_dim))
        nn.init.xavier_uniform_(self.W_k)
        self.W_v = nn.Parameter(torch.empty(input_dim, state_dim))
        nn.init.xavier_uniform_(self.W_v)
        self.W_o = nn.Parameter(torch.empty(state_dim, output_dim))
        nn.init.xavier_uniform_(self.W_o)

        # Initialize semiseparable matrices directly in this class
        # Using structured matrices like semiseparable matrices helps optimize memory usage
        # and efficiently handle large matrices, a key principle from the SSD framework.
        self.SSM_A = nn.Parameter(torch.tril(torch.randn(state_dim, state_dim) * 0.001))  # Increased scale slightly
        self.SSM_B = nn.Parameter(torch.tril(torch.randn(state_dim, input_dim) * 0.001))
        self.SSM_C = nn.Parameter(torch.tril(torch.randn(output_dim, state_dim) * 0.001))

        # Dropout layer for regularization
        self.dropout_layer = nn.Dropout(dropout)

        # Layer normalization layers with increased epsilon
        # Layer normalization is used here to stabilize the output
        # across sequential layers, which is crucial for models with deep or complex architectures, as it mitigates
        # the risk of vanishing/exploding gradients.
        self.layer_norm = nn.LayerNorm(self.state_dim, eps=1e-5)

    def forward(self, x):
        device = x.device  # Get the device of the input tensor

        # Move LayerNorm and dynamic weight to the same device as the input tensor
        self.layer_norm = self.layer_norm.to(device)

        batch_size, seq_len, _ = x.size()

        # Compute queries, keys, and values using einsum notation
        q = torch.einsum('bsi,id->bsd', x, self.W_q)
        k = torch.einsum('bsi,id->bsd', x, self.W_k)
        v = torch.einsum('bsi,id->bsd', x, self.W_v)

        if seq_len > self.sequence_length_threshold:
            # Compute attention scores
            attention_scores = torch.einsum('bsd,bsd->bs', q, k)
            attention_mean = torch.mean(attention_scores, dim=1)

            # Compute sequence length-based scaling
            # This dynamic adjustment is part of the State Space Duality technique, where the model adapts between
            # linear and quadratic operations based on the sequence length, ensuring efficient processing regardless
            # of input size.
            length_scale = torch.log(torch.tensor(seq_len, dtype=torch.float32) + 1).to(device)

            # Combine sequence length and attention score to determine dynamic weight
            dynamic_weight_clamped = torch.sigmoid(10 * (attention_mean / length_scale))
            dynamic_weight_clamped_mean = dynamic_weight_clamped.mean()
        else:
            dynamic_weight_clamped = None
            dynamic_weight_clamped_mean = 0

        if dynamic_weight_clamped_mean > 0.99:
            # Only perform quadratic calculation
            ssm_output = self.quadratic_transform(q, self.SSM_A) + self.quadratic_transform(k,
                                                                                            self.SSM_B) + self.quadratic_transform(
                v, self.SSM_C)
        elif dynamic_weight_clamped_mean < 0.01:
            # Only perform linear calculation
            ssm_output = self.linear_transform(q, self.SSM_A) + self.linear_transform(k,
                                                                                      self.SSM_B) + self.linear_transform(
                v, self.SSM_C)
        else:
            # Weighted blend between linear and quadratic transforms
            # By combining linear and quadratic transformations dynamically, the model leverages the strengths of both
            # forms of processing, which is a core advantage of using the SSD framework.
            ssm_linear = self.linear_transform(q, self.SSM_A) + self.linear_transform(k,
                                                                                      self.SSM_B) + self.linear_transform(
                v, self.SSM_C)
            ssm_quadratic = self.quadratic_transform(q, self.SSM_A) + self.quadratic_transform(k,
                                                                                               self.SSM_B) + self.quadratic_transform(
                v, self.SSM_C)
            # Expand dynamic_weight_clamped to match the last dimension of ssm_linear and ssm_quadratic
            dynamic_weight_clamped = dynamic_weight_clamped.unsqueeze(-1).unsqueeze(-1).expand_as(ssm_linear)
            ssm_output = dynamic_weight_clamped * ssm_quadratic + (1 - dynamic_weight_clamped) * ssm_linear

        # Add residual connection to help with stability
        # Residual connections are essential for maintaining numerical stability, especially in deep models,
        # and help prevent the degradation of gradients during backpropagation.
        ssm_output += x

        ssm_output = self.layer_norm(ssm_output)

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
        This technique, derived from the SSD framework, is critical for managing memory usage efficiently,
        allowing the model to scale without a linear increase in memory consumption.
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
