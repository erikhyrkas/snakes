import random
import torch
from torch.utils.data import IterableDataset


class TextDataset(IterableDataset):
    def __init__(self, files, tokenizer, context_length, shuffle_files=True):
        self.files = files
        self.tokenizer = tokenizer
        self.context_length = context_length
        self._length = None
        if shuffle_files:
            random.shuffle(self.files)

    def __iter__(self):
        for file in self.files:
            with open(file, 'r', encoding='utf-8') as f:
                text = f.read()
                tokens = self.tokenizer.tokenize(text)
                for i in range(0, len(tokens) - self.context_length, self.context_length):
                    x = tokens[i:i + self.context_length]
                    y = tokens[i + 1:i + 1 + self.context_length]
                    yield torch.tensor(x, dtype=torch.long), torch.tensor(y, dtype=torch.long)

    def __len__(self):
        if self._length is None:
            # Calculate the length by iterating through the dataset
            count = 0
            for file in self.files:
                with open(file, 'r', encoding='utf-8') as f:
                    text = f.read()
                    tokens = self.tokenizer.tokenize(text)
                    count += len(tokens) // self.context_length
            self._length = count
        return self._length
