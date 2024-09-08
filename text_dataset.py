import os
import numpy as np
import torch
from torch.utils.data import IterableDataset
import random


class TextDataset(IterableDataset):
    def __init__(self, files, tokenizer, sequence_length, batch_size, cache_dir="./cache_dir", shuffle_files=True):
        self.sequence_length = sequence_length
        self.batch_size = batch_size
        self.files = files
        self.tokenizer = tokenizer
        self.cache_dir = cache_dir
        self.shuffle_files = shuffle_files

        # Ensure cache directory exists
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

        # Preprocess and cache tokens
        self.cached_files = [self._cache_file(file) for file in self.files]

        # Shuffle files if required
        if self.shuffle_files:
            random.shuffle(self.cached_files)

        # Precompute the length
        self._length = self._precompute_length()
        self.mask = torch.ones((self.sequence_length,), dtype=torch.bool)


    def _cache_file(self, file):
        """Tokenize and cache the file if not already cached."""
        cached_file = os.path.join(self.cache_dir, os.path.basename(file) + ".npy")
        if not os.path.exists(cached_file):
            with open(file, 'r', encoding='utf-8') as f:
                text = f.read()
            tokens = self.tokenizer.encode(text)

            # Save tokens to the cache
            np.save(cached_file, np.array(tokens, dtype=np.int32))
        return cached_file

    def _precompute_length(self):
        """Precompute the total number of sequences available."""
        total_tokens = sum(len(np.load(cached_file, mmap_mode='r')) for cached_file in self.cached_files)
        total_sequences = (total_tokens - self.sequence_length) // self.sequence_length
        return total_sequences - (total_sequences % self.batch_size)  # Discard partial batches

    def __len__(self):
        return self._length

    def __iter__(self):
        buffer = []
        buffer_length = 0
        sequences_returned = 0
        sequences_in_current_batch = 0

        for file in self.cached_files:
            tokens = np.load(file, mmap_mode='r')
            file_length = len(tokens)
            start_idx = 0

            while start_idx < file_length:
                # Calculate how many tokens we need to fill the buffer
                #remaining_space = (self.batch_size * self.sequence_length + self.sequence_length) - buffer_length
                remaining_space = (self.batch_size * self.sequence_length) - buffer_length

                # Number of tokens we can take from the current file to fill the buffer
                end_idx = min(start_idx + remaining_space, file_length)

                # Append tokens from file to the buffer
                buffer.extend(tokens[start_idx:end_idx])
                buffer_length += (end_idx - start_idx)
                start_idx = end_idx

                # If the buffer has enough tokens, yield sequences
                while buffer_length >= self.sequence_length + 1:
                    if sequences_returned >= self._length:
                        return

                    x = torch.tensor(buffer[:self.sequence_length], dtype=torch.long)
                    y = torch.tensor(buffer[1:self.sequence_length + 1], dtype=torch.long)

                    yield x, y, self.mask

                    sequences_returned += 1
                    sequences_in_current_batch += 1

                    # If we've completed a batch, reset the counter
                    if sequences_in_current_batch == self.batch_size:
                        sequences_in_current_batch = 0

                    # Remove used tokens from buffer
                    buffer = buffer[self.sequence_length:]
                    buffer_length -= self.sequence_length

        # # Ensure we don't yield a partial batch at the end
        # if sequences_in_current_batch > 0:
        #     remaining_sequences = self.batch_size - sequences_in_current_batch
        #     for _ in range(remaining_sequences):
        #         sequences_returned -= 1

        # Discard any remaining tokens that don't make a full sequence