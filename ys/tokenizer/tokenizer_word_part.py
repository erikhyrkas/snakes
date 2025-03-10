import pickle
import re

DEBUG_TOKENIZER = False

REPEAT_ARRAY = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


class Tokenizer:
    def __init__(self):
        self.index_to_word = {}
        self.word_to_index = {}
        self.current_index = 0
        self.initialized = False
        self.special_tokens = ["<upper>", "<shout>", "<start>", "<end>", "<space>", "<newline>", "<pad>",
                               "<nospace>", "<repeata>", "<repeatb>", "<repeatc>", "<repeatd>", "<repeate>",
                               "<repeatf>", "<repeath>", "<repeati>"]
        self.prefix_tokens = [
            ' counter',
            ' hetero', ' contra', ' circum',
            ' extra', ' hyper', ' micro', ' multi', ' retro', ' ultra', ' inter', ' trans', ' super', ' under',
            ' auto', ' homo', ' hypo', ' mono', ' poly', ' post', ' tele', ' semi', ' anti', ' over', ' fore',
            ' mid', ' mal', ' pro', ' syn', ' sym', ' tri', ' dis', ' non', ' mis', ' sub', ' pre', ' con', ' com',
            ' co', ' de', ' ex', ' un', ' re', ' in', ' im', ' il', ' ir', ' en', ' em', ' de', ' bi',
        ]
        self.suffix_tokens = ['itive', 'ative', 'ation', 'ition',
                              'ment', 'ness', 'less', 'able', 'ible', 'tion', 'eous', 'ious',
                              'ting', 'ning', 'bing',
                              'ous', 'ive', 'ity', 'ial', 'est', 'ful', 'ing', 'ion',
                              'ted', 'ned', 'bed',
                              'al', 'ed', 'en', 'er', 'ic', 'ty', 'ly', 'es',
                              's', 'y']

    def _add_to_vocab(self, word):
        if word not in self.word_to_index:
            self.index_to_word[self.current_index] = word
            self.word_to_index[word] = self.current_index
            self.current_index += 1

    def _initialize_vocabulary(self):
        if not self.initialized:
            for token in self.special_tokens:
                self._add_to_vocab(token)
            self._add_to_vocab('_')
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
                self._add_to_vocab(char)

            # Add common Western European accented characters and symbols
            for char in extended_chars:
                self._add_to_vocab(char)

            for prefix in self.prefix_tokens:
                self._add_to_vocab(prefix)

            for suffix in self.suffix_tokens:
                self._add_to_vocab(suffix)

            self.initialized = True

    @staticmethod
    def _detect_repeats(text):
        repeats_replaced = ''
        last_char = ''
        repeat_count = 0

        for char in text:
            if (char.isspace() or not char.isalnum()) and char == last_char:
                repeat_count += 1
                if repeat_count == 10:
                    # If repeat count reaches 10, insert a <repeat-10> token
                    repeats_replaced += f"<repeati>{char}"
                    repeat_count = 0  # Reset repeat count after inserting
            else:
                if repeat_count > 1:
                    repeat_letter = REPEAT_ARRAY[repeat_count - 2]
                    repeats_replaced += f"<repeat{repeat_letter}>{last_char}"
                elif repeat_count == 1:
                    repeats_replaced += last_char
                last_char = char
                repeat_count = 1

        # Append any remaining repeat count
        if repeat_count > 1:
            repeat_letter = REPEAT_ARRAY[repeat_count - 2]
            repeats_replaced += f"<repeat{repeat_letter}>{last_char}"
        elif repeat_count == 1:
            repeats_replaced += last_char

        return repeats_replaced

    def learn_new_vocab(self, document: str):
        if not self.initialized:
            self._initialize_vocabulary()
        words = self.to_words(document)
        for word in words:
            if word not in self.word_to_index:
                self._add_to_vocab(word)

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
        number_regex = r'\d'  # One or more numbers
        symbol_regex = r'[^\w\s]|_'  # Single symbol or punctuation mark

        # Create a combined regex to match all tokens
        combined_regex = f'({space_regex}|{tag_regex}|{all_caps_regex}|{cap_word_regex}|{lower_word_regex}|{single_cap_regex}|{number_regex}|{symbol_regex})'

        # Find all matches using the combined regex
        matches = re.findall(combined_regex, text)

        for match in matches:
            tokens.append(match)

        return tokens

    def to_word_parts(self, text: str):
        lower_space_text = ' ' + text.lower()
        if len(lower_space_text) < 4:
            return [lower_space_text]

        result = []
        for prefix in self.prefix_tokens:
            if lower_space_text.startswith(prefix):
                result.append(prefix)
                lower_space_text = lower_space_text[len(prefix):]
                break

        for suffix in self.suffix_tokens:
            if lower_space_text.endswith(suffix):
                temp_lower_space_text = lower_space_text[:-len(suffix)]
                if len(lower_space_text) > 0:
                    lower_space_text = temp_lower_space_text
                    result.append(lower_space_text)
                    result.append(suffix)
                    break

        if len(result) < 2 and len(lower_space_text) > 0:
            result.append(lower_space_text)
        return result

    def to_words(self, text: str):
        text_no_repeats = self._detect_repeats(text)
        tokens = self._split_text(text_no_repeats)

        result = []
        for token in tokens:
            if not token:
                continue
            if DEBUG_TOKENIZER:
                print(f"Processing token: {token}")
            if '\n' in token:
                result.append('<newline>')
            elif token.isspace():
                for _ in token:
                    result.append('<space>')
            elif token.startswith('<repeat'):
                result.append(token.lower())
            elif re.match(r'<[a-z]+>', token):
                result.append(token)  # tag
            elif re.match(r'[A-Z][A-ZÀ-ß]+', token):
                no_space = len(result) == 0 or result[-1] != '<space>'
                if not no_space:
                    result.pop()
                result.append('<shout>')
                if no_space:
                    result.append('<nospace>')
                result.extend(self.to_word_parts(token))
            elif re.match(r'[A-Z][a-zà-ÿ]*', token):
                no_space = len(result) == 0 or result[-1] != '<space>'
                if not no_space:
                    result.pop()
                result.append('<upper>')
                if no_space:
                    result.append('<nospace>')
                result.extend(self.to_word_parts(token))
            elif re.match(r'[a-zà-ÿ]+', token):
                no_space = len(result) == 0 or result[-1] != '<space>'
                if no_space:
                    result.append('<nospace>')
                else:
                    result.pop()
                result.extend(self.to_word_parts(token))
            elif re.match(r'[A-ZÀ-ß]', token):
                no_space = len(result) == 0 or result[-1] != '<space>'
                if no_space:
                    result.append('<nospace>')
                else:
                    result.pop()
                result.extend(self.to_word_parts(token))
            else:
                result.append(token)

        if DEBUG_TOKENIZER:
            print(f"Final token list: {result}")
        return result

    def encode(self, text):
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

    def tokens_to_words(self, tokens):
        words = []
        for token in tokens:
            word = self.index_to_word[token]
            words.append(word)
        return words

    def decode(self, tokens):
        text = ''
        capitalize_next = False
        shout_next = False
        repeat_next = 1
        no_space = False
        for token in tokens:
            word = self.index_to_word[token]
            if word == '<nospace>':
                no_space = True
            elif word == '<repeata>':
                repeat_next = 2
            elif word == '<repeatb>':
                repeat_next = 3
            elif word == '<repeatc>':
                repeat_next = 4
            elif word == '<repeatd>':
                repeat_next = 5
            elif word == '<repeate>':
                repeat_next = 6
            elif word == '<repeatf>':
                repeat_next = 7
            elif word == '<repeatg>':
                repeat_next = 8
            elif word == '<repeath>':
                repeat_next = 9
            elif word == '<repeati>':
                repeat_next = 10
            elif word == '<space>':
                for _ in range(repeat_next):
                    text += ' '
                repeat_next = 1
            elif word == '<newline>':
                for _ in range(repeat_next):
                    text += '\n'
                repeat_next = 1
            elif word == '<upper>':
                capitalize_next = True
            elif word == '<shout>':
                shout_next = True
            elif word == '_':
                for _ in range(repeat_next):
                    text += '_'
                repeat_next = 1
            elif word in self.special_tokens:
                continue  # Skip rendering of standalone special tokens
            else:
                if no_space:
                    word = word.strip()
                    no_space = False
                if capitalize_next:
                    if word[0].isspace():
                        word = ' ' + (word.strip()).capitalize()
                    else:
                        word = word.capitalize()
                    capitalize_next = False
                if shout_next:
                    word = word.upper()
                    shout_next = False

                if repeat_next > 1:
                    for _ in range(repeat_next):
                        text += word[0]
                    next_part = word[1:]
                    text += next_part
                else:
                    text += word
                repeat_next = 1
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
            print(f"Tokenizer vocabulary size: {self.vocab_size():,}")

    def print_vocabulary(self):
        print(self.word_to_index)
        print(f"Tokenizer vocabulary size: {self.vocab_size():,}")

    def get_end_token(self):
        if not self.initialized:
            self._initialize_vocabulary()
        return self.word_to_index['<end>']

    def get_start_token(self):
        if not self.initialized:
            self._initialize_vocabulary()
        return self.word_to_index['<start>']

    def get_pad_token(self):
        if not self.initialized:
            self._initialize_vocabulary()
        return self.word_to_index['<pad>']


