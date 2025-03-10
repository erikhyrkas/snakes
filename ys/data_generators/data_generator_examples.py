import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.ollama_prompter import prompt_ollama


def load_words(file_path='./ys/data_generators/english.txt'):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    random.shuffle(words)
    return words


def generate_example_sentence(word):
    prompt = (
        f"Generate several example sentences using the word '{word}' in different contexts. "
        "Include various meanings and uses of the word if applicable."
    )
    return prompt_ollama(prompt)


def entry_generator() -> Tuple[str, str]:
    words = load_words()

    while True:
        for idx, word in enumerate(words):
            print(f"Generating example sentences {idx + 1} of {len(words)}: {word}")
            examples = generate_example_sentence(word)
            prompt = f"Generate example sentences using the word '{word}'."
            yield  prompt, examples


if __name__ == '__main__':
    generate_training_files_v2("generated-sentences", entry_generator)
