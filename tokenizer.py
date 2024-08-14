import re
import pickle

DEBUG_TOKENIZER = False


class SimpleTokenizer:
    def __init__(self):
        self.index_to_word = {}
        self.word_to_index = {}
        self.current_index = 0
        self.initialized = False
        self.special_tokens = ["<upper>", "<shout>", "<start>", "<end>", "<space>", "<newline>"]

    def add_to_vocab(self, word):
        if word not in self.word_to_index:
            self.index_to_word[self.current_index] = word
            self.word_to_index[word] = self.current_index
            self.current_index += 1

    def _initialize_vocabulary(self):
        if not self.initialized:
            for token in self.special_tokens:
                self.add_to_vocab(token)
            self.add_to_vocab('_')
            # Note:
            # We have to keep the model small, and there's no intention
            # of being exclusionary, but I have to focus on the text that I know.
            # If you are taking and modifying this code, I highly recommend
            # streamlining this for the language you will train on and use.
            # I don't have the money to train a model that can handle all languages.

            # Initialize single-letter printable tokens for basic ASCII and common Western European characters
            ascii_range = list(range(32, 127))  # Basic printable ASCII
            extended_chars = [
                'é', 'è', 'ê', 'ë', 'à', 'á', 'â', 'ä', 'å', 'ç', 'ì', 'í', 'î', 'ï',
                'ñ', 'ò', 'ó', 'ô', 'ö', 'ù', 'ú', 'û', 'ü', 'ý', 'ÿ', 'ø', 'å', 'Æ',
                'æ', 'œ', 'ß', 'ñ', '¿', '¡', '€', '£'
            ]
            extended_chars += [char.upper() for char in extended_chars if char.islower()]

            # Add ASCII characters to vocabulary
            for i in ascii_range:
                char = chr(i)
                self.add_to_vocab(char)

            # Add common Western European accented characters and symbols
            for char in extended_chars:
                self.add_to_vocab(char)

            self.initialized = True

    def append_to_vocab(self, document: str):
        if not self.initialized:
            self._initialize_vocabulary()
        words = self.to_words(document)
        for word in words:
            if word not in self.word_to_index:
                self.add_to_vocab(word)

    @staticmethod
    def _split_text(text):
        tokens = []

        # Define the regular expressions for the tokens, ordered by priority
        space_regex = r'\s+'  # One or more spaces
        tag_regex = r'<[a-z]+>'  # <lowercase letters>
        cap_word_regex = r'[A-Z][a-zà-ÿ]*'  # Capital followed by lowercase, including accented characters
        all_caps_regex = r'[A-Z][A-ZÀ-ß]+'  # All capital letters in a row, including accented uppercase characters
        lower_word_regex = r'[a-zà-ÿ]+'  # One or more lowercase letters, including accented characters
        single_cap_regex = r'[A-ZÀ-ß]'  # A single capital word (like 'A' or accented capital)
        number_regex = r'\d+'  # One or more numbers
        symbol_regex = r'[^\w\s]|_'  # Single symbol or punctuation mark

        # Create a combined regex to match all tokens
        combined_regex = f'({space_regex}|{tag_regex}|{cap_word_regex}|{all_caps_regex}|{lower_word_regex}|{single_cap_regex}|{number_regex}|{symbol_regex})'

        # Find all matches using the combined regex
        matches = re.findall(combined_regex, text)

        for match in matches:
            tokens.append(match)

        return tokens

    def to_words(self, text: str):
        tokens = self._split_text(text)

        result = []
        for token in tokens:
            if not token:
                continue
            if DEBUG_TOKENIZER:
                print(f"Processing token: {token}")  # Debugging statement
            if '\n' in token:
                result.append('<newline>')
            elif token.isspace():
                result.append('<space>')
            elif re.match(r'<[a-z]+>', token):
                result.append(token)  # tag
            elif re.match(r'[A-Z][a-zà-ÿ]*', token):
                result.append('<upper>')
                result.append(token.lower())
            elif re.match(r'[A-Z][A-ZÀ-ß]+', token):
                result.append('<shout>')
                result.append(token.lower())
            elif re.match(r'[a-zà-ÿ]+', token):
                result.append(token)
            elif re.match(r'[A-ZÀ-ß]', token):
                result.append(token.lower())
            else:
                result.append(token)

        if DEBUG_TOKENIZER:
            print(f"Final token list: {result}")  # Debugging statement
        return result

    def tokenize(self, text):
        if not self.initialized:
            self._initialize_vocabulary()
        tokens = []
        words = self.to_words(text)
        for word in words:
            if word in self.word_to_index:
                tokens.append(self.word_to_index[word])
            else:
                if DEBUG_TOKENIZER:
                    print(f"Word '{word}' not found in vocabulary. Using individual characters.")
                for letter in word:
                    if letter in self.word_to_index:
                        tokens.append(self.word_to_index[letter])
                    elif DEBUG_TOKENIZER:
                        print(f"Character '{letter}' wasn't in vocabulary. Skipping!")
        return tokens

    def detokenize(self, tokens):
        text = ''
        capitalize_next = False
        shout_next = False
        for token in tokens:
            word = self.index_to_word[token]
            if word == '<space>':
                text += ' '
            elif word == '<newline>':
                text += '\n'
            elif word == '<upper>':
                capitalize_next = True
            elif word == '<shout>':
                shout_next = True
            elif word == '_':
                text += '_'
            elif word in self.special_tokens:
                continue  # Skip rendering of standalone special tokens
            else:
                if capitalize_next:
                    word = word.capitalize()
                    capitalize_next = False
                if shout_next:
                    word = word.upper()
                    shout_next = False
                text += word
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
        if DEBUG_TOKENIZER:
            print("Tokenizer vocabulary size: ", self.vocab_size())

    def print_vocabulary(self):
        print(self.word_to_index)
        print("Tokenizer vocabulary size: ", self.vocab_size())

    def get_end_token(self):
        if not self.initialized:
            self._initialize_vocabulary()
        return self.word_to_index['<end>']

    def get_start_token(self):
        if not self.initialized:
            self._initialize_vocabulary()
        return self.word_to_index['<start>']


