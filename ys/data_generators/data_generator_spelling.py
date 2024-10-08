import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files
from ys.data_generators.util.item_loader import file_to_list


def entry_generator() -> Tuple[int, str, str]:
    english = file_to_list('english.txt')
    names = file_to_list('names.txt')
    foods = file_to_list('foods.txt')
    file_number: int = 0
    index = 0
    words: set[str] = set[str](english)
    words.update(names)
    words.update(foods)
    if '' in words:
        words.remove('')
    for word in words:
        prompt = random.choice([f"Spell {word}.",
                                f"Spell the word {word}.",
                                f"How do you spell {word}?",
                                f"How is {word} spelled?"])

        word_lower = word.lower()
        random_letter = random.choice(word_lower)
        letter_count = word.count(random_letter)
        prompt += "\n"
        prompt += random.choice([f"How many {random_letter}'s are in {word}?",
                                 f"How many times does {random_letter} appear in {word}?",
                                 f"Count the {random_letter}'s in {word}."])
        response = ""
        delim = ""
        for letter in word:
            response += delim + letter.upper()
            delim = "-"

        response += f'\nThe letter {random_letter} is found {letter_count} times.'

        if index % 1000 == 0:
            file_number = file_number + 1
        index += 1
        yield file_number, prompt, response


if __name__ == '__main__':
    generate_training_files("generated-spelling", entry_generator)
