import random

import torch
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import IterableDataset
import os


class FineTuningDataset(IterableDataset):
    def __init__(self, directory, tokenizer, shuffle_files=True):
        self.directory = directory
        self.tokenizer = tokenizer
        self.pad_token_id = tokenizer.get_pad_token()
        self.files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')]
        self._length = None
        if shuffle_files:
            random.shuffle(self.files)

    def __iter__(self):
        for file_path in self.files:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read().strip()
            items = [item + '<end>' for item in text.split('<end>') if item.strip()]

            tokenized_items = [torch.tensor(self.tokenizer.tokenize(item), dtype=torch.long) for item in items]
            if len(tokenized_items) == 0:
                continue

            padded_items = pad_sequence(tokenized_items, batch_first=True, padding_value=self.pad_token_id)
            masks = (padded_items != self.pad_token_id).type(torch.bool)

            for i in range(padded_items.shape[0]):
                x = padded_items[i][:-1]
                y = padded_items[i][1:]
                mask = masks[i][:-1]
                yield x, y, mask

    def __len__(self):
        if self._length is None:
            total_sequences = 0
            for file_path in self.files:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                # Counting the number of <end> tags as each represents the end of a record
                total_sequences += text.count('<end>')
                self._length = total_sequences
        return self._length