def example_tokenize():
    tokenizer = SimpleTokenizer()
    documents = ["Hello world\nthis is a Test", "Hello there", "break <start>dancing<end><start>"]
    for document in documents:
        tokenizer.append_to_vocab(document)
    tokens = tokenizer.tokenize("hello 1980 <start>Test ërik's world<start><end> <html> Erik<start>")
    print("Tokens:", tokens)
    print("Detokenized:", tokenizer.detokenize(tokens))
    print("Vocab Size:", tokenizer.vocab_size())
    tokenizer.print_vocabulary()


def run_tokenizer_tests():
    tokenizer = SimpleTokenizer()
    test_cases = [
        "LaSalle is a great example of camelCase splitting.",
        "The quick brown fox jumps over the lazy dog.",
        "Jalapeño is a spicy pepper! Do you like Piña colada?",
        "THIS IS AN ALL CAPS SENTENCE.",
        "Under_score and CamelCase mixed together.",
        "1234 numbers and symbols *&^%$#@! are tricky.",
        "_Meet the new *Star* player of the team.",
        "eCommerce is the future of onlineShopping.",
        "hello <start>Test world<end> Erik<start>",
        "The symbol € is a UTF-8 character, as is ™.",
        "JSON-like: {'key': 'value', 'number': 1001}",
        "Math symbols: 2 * 3 = 6 and a^2 + b^2 = c^2.",
        "The 1980s were fun but I came in 43th place in my race.",
        "Can you write a blog post for me?<start>Here's a post for you.<end>",
    ]

    for idx, test in enumerate(test_cases):
        print(f"Test Case {idx + 1}:")
        print(f"Original: {test}")
        tokens = tokenizer.tokenize(test)
        print(f"Tokens: {tokens}")
        detokenized_text = tokenizer.detokenize(tokens)
        print(f"Detokenized: {detokenized_text}")
        print("-" * 80)


if __name__ == "__main__":
    example_tokenize()
    run_tokenizer_tests()
