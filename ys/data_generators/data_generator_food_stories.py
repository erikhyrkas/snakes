from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files
from ys.data_generators.util.item_loader import file_to_list
from ys.data_generators.util.ollama_prompter import prompt_ollama


def entry_generator() -> Tuple[int, str, str]:
    foods = file_to_list('foods.txt')
    file_number: int = 0
    index = 0
    for food in foods:
        prompt = f"Describe the food, animal, or beverage '{food}' in detail, including where it is popular, how it tastes, how it is prepared, common ingredients (if applicable), time of year it is popular (if applicable), and examples of it in a sentence. Then write a short story that includes {food}."
        response = prompt_ollama(prompt)

        if index % 100 == 0:
            file_number = file_number + 1
        index += 1
        yield file_number, prompt, response


if __name__ == '__main__':
    generate_training_files("generated-food-stories", entry_generator)
