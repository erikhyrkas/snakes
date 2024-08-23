import os
import random
import torch
import numpy as np
from torch.utils.data import IterableDataset


def preprocess_and_save_tokens(files, tokenizer, output_dir):
    total_tokens = 0
    if os.path.exists(output_dir):
        for file in files:
            output_file = str(os.path.join(output_dir, os.path.basename(file) + ".npy"))
            tokens = np.load(output_file, mmap_mode='r')
            total_tokens += len(tokens)
        return total_tokens
    os.makedirs(output_dir)

    for file in files:
        tokens = tokenizer.tokenize(open(file, 'r', encoding='utf-8').read())
        tokens = np.array(tokens, dtype=np.int32)
        total_tokens += len(tokens)
        output_file = str(os.path.join(output_dir, os.path.basename(file) + ".npy"))
        np.save(output_file, tokens)
    return total_tokens


class TextDataset(IterableDataset):
    def __init__(self, original_files, tokenizer, max_sequence_length, batch_size, output_dir="./cache_dir",
                 shuffle_files=True):
        self.files = [os.path.join(output_dir, os.path.basename(f) + ".npy") for f in original_files]
        total_tokens = preprocess_and_save_tokens(original_files, tokenizer, output_dir)
        self.max_sequence_length = max_sequence_length
        self.batch_size = batch_size
        self._length = None
        if shuffle_files:
            random.shuffle(self.files)
        self.shuffle_files = shuffle_files
        self.sequence_lengths = []

        # Pre-generate random sequence lengths for all batches
        remaining_tokens = total_tokens
        while remaining_tokens > 0:
            sequence_length = random.randint(32, self.max_sequence_length)
            total_tokens_used = sequence_length * self.batch_size
            if total_tokens_used > remaining_tokens:
                # we still might be able to squeak in a batch or two
                sequence_length = 32
                total_tokens_used = sequence_length * self.batch_size
                if total_tokens_used > remaining_tokens:
                    break
            self.sequence_lengths.append(sequence_length)
            remaining_tokens -= total_tokens_used

    def __iter__(self):
        if self.shuffle_files:
            random.shuffle(self.sequence_lengths)
        sequence_lengths = iter(self.sequence_lengths)
        sequence_length = next(sequence_lengths)
        buffer = []
        buffer_length = 0
        sequences_returned = 0

        for file in self.files:
            tokens = np.load(file, mmap_mode='r')
            file_length = len(tokens)
            start_idx = 0

            while start_idx < file_length:
                # Calculate how many tokens we need to fill the buffer to batch_size
                remaining_space = self.batch_size * sequence_length - buffer_length

                # Number of tokens we can take from the current file to fill the buffer
                end_idx = min(start_idx + remaining_space, file_length)

                # Append tokens from file to the buffer
                buffer.extend(tokens[start_idx:end_idx])
                buffer_length += (end_idx - start_idx)
                start_idx = end_idx

                # If the buffer is full, yield the batch
                if buffer_length >= self.batch_size * sequence_length:
                    # Split buffer into X (inputs) and Y (targets)
                    x = [buffer[i:i + sequence_length] for i in range(0, len(buffer) - sequence_length)]
                    y = [buffer[i:i + sequence_length] for i in range(1, len(buffer) - sequence_length + 1)]

                    for i in range(self.batch_size):
                        sequences_returned += 1
                        # Create a mask with all ones (no padding)
                        mask = torch.ones((sequence_length,), dtype=torch.bool)
                        # Yield batch as torch tensors
                        yield torch.tensor(x[i], dtype=torch.long), torch.tensor(y[i], dtype=torch.long), mask
                        if sequences_returned == self._length:
                            return

                    # Reset buffer and buffer_length
                    buffer = []
                    buffer_length = 0
                    sequence_length = next(sequence_lengths, None)
                    if sequence_length is None:
                        return

    def __len__(self):
        return len(self.sequence_lengths) * self.batch_size
