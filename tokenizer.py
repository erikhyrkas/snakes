import hashlib
import pickle
import string


class SimpleTokenizer:
    def __init__(self):
        self.index_to_word = {}
        self.word_to_index = {}
        self.hash_to_index = {}
        self.current_index = 0
        self.printable_chars = set(string.printable)
        self.vocab_built = False

    @staticmethod
    def _hash(word):
        return int(hashlib.md5(word.encode()).hexdigest(), 16)

    def add_to_vocab(self, word):
        hash_value = self._hash(word)
        if hash_value not in self.hash_to_index:
            self.hash_to_index[hash_value] = self.current_index
            self.index_to_word[self.current_index] = word
            self.word_to_index[word] = self.current_index
            self.current_index += 1

    def to_words(self, text: str):
        result = []
        next_word = ''
        for ch in text:
            if ch not in self.printable_chars:
                continue
            word_end = next_word.isspace() or ch.isspace() or ch in string.punctuation
            if word_end and len(next_word) > 0:
                result.append(next_word)
                if ch == '\n':
                    result.append('<newline>')
                    next_word = ''
                elif ch.isspace():
                    result.append('<space>')
                    next_word = ''
                else:
                    next_word = ch
            else:
                next_word += ch

        if len(next_word) > 0:
            result.append(next_word)
        return result

    # This is sort of the training method
    def build_vocabulary(self, documents: list):
        # Include all printable characters
        for char in self.printable_chars:
            self.add_to_vocab(char)

        # Process additional documents if any
        for document in documents:
            words = self.to_words(document)
            for word in words:
                self.add_to_vocab(word)

        self.vocab_built = True

    def tokenize(self, text):
        tokens = []
        words = self.to_words(text)
        for word in words:
            hash_value = self._hash(word)
            if hash_value in self.hash_to_index:
                tokens.append(self.hash_to_index[hash_value])
            else:
                for ch in word:
                    hash_value = self._hash(ch)
                    if hash_value in self.hash_to_index:
                        tokens.append(self.hash_to_index[hash_value])
                    else:
                        print(f"Character '{ch}' not found in vocabulary.")
        return tokens

    def detokenize(self, tokens):
        text = ''
        for token in tokens:
            word = self.index_to_word[token]
            if word == '<space>':
                text += ' '  # Append a space for '<space>' token
            elif word == '<newline>':
                text += '\n'  # Append a newline for '<newline>' token
            else:
                text += word
        return text

    def vocab_size(self):
        return self.current_index

    def save(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump(
                (self.index_to_word, self.word_to_index, self.hash_to_index, self.current_index, self.vocab_built), f)

    def load(self, filepath):
        with open(filepath, 'rb') as f:
            self.index_to_word, self.word_to_index, self.hash_to_index, self.current_index, self.vocab_built = pickle.load(
                f)


def example_tokenize():
    tokenizer = SimpleTokenizer()
    documents = ["hello world\nthis is a test", "hello there", "break dancing"]  # Include '\n' and spaces
    tokenizer.build_vocabulary(documents)
    tokens = tokenizer.tokenize("hello test world erik")
    print("Tokens:", tokens)
    print("Detokenized:", tokenizer.detokenize(tokens))
    print("Vocab Size:", tokenizer.vocab_size())


if __name__ == "__main__":
    example_tokenize()