def example_tokenize():
    tokenizer = Tokenizer()
    documents = ["Hello world\nthis is a Test", "Hello there", "break <start>dancing<end><start>"]
    for document in documents:
        tokenizer.learn_new_vocab(document)
    tokens = tokenizer.encode("hello 1980 <start>Test ërik's world<start><end> <html> Erik<start>")
    print("Tokens:", tokens)
    print("Decoded:", tokenizer.decode(tokens))
    print(f"Vocab Size: {tokenizer.vocab_size():,}")
    tokenizer.print_vocabulary()


def run_tokenizer_tests():
    tokenizer = Tokenizer()
    test_cases = [
        ("rebasing and understanding", ['<nospace>', ' re', 'bas', 'ing', ' and', ' under', 'stand', 'ing']),
        ("LaSalle is a great example of camelCase splitting.",
         ['<upper>', '<nospace>', ' la', '<upper>', '<nospace>', ' salle', ' is', ' a', ' great', ' ex', 'ample', ' of', ' camel', '<upper>', '<nospace>', ' case', ' split', 'ting', '.']),
        ("The quick brown fox jumps over the lazy dog.",
         ['<upper>', '<nospace>', ' the', ' quick', ' brown', ' fox', ' jump', 's', ' over', ' the', ' laz', 'y', ' dog', '.']),
        ("Jalapeño is a spicy pepper! Do you like Piña colada?",
         ['<upper>', '<nospace>', ' jalapeño', ' is', ' a', ' spicy', ' pepper', '!', '<upper>', ' do', ' you', ' like',
          '<upper>', ' piña', ' colada', '?']),
        ("THIS IS AN ALL CAPS SENTENCE.",
         ['<shout>', '<nospace>', ' this', '<shout>', ' is', '<shout>', ' an', '<shout>', ' all', '<shout>', ' caps',
          '<shout>', ' sentence', '.']),
        ("Under_score and CamelCase mixed together.",
         ['<upper>', '<nospace>', ' under', '_', '<nospace>', ' score', ' and', '<upper>', ' camel', '<upper>',
          '<nospace>', ' case', ' mixed', ' together', '.']),
        ("1234 numbers and symbols *&^%$#@! are tricky.",
         ['1', '2', '3', '4', ' numbers', ' and', ' symbols', '<space>', '*', '&', '^', '%', '$', '#', '@', '!', ' are',
          ' tricky', '.']),
        ("_Meet the new *Star* player of the team.",
         ['_', '<upper>', '<nospace>', ' meet', ' the', ' new', '<space>', '*', '<upper>', '<nospace>', ' star', '*',
          ' player', ' of', ' the', ' team', '.']),
        ("eCommerce is the future of onlineShopping.",
         ['<nospace>', ' e', '<upper>', '<nospace>', ' commerce', ' is', ' the', ' future', ' of', ' online', '<upper>',
          '<nospace>', ' shopping', '.']),
        ("hello <start>Test world<end> Erik<start>",
         ['<nospace>', ' hello', '<space>', '<start>', '<upper>', '<nospace>', ' test', ' world', '<end>', '<upper>',
          ' erik', '<start>']),
        ("The symbol € is a UTF-8 character, as is ™.",
         ['<upper>', '<nospace>', ' the', ' symbol', '<space>', '€', ' is', ' a', '<shout>', ' utf', '-', '8',
          ' character', ',', ' as', ' is', '<space>', '™', '.']),
        ("JSON-like: {'key': 'value', 'number': 1001}",
         ['<shout>', '<nospace>', ' json', '-', '<nospace>', ' like', ':', '<space>', '{', "'", '<nospace>', ' key',
          "'", ':', '<space>', "'", '<nospace>', ' value', "'", ',', '<space>', "'", '<nospace>', ' number', "'", ':',
          '<space>', '1', '0', '0', '1', '}']),
        ("Math symbols: 2 * 3 = 6 and a^2 + b^2 = c^2.",
         ['<upper>', '<nospace>', ' math', ' symbols', ':', '<space>', '2', '<space>', '*', '<space>', '3', '<space>',
          '=', '<space>', '6', ' and', ' a', '^', '2', '<space>', '+', ' b', '^', '2', '<space>', '=', ' c', '^', '2',
          '.']),
        ("The 1980s were fun but I came in 43th place in my race.",
         ['<upper>', '<nospace>', ' the', '<space>', '1', '9', '8', '0', '<nospace>', ' s', ' were', ' fun', ' but',
          '<upper>', ' i', ' came', ' in', '<space>', '4', '3', '<nospace>', ' th', ' place', ' in', ' my', ' race',
          '.']),
        ("Can you write a blog post for me?<start>Here's a post for you.<end>",
         ['<upper>', '<nospace>', ' can', ' you', ' write', ' a', ' blog', ' post', ' for', ' me', '?', '<start>',
          '<upper>', '<nospace>', ' here', "'", '<nospace>', ' s', ' a', ' post', ' for', ' you', '.', '<end>']),
        ("  Python  needs  spaces.   So, let's give it   spaces    .",
         ['<repeata>', '<upper>', ' python', '<repeata>', ' needs', '<repeata>', ' spaces', '.', '<repeatb>', '<upper>',
          ' so', ',', ' let', "'", '<nospace>', ' s', ' give', ' it', '<repeatb>', ' spaces', '<repeatc>', '<space>',
          '.']),
        ("<pad><pad><pad><pad><pad><pad><pad><pad><pad><pad><pad><pad>",
         ['<pad>', '<pad>', '<pad>', '<pad>', '<pad>', '<pad>', '<pad>', '<pad>', '<pad>', '<pad>', '<pad>', '<pad>']),
        ("Erik is testing padding.<pad><pad><pad><pad>",
         ['<upper>', '<nospace>', ' erik', ' is', ' testing', ' padding', '.', '<pad>', '<pad>', '<pad>', '<pad>']),
        ("<start><start><start><start><start>", ['<start>', '<start>', '<start>', '<start>', '<start>']),
        ("<end><end><end><end><end><end>", ['<end>', '<end>', '<end>', '<end>', '<end>', '<end>']),
        ("a-a", ['<nospace>', ' a', '-', '<nospace>', ' a']),
        ("a--a", ['<nospace>', ' a', '<repeata>', '-', '<nospace>', ' a']),
        ("a---a", ['<nospace>', ' a', '<repeatb>', '-', '<nospace>', ' a']),
        ("a----a", ['<nospace>', ' a', '<repeatc>', '-', '<nospace>', ' a']),
        ("a-----a", ['<nospace>', ' a', '<repeatd>', '-', '<nospace>', ' a']),
        ("a------a", ['<nospace>', ' a', '<repeate>', '-', '<nospace>', ' a']),
        ("a-------a", ['<nospace>', ' a', '<repeatf>', '-', '<nospace>', ' a']),
        ("a--------a", ['<nospace>', ' a', '<repeatg>', '-', '<nospace>', ' a']),
        ("a---------a", ['<nospace>', ' a', '<repeath>', '-', '<nospace>', ' a']),
        ("a----------a", ['<nospace>', ' a', '<repeati>', '-', '<nospace>', ' a']),
        ("a-----------a", ['<nospace>', ' a', '<repeati>', '-', '-', '<nospace>', ' a']),
        ("a-----abc------a",
         ['<nospace>', ' a', '<repeatd>', '-', '<nospace>', ' abc', '<repeate>', '-', '<nospace>', ' a']),
        ("a     abc  a", ['<nospace>', ' a', '<repeatd>', ' abc', '<repeata>', ' a']),
        ("            def my_py_func(x):\n            def something_func(x):\n              x += 2",
         ['<repeati>', '<space>', '<repeata>', ' def', ' my', '_', '<nospace>', ' py', '_', '<nospace>', ' func', '(',
          '<nospace>', ' x', ')', ':', '<newline>', '<repeati>', '<space>', '<repeata>', ' def', ' something', '_',
          '<nospace>', ' func', '(', '<nospace>', ' x', ')', ':', '<newline>', '<repeati>', '<space>', '<repeatc>',
          ' x', '<space>', '+', '=', '<space>', '2']),
        ("  def something():\n    pass",
         ['<repeata>', ' def', ' something', '(', ')', ':', '<newline>', '<repeatc>', ' pass']),
        ("999 888 675 432 1090 1 2 3 4",
         ['9', '9', '9', '<space>', '8', '8', '8', '<space>', '6', '7', '5', '<space>', '4', '3', '2', '<space>', '1',
          '0', '9', '0', '<space>', '1', '<space>', '2', '<space>', '3', '<space>', '4'])
    ]

    tokenizer.get_pad_token()
    for test_case in test_cases:
        test = test_case[0]
        tokenizer.learn_new_vocab(test)

    for idx, test_case in enumerate(test_cases):
        test = test_case[0]
        expected_tokens = test_case[1]
        print(f"Test Case {idx + 1}:")
        print(f"Original: |{test}|")
        tokens = tokenizer.encode(test)
        print(f"Tokens: {tokens}")
        decode_text = tokenizer.decode(tokens)
        print(f"Decoded: |{decode_text}|")
        token_words = tokenizer.tokens_to_words(tokens)
        print(f"Tokens as Words: {token_words}")
        print(f"Expected: {expected_tokens}")
        assert token_words == expected_tokens
        print("-" * 80)


if __name__ == "__main__":
    example_tokenize()
    run_tokenizer_tests()
