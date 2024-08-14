import pickle
import string


class SimpleTokenizer:
    def __init__(self):
        self.index_to_word = {}
        self.word_to_index = {}
        self.current_index = 0
        self.printable_chars = set(string.printable)
        self.initialized = False

    def add_to_vocab(self, word):
        if word not in self.word_to_index:
            self.index_to_word[self.current_index] = word
            self.word_to_index[word] = self.current_index
            self.current_index += 1

    def to_words(self, text: str):
        result = []
        next_word = ''
        for ch in text:
            if ch not in self.printable_chars:
                continue
            is_punc = ch in string.punctuation
            word_end = next_word.isspace() or ch.isspace() or ch.isupper() or is_punc
            if word_end:
                if len(next_word) > 0:
                    if next_word.startswith('<'):
                        if ch == '>':
                            next_word += ch
                            ch = ''
                        elif len(next_word) > 1:
                            result.append('<')
                            next_word = next_word[1:]
                    result.append(next_word)
                if ch == '\n':
                    result.append('<newline>')
                    next_word = ''
                elif ch.isspace():
                    result.append('<space>')
                    next_word = ''
                elif ch.isupper():
                    result.append('<upper>')
                    next_word = ch.lower()
                elif ch != '<' and ch in string.punctuation:
                    if len(ch) > 0:
                        result.append(ch)
                    next_word = ''
                else:
                    next_word = ch
            else:
                next_word += ch

        if len(next_word) > 0:
            result.append(next_word)

        if '' in result:
            raise ValueError("Empty value found in tokenizer")
        # print(result)
        return result

    # This is sort of the training method
    def _initialize_vocabulary(self):
        if not self.initialized:
            self.add_to_vocab('<start>')
            self.add_to_vocab('<end>')
            self.add_to_vocab('<space>')
            self.add_to_vocab('<newline>')
            self.add_to_vocab('<upper>')
            # Include all printable characters
            for char in self.printable_chars:
                self.add_to_vocab(char)
            self.initialized = True

    def append_documents_to_vocabulary(self, documents: list):
        for document in documents:
            self.append_to_vocab(document)

    def append_to_vocab(self, document: str):
        if not self.initialized:
            self._initialize_vocabulary()
        words = self.to_words(document)
        for word in words:
            self.add_to_vocab(word)

    def get_end_token(self) -> int:
        if not self.initialized:
            self._initialize_vocabulary()
        return self.word_to_index['<end>']

    def print_vocabulary(self):
        print(self.word_to_index)

    def tokenize(self, text):
        tokens = []
        words = self.to_words(text)
        for word in words:
            if word in self.word_to_index:
                val = self.word_to_index[word]
                if val:
                    tokens.append(val)
            else:
                for ch in word:
                    if ch in self.word_to_index:
                        val = self.word_to_index[ch]
                        if val:
                            tokens.append(val)
                    else:
                        print(f"Character '{ch}' not found in vocabulary.")
        return tokens

    def detokenize(self, tokens):
        text = ''
        capitalize_next = False
        for token in tokens:
            word = self.index_to_word[token]
            if word == '<space>':
                text += ' '  # Append a space for '<space>' token
            elif word == '<newline>':
                text += '\n'  # Append a newline for '<newline>' token
            elif word == '<upper>':
                capitalize_next = True
            else:
                if capitalize_next:
                    capitalize_next = False
                    word = word.capitalize()
                text += word
        if capitalize_next:
            text += '<upper>'
        return text

    def vocab_size(self):
        return self.current_index

    def save(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump(
                (self.index_to_word, self.word_to_index, self.current_index, self.initialized), f)

    def load(self, filepath):
        with open(filepath, 'rb') as f:
            self.index_to_word, self.word_to_index, self.current_index, self.initialized = pickle.load(f)
        print("Tokenizer vocabulary size: ", self.vocab_size())


def example_tokenize():
    tokenizer = SimpleTokenizer()
    documents = ["Hello world\nthis is a Test", "Hello there", "break <start>dancing<end><start>"]
    tokenizer.append_documents_to_vocabulary(documents)
    tokens = tokenizer.tokenize("hello <start>Test world<start><end> Erik<start>")
    print("Tokens:", tokens)
    print("Detokenized:", tokenizer.detokenize(tokens))
    print("Vocab Size:", tokenizer.vocab_size())
    tokenizer.print_vocabulary()


if __name__ == "__main__":
    example_tokenize()
