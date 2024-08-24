import torch
import torch.nn as nn


class StateSpaceModelAttentionWithSSD(nn.Module):
    """
    This is the in-progress attention for the YS v0.2 base model.

    Implementation Summary:
    -----------------------
    * State Space Model Focused -- Prioritizes sequential processing for hardware efficiency.
    * State Space Duality -- Balances linear and quadratic SSMs for efficiency vs. quality flexibility.
    * Multi-Head Attention -- Incorporates multiple attention heads to capture diverse aspects of the input,
      improving the model's ability to learn complex patterns.
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
    of multi-head attention allows the model to capture diverse aspects of the input sequences, enhancing the representation
    learned by the model. Structured semiseparable matrices allow for efficient memory usage, enabling the model to handle
    larger state sizes without compromising speed. Layer normalization and dropout are critical for maintaining numerical
    stability and preventing overfitting, especially in deep learning environments with long sequences. These techniques,
    inspired by recent advancements in SSMs, enable the model to achieve high performance on language modeling tasks with
    reduced computational overhead.
    """

    def __init__(self, state_dim=448, input_dim=448, output_dim=448, sequence_length_threshold=512,
                 dropout=0.1, block_size=32, num_heads=8):
        super(StateSpaceModelAttentionWithSSD, self).__init__()

        self.state_dim = state_dim
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.sequence_length_threshold = sequence_length_threshold
        self.dropout = dropout
        self.block_size = block_size
        self.num_heads = num_heads  # Store num_heads, default to 1

        # Input transformation
        if input_dim != state_dim:
            self.input_transform = nn.Linear(input_dim, state_dim)
        else:
            self.input_transform = None

        # Output transformation
        if state_dim != output_dim:
            self.output_transform = nn.Linear(state_dim, output_dim)
        else:
            self.output_transform = None

        # Adjust the state dimension per head
        self.head_dim = state_dim // num_heads

        # Initialize attention matrices with Xavier uniform
        self.W_q = nn.Parameter(torch.empty(num_heads, self.head_dim, self.head_dim))
        nn.init.xavier_uniform_(self.W_q)
        self.W_k = nn.Parameter(torch.empty(num_heads, self.head_dim, self.head_dim))
        nn.init.xavier_uniform_(self.W_k)
        self.W_v = nn.Parameter(torch.empty(num_heads, self.head_dim, self.head_dim))
        nn.init.xavier_uniform_(self.W_v)
        self.W_o = nn.Parameter(torch.empty(state_dim, state_dim))
        nn.init.xavier_uniform_(self.W_o)

        # Initialize semiseparable matrices
        self.SSM_A = nn.Parameter(torch.tril(torch.randn(state_dim, state_dim) * 0.001))
        self.SSM_B = nn.Parameter(torch.tril(torch.randn(state_dim, state_dim) * 0.001))
        self.SSM_C = nn.Parameter(torch.tril(torch.randn(state_dim, state_dim) * 0.001))

        # Dropout layer
        self.dropout_layer = nn.Dropout(dropout)

        # Layer normalization
        self.layer_norm = nn.LayerNorm(state_dim, eps=1e-5)

    def forward(self, x):
        device = x.device

        if self.input_transform:
            x = self.input_transform(x)

        batch_size, seq_len, _ = x.size()

        # Reshape input to add head dimension
        x = x.view(batch_size, seq_len, self.num_heads, self.head_dim)

        # Perform einsum with broadcasting across heads
        q = torch.einsum('bshd,hvd->bshv', x, self.W_q)
        k = torch.einsum('bshd,hvd->bshv', x, self.W_k)
        v = torch.einsum('bshd,hvd->bshv', x, self.W_v)

        # Flatten the heads back to match the original state_dim
        q = q.reshape(batch_size, seq_len, -1)
        k = k.reshape(batch_size, seq_len, -1)
        v = v.reshape(batch_size, seq_len, -1)

        # Processing with SSM
        if seq_len > self.sequence_length_threshold:
            attention_scores = torch.einsum('bsd,bsd->bs', q, k)
            attention_mean = torch.mean(attention_scores, dim=1)
            length_scale = torch.log(torch.tensor(seq_len, dtype=torch.float32) + 1).to(device)
            dynamic_weight_clamped = torch.sigmoid(10 * (attention_mean / length_scale))
            dynamic_weight_clamped_mean = dynamic_weight_clamped.mean()
        else:
            dynamic_weight_clamped = None
            dynamic_weight_clamped_mean = 0

        if dynamic_weight_clamped_mean > 0.99:
            ssm_output = self.quadratic_transform(q, self.SSM_A) + \
                         self.quadratic_transform(k, self.SSM_B) + \
                         self.quadratic_transform(v, self.SSM_C)
        elif dynamic_weight_clamped_mean < 0.01:
            ssm_output = self.linear_transform(q, self.SSM_A) + \
                         self.linear_transform(k, self.SSM_B) + \
                         self.linear_transform(v, self.SSM_C)
        else:
            ssm_linear = self.linear_transform(q, self.SSM_A) + \
                         self.linear_transform(k, self.SSM_B) + \
                         self.linear_transform(v, self.SSM_C)
            ssm_quadratic = self.quadratic_transform(q, self.SSM_A) + \
                            self.quadratic_transform(k, self.SSM_B) + \
                            self.quadratic_transform(v, self.SSM_C)
            dynamic_weight_clamped = dynamic_weight_clamped.unsqueeze(-1).unsqueeze(-1).expand_as(ssm_linear)
            ssm_output = dynamic_weight_clamped * ssm_quadratic + (1 - dynamic_weight_clamped) * ssm_linear

        # Ensure that x is aligned to match ssm_output before adding
        x_aligned = x.view(batch_size, seq_len, -1)

        # Ensure ssm_output and x_aligned have the same shape
        if ssm_output.size() != x_aligned.size():
            raise ValueError(f"Shape mismatch: ssm_output {ssm_output.size()} vs x_aligned {x_aligned.size()}")

        # Add residual connection
        ssm_output += x_aligned

        # Apply dropout
        ssm_output = self.dropout_layer(ssm_output)

        # Apply LayerNorm
        ssm_output = self.layer_norm(ssm_output)

        # Align output dimensions if necessary
        if self.output_transform:
            ssm_output = self.output_transform(ssm_output)

        # Final output, matching dimensions of W_o
        output = torch.einsum('bsd,do->bso', ssm_output, self.W_o)

        return output

    def block_decomposition(self, x, matrix):
        """
        Apply block decomposition to matrix operations for better memory efficiency.
        This technique, derived from the SSD framework, is critical for managing memory usage efficiently,
        allowing the model to scale without a linear increase in memory consumption.
        """
        output = torch.zeros_like(x)
        num_blocks = (x.size(-1) + self.block_size - 1) // self.block_size  # ceil division to handle partial blocks

        for i in range(num_blocks):
            start = i * self.block_size
            end = min(start + self.block_size, x.size(-1))  # Ensure end does not exceed x's dimension

            if start == end:
                continue  # Skip this block if it results in a zero-sized tensor

            matrix_slice = matrix[start:end, start:end]

            if matrix_slice.size(0) == 0 or matrix_slice.size(1) == 0:
                continue  # Skip if the matrix_slice has zero size

            # Perform the einsum operation with the correctly sized slices
            output[..., start:end] = torch.einsum('bsi,ij->bsj', x[..., start:end], matrix_slice)

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
        num_blocks = (x.size(-1) + self.block_size - 1) // self.block_size

        for i in range(num_blocks):
            start = i * self.block_size
            end = min(start + self.block_size, x.size(-1))  # Ensure end does not exceed x's dimension
            output[..., start:end] = torch.einsum('bsi,ij,bsk->bsj', x[..., start:end], matrix[start:end, start:end],
                                                  x[..., start:end]) * 0.1

        return output
