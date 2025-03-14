import random
from typing import Tuple

from ys.data_generators.data_generator_names import load_items
from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.ollama_prompter import prompt_ollama


def entry_generator() -> Tuple[str, str]:
    main_characters = load_items('./ys/data_generators/names.txt')

    while True:
        all_titles = dict()
        for name in main_characters:
            titles_string = prompt_ollama(
                f"Provide a comma delimited list of 20 titles for campfire stories about a person named {name}. Do not use titles of real books or stories, invent new titles that don't exist. Do not make another other comments or acknowledgements.")
            print(f"Name: {name}")
            print(f"Titles: {titles_string}")
            for title in titles_string.split(','):
                all_titles[title.strip()] = name

        all_titles_shuffled_keys = list(all_titles.keys())
        random.shuffle(all_titles_shuffled_keys)
        for title in all_titles_shuffled_keys:
            name = all_titles[title].lower()
            base_prompt = f"Tell a campfire story called `{title}`."
            script = prompt_ollama(f"{base_prompt} The main character's name is `{name}`. Do not make another other comments or acknowledgements.")

            yield base_prompt, script


if __name__ == '__main__':
    generate_training_files_v2("generated-campfire", entry_generator)
