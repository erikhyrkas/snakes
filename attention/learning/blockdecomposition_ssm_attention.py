import torch
import torch.nn as nn


class BlockDecomposedSSMAttention(nn.Module):
    """
    A PyTorch module that implements a block-decomposed state space model (SSM) attention mechanism.

    This model is designed to process sequences in blocks, allowing it to handle long sequences more efficiently.
    It leverages the principles of state space models (SSMs) by incorporating state matrices and block decomposition,
    making it particularly suitable for sequence modeling tasks where the relationship between input and output sequences
    can be captured by state transitions.

    Attributes:
        state_size (int): The dimensionality of the state vector. Default is 448.
        input_size (int): The dimensionality of the input vector. Default is 448.
        output_size (int): The dimensionality of the output vector. Default is 448.
        block_size (int): The size of the blocks into which the input sequence is divided for processing. Default is 32.
        A (torch.nn.Parameter): The state transition matrix, representing how the state vector evolves over time.
        B (torch.nn.Parameter): The input-to-state matrix, representing how the input influences the state.
        C (torch.nn.Parameter): The state-to-output matrix, representing how the state produces the output.
        dropout (torch.nn.Dropout): A dropout layer applied to the output, with a default dropout rate of 0.1.

    Methods:
        forward(x):
            Computes the forward pass of the model.
            Args:
                x (torch.Tensor): The input tensor of shape (batch_size, seq_len, input_size).
            Returns:
                torch.Tensor: The output tensor of shape (batch_size, seq_len, output_size).

    Example Usage:
        model = BlockDecomposedSSMAttention()
        x = torch.randn(10, 100, 448)  # batch_size=10, seq_len=100, input_size=448
        output = model(x)
    """
    def __init__(self, state_dim=448, input_dim=448, output_dim=448, block_size=32, dropout_rate=0.1):
        super(BlockDecomposedSSMAttention, self).__init__()
        self.state_size = state_dim
        self.input_size = input_dim
        self.output_size = output_dim
        self.block_size = block_size

        # Initialize matrices with adjusted initialization
        self.A = nn.Parameter(torch.randn(state_dim, state_dim) * 0.1 + 0.001)
        self.B = nn.Parameter(torch.randn(state_dim, input_dim) * 0.1 + 0.001)
        self.C = nn.Parameter(torch.randn(output_dim, state_dim) * 0.1 + 0.001)
        self.dropout = nn.Dropout(dropout_rate)

    def forward(self, x):
        """
        Forward pass through the BlockDecomposedSSMAttention model.

        The input sequence is divided into blocks of a specified size. Each block is processed independently
        by the state space model using the matrices A, B, and C, which govern the evolution of the state,
        the influence of the input on the state, and the production of the output from the state, respectively.
        The outputs of the blocks are combined to form the final output sequence.

        Args:
            x (torch.Tensor): Input tensor of shape (batch_size, seq_len, input_size).

        Returns:
            torch.Tensor: Output tensor of shape (batch_size, seq_len, output_size).
        """
        # x is of shape (batch_size, seq_len, input_size)
        batch_size, seq_len, _ = x.size()

        # Number of blocks
        num_blocks = (seq_len + self.block_size - 1) // self.block_size

        # Precompute transposes for efficiency
        B_transpose = self.B.T
        C_transpose = self.C.T

        y = torch.zeros(batch_size, seq_len, self.output_size).to(x.device)

        for i in range(num_blocks):
            # Define the start and end of the block
            start = i * self.block_size
            end = min(start + self.block_size, seq_len)

            # Extract the block
            x_block = x[:, start:end, :]  # x_block shape: (batch_size, block_size, input_size)

            # Compute h_block: (batch_size, block_size, state_size)
            h_block = torch.bmm(x_block, B_transpose.unsqueeze(0).expand(batch_size, -1, -1))

            # Compute intermediate_result: (batch_size, block_size, state_size)
            intermediate_result = torch.bmm(h_block, self.A.unsqueeze(0).expand(batch_size, -1, -1))

            # Compute y_block: (batch_size, block_size, output_size)
            y_block = torch.bmm(intermediate_result, C_transpose.unsqueeze(0).expand(batch_size, -1, -1))

            y_block = self.dropout(y_block)  # Apply dropout

            # Store the result in the corresponding positions using in-place addition
            y[:, start:end, :].add_(y_block)

        return y
