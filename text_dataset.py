import random
from functools import lru_cache

from torch.utils.data import IterableDataset
import torch


class TextDataset(IterableDataset):
    def __init__(self, files, tokenizer, training_sequence_length, shuffle_files=True):
        self.files = files
        self.tokenizer = tokenizer
        self.training_sequence_length = training_sequence_length
        self._length = None
        if shuffle_files:
            random.shuffle(self.files)
        # Pre-initialize the mask as all ones, since there's no padding and all data points are valid
        self.mask = torch.ones((training_sequence_length,), dtype=torch.bool)

    def __iter__(self):
        for file in self.files:
            with open(file, 'r', encoding='utf-8') as f:
                text = f.read()
                tokens = self.tokenizer.tokenize(text)
                for i in range(0, len(tokens) - self.training_sequence_length, self.training_sequence_length):
                    x = tokens[i:i + self.training_sequence_length]
                    y = tokens[i + 1:i + 1 + self.training_sequence_length]
                    # Yield the pre-initialized mask with each sequence
                    yield torch.tensor(x, dtype=torch.long), torch.tensor(y, dtype=torch.long), self.mask

    def __len__(self):
        if self._length is None:
            count = 0
            for file in self.files:
                count = self.file_to_tensors(count, file)
            self._length = count
        return self._length

    @lru_cache(maxsize=None)
    def file_to_tensors(self, count, file):
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
        tokens = self.tokenizer.tokenize(text)
        # Calculate complete sequences only
        complete_batches = len(tokens) // self.training_sequence_length
        count += complete_batches
        return count
