import os
import random
import torch
import numpy as np
from torch.utils.data import IterableDataset


def preprocess_and_save_tokens(files, tokenizer, cache_dir):
    total_tokens = 0
    if os.path.exists(cache_dir):
        for file in files:
            output_file = str(os.path.join(cache_dir, os.path.basename(file) + ".npy"))
            if not os.path.exists(output_file):
                total_tokens += tokenize_file(cache_dir, file, tokenizer)
            else:
                tokens = np.load(output_file, mmap_mode='r')
                total_tokens += len(tokens)
        return total_tokens
    os.makedirs(cache_dir)

    for file in files:
        total_tokens += tokenize_file(cache_dir, file, tokenizer)
    return total_tokens


def tokenize_file(cache_dir, file, tokenizer):
    tokens = tokenizer.tokenize(open(file, 'r', encoding='utf-8').read())
    tokens = np.array(tokens, dtype=np.int32)
    output_file = str(os.path.join(cache_dir, os.path.basename(file) + ".npy"))
    np.save(output_file, tokens)
    return len(tokens)


class TextDataset(IterableDataset):
    def __init__(self, original_files, tokenizer, sequence_length, batch_size, block_length=32,
                 cache_dir="./cache_dir",
                 shuffle_files=True):
        self.block_length = block_length
        self.files = [os.path.join(cache_dir, os.path.basename(f) + ".npy") for f in original_files]
        total_tokens = preprocess_and_save_tokens(original_files, tokenizer, cache_dir)
        self.sequence_length = sequence_length
        self.batch_size = batch_size
        unbatched_length = total_tokens // self.sequence_length
        batches = unbatched_length // self.batch_size
        self._length = batches * self.sequence_length  # discard partial batches
        if shuffle_files:
            random.shuffle(self.files)
        self.shuffle_files = shuffle_files

    def __iter__(self):
        buffer = []
        buffer_length = 0
        sequences_returned = 0

        for file in self.files:
            tokens = np.load(file)
            # tokens = np.load(file, mmap_mode='r')
            file_length = len(tokens)
            start_idx = 0

            while start_idx < file_length:
                # Calculate how many tokens we need to fill the buffer to batch_size
                remaining_space = self.batch_size * self.sequence_length - buffer_length

                # Number of tokens we can take from the current file to fill the buffer
                end_idx = min(start_idx + remaining_space, file_length)

                # Append tokens from file to the buffer
                buffer.extend(tokens[start_idx:end_idx])
                buffer_length += (end_idx - start_idx)
                start_idx = end_idx

                # If the buffer is full, yield the batch
                if buffer_length >= self.batch_size * self.sequence_length:
                    # Split buffer into X (inputs) and Y (targets)
                    result_len = len(buffer) - self.sequence_length
                    if result_len <= 0:
                        continue  # Skip this batch since it doesn't have enough data
                    x = [buffer[i:i + self.sequence_length] for i in range(0, result_len)]
                    y = [buffer[i + 1:i + 1 + self.sequence_length] for i in range(0, result_len)]

                    for i in range(self.batch_size):
                        # Create a mask with all ones (no padding)
                        mask = torch.ones((self.sequence_length,), dtype=torch.bool)
                        # Yield batch as torch tensors
                        yield torch.tensor(x[i], dtype=torch.long), torch.tensor(y[i], dtype=torch.long), mask
                        sequences_returned += 1
                        if sequences_returned == self._length:
                            return

                    # Reset buffer and buffer_length
                    buffer = []
                    buffer_length = 0

    def __len__(self):
        return self._length
