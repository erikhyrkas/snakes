import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.item_loader import file_to_list
from ys.data_generators.util.ollama_prompter import prompt_ollama


def entry_generator() -> Tuple[str, str]:
    foods = file_to_list('foods.txt')
    while True:
        random.shuffle(foods)
        for food in foods:
            prompt = f"Describe the food, animal, or beverage '{food}' in detail, including where it is popular, how it tastes, how it is prepared, common ingredients (if applicable), time of year it is popular (if applicable), and examples of it in a sentence. Then write a short story that includes {food}."
            response = prompt_ollama(prompt)
            yield prompt, response


if __name__ == '__main__':
    generate_training_files_v2("generated-food-stories", entry_generator)
