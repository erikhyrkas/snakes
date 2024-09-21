import torch.nn.functional as F

def pad_to_chunk_size(embedded_tokens, chunk_size):
    """
    Pads the embedded tokens so that the sequence length is divisible by chunk_size.
    Creates a mask that marks the original valid tokens (1 for valid, 0 for padded).

    Inputs:
    - embedded_tokens: Tensor of shape [batch_size, current_sequence_length, embedding_dim]
    - chunk_size: The size of each chunk (int)

    Outputs:
    - padded_embedded_tokens: Padded tensor of shape [batch_size, padded_sequence_length, embedding_dim]
    - valid_token_mask: Mask tensor of shape [batch_size, padded_sequence_length] (1 = valid token, 0 = padding)
    """
    current_sequence_length = embedded_tokens.size(1)

    # Calculate padding needed to make sequence divisible by chunk_size
    if current_sequence_length % chunk_size != 0:
        padding_needed = chunk_size - (current_sequence_length % chunk_size)
        # Pad the embedded tokens along the sequence length (2nd dimension)
        padded_embedded_tokens = F.pad(embedded_tokens, (0, 0, 0, padding_needed))  # Pad only the sequence length
        # Also pad the valid token mask with zeros to account for padding
        valid_token_mask = torch.ones(embedded_tokens.size(0), current_sequence_length, device=embedded_tokens.device)
        valid_token_mask = F.pad(valid_token_mask, (0, padding_needed), value=0)
    else:
        # No padding needed
        padded_embedded_tokens = embedded_tokens
        valid_token_mask = torch.ones(embedded_tokens.size(0), current_sequence_length, device=embedded_tokens.device)

    return padded_embedded_tokens, valid_token_mask