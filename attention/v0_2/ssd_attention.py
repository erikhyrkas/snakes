import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class SSDAttention(nn.Module):
    """
    SSDAttention implements a custom attention mechanism inspired by the Mamba 2 paper. This implementation
    is adapted from concepts discussed in their Apache 2.0 licensed work but has been substantially modified and is not
    a direct derivative.

    The original code from which inspiration was drawn is under the Apache License 2.0. Acknowledgment and thanks to
    the authors and contributors of the Mamba project for their insights and foundational work. You can find the
    original code and license at: https://github.com/state-spaces/mamba/blob/main/mamba_ssm/modules/ssd_minimal.py

    This version of SSDAttention is provided under the MIT License, which permits use, copy, modify, merge,
    publish, distribute, sublicense, and/or sell copies of the software, and to permit persons to whom the software is
    furnished to do so, subject to the following conditions: - The above copyright notice and this permission notice
    shall be included in all copies or substantial portions of the software. - The software is provided "AS IS",
    without warranty of any kind.

    Args:
        input_dim (int): Dimensionality of the input embeddings.
        state_dim (int): Dimensionality of the state used within the attention mechanism.
        output_dim (int): Desired dimensionality of the output.
        block_length (int, optional): Length of each block/chunk for processing. Default is 32.
        number_of_heads (int, optional): Number of attention heads. Default is 8.

    Expected tensor shapes:
        - Input tensor: (batch_size, sequence_length, input_dim)
        - Output tensor: (batch_size, sequence_length, output_dim)
    """
    def __init__(self, input_dim, state_dim, output_dim, block_length, number_of_heads):
        super(SSDAttention, self).__init__()

        self.block_length = block_length
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.number_of_heads = number_of_heads
        self.state_dim = state_dim

        # Ensure that input_dim is divisible by number_of_heads
        if input_dim % number_of_heads != 0:
            raise ValueError(f"input_dim ({input_dim}) must be divisible by number_of_heads ({number_of_heads})")

        # Dimensionality of each attention head
        self.head_dim = input_dim // number_of_heads

        # Initialize the learnable parameters: attention_weights, state_transformation_weights,
        # and output_transformation_weights
        self.attention_weights = nn.Parameter(torch.randn(1, 1, 1, self.number_of_heads) * 0.1 + 0.01)
        self.state_transformation_weights = nn.Parameter(
            torch.randn(1, 1, self.number_of_heads, self.state_dim) * 0.1 + 0.01)
        self.output_transformation_weights = nn.Parameter(
            torch.randn(1, 1, self.number_of_heads, self.state_dim) * 0.1 + 0.01)

        # Linear layer to project the attention output to the desired output dimension
        self.output_projection = nn.Linear(input_dim, self.output_dim)

    @staticmethod
    def cumulative_sum_with_mask(tensor):
        """
        Compute the cumulative sum of the tensor along the last dimension, using a lower triangular mask to enforce
        sequential dependence.

        Args:
            tensor (Tensor): Input tensor of shape (batch_size, sequence_length).

        Returns:
            Tensor: Cumulative sum tensor with shape (batch_size, sequence_length, sequence_length).
        """
        sequence_length = tensor.size(-1)
        lower_triangular_mask = torch.tril(
            torch.ones(sequence_length, sequence_length, device=tensor.device, dtype=torch.bool), diagonal=-1)

        cumulative_sum = torch.cumsum(tensor.unsqueeze(-1) * lower_triangular_mask.float(), dim=-2)
        cumulative_sum = cumulative_sum.masked_fill(~lower_triangular_mask, -torch.inf)

        return cumulative_sum

    def forward(self, input_tensor):
        """
        Args:
            input_tensor (Tensor): Input tensor of shape (batch_size, sequence_length, input_dim).

        Returns:
            Tensor: Output tensor of shape (batch_size, sequence_length, output_dim).
        """
        batch_size, sequence_length, _ = input_tensor.shape

        # Calculate the number of blocks/chunks
        num_blocks = math.ceil(sequence_length / self.block_length)

        # Determine padding if the sequence length isn't divisible by block_length
        padding_length = num_blocks * self.block_length - sequence_length
        if padding_length > 0:
            input_tensor = F.pad(input_tensor, (0, 0, 0, padding_length), mode='constant', value=0)

        # Reshape input to (batch_size, sequence_length, number_of_heads, head_dim)
        reshaped_input = input_tensor.view(batch_size, -1, self.number_of_heads, self.head_dim)

        # Expand parameters to match the batch and chunk dimensions
        expanded_attention_weights = self.attention_weights.expand(batch_size, num_blocks, self.block_length,
                                                                   self.number_of_heads)
        expanded_state_transformation_weights = self.state_transformation_weights.expand(batch_size, num_blocks,
                                                                                         self.block_length,
                                                                                         self.number_of_heads,
                                                                                         self.state_dim)
        expanded_output_transformation_weights = self.output_transformation_weights.expand(batch_size, num_blocks,
                                                                                           self.block_length,
                                                                                           self.number_of_heads,
                                                                                           self.state_dim)

        # Rearrange attention_weights to shape (batch_size, number_of_heads, num_blocks, block_length)
        rearranged_attention_weights = expanded_attention_weights.permute(0, 3, 1, 2)
        cumulative_attention_weights = torch.cumsum(rearranged_attention_weights, dim=-1)

        # Compute intra-block attention
        intra_attention_weights = torch.exp(self.cumulative_sum_with_mask(rearranged_attention_weights))
        reshaped_input = reshaped_input.view(batch_size, num_blocks, self.block_length, self.number_of_heads,
                                             self.head_dim)
        intra_block_output = torch.einsum("bclhn,bcshn,bhcls,bcshp->bclhp",
                                          expanded_output_transformation_weights,
                                          expanded_state_transformation_weights,
                                          intra_attention_weights,
                                          reshaped_input)

        # Compute decay states for intra-block processing
        decay_states = torch.exp(cumulative_attention_weights[:, :, :, -1:] - cumulative_attention_weights)
        states = torch.einsum("bclhn,bhcl,bclhp->bchpn", expanded_state_transformation_weights, decay_states,
                              reshaped_input)

        # Initialize states if not provided
        initial_states = torch.zeros_like(states[:, :1])
        states = torch.cat([initial_states, states], dim=1)

        # Compute inter-block decay
        decay_chunk = torch.exp(self.cumulative_sum_with_mask(F.pad(cumulative_attention_weights[:, :, :, -1], (1, 0))))
        inter_block_states = torch.einsum("bhzc,bchpn->bzhpn", decay_chunk, states)
        states = inter_block_states[:, :-1]  # Exclude the last state which is beyond the current chunks

        # Compute output from the states
        state_decay_output = torch.exp(cumulative_attention_weights)
        inter_block_output = torch.einsum('bclhn,bchpn,bhcl->bclhp', expanded_output_transformation_weights, states,
                                          state_decay_output)

        # Combine intra-block and inter-block outputs
        combined_output = intra_block_output + inter_block_output

        # Reshape combined_output back to (batch_size, sequence_length + padding_length, input_dim)
        combined_output = combined_output.reshape(batch_size, -1, self.input_dim)

        # Remove padding if added
        if padding_length > 0:
            combined_output = combined_output[:, :-padding_length, :]

        # Project the attention output to the desired output dimension
        output = self.output_projection(combined_output)

        return output
