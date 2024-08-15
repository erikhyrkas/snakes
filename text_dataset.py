import random
import torch
from torch.utils.data import IterableDataset


class TextDataset(IterableDataset):
    def __init__(self, files, tokenizer, training_sequence_length, shuffle_files=True):
        self.files = files
        self.tokenizer = tokenizer
        self.training_sequence_length = training_sequence_length
        self._length = None
        if shuffle_files:
            random.shuffle(self.files)

    def __iter__(self):
        for file in self.files:
            with open(file, 'r', encoding='utf-8') as f:
                text = f.read()
                tokens = self.tokenizer.tokenize(text)
                for i in range(0, len(tokens) - self.training_sequence_length, self.training_sequence_length):
                    x = tokens[i:i + self.training_sequence_length]
                    y = tokens[i + 1:i + 1 + self.training_sequence_length]
                    yield torch.tensor(x, dtype=torch.long), torch.tensor(y, dtype=torch.long)

    def __len__(self):
        if self._length is None:
            # Calculate the length by iterating through the dataset
            count = 0
            for file in self.files:
                with open(file, 'r', encoding='utf-8') as f:
                    text = f.read()
                    tokens = self.tokenizer.tokenize(text)
                    count += len(tokens) // self.training_sequence_length
            self._length = count
        return self._length
