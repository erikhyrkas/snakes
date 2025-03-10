import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files
from ys.data_generators.util.ollama_prompter import prompt_ollama


def entry_generator() -> Tuple[int, str, str]:
    genres = [
        "Drama",
        "Comedy",
        "Fantasy",
        "Science Fiction",
        "Mystery",
        "Action/Adventure",
        "Historical Fiction",
        "Romance",
        "Crime",
        "Superhero",
        "Western",
        "Anthology",
        "Slice of Life",
        "Epic",
    ]
    file_number: int = 0
    index = 0
    for _ in range(2800):
        all_titles = dict()
        for genre in genres:
            lower_genre = genre.lower()
            titles_string = prompt_ollama(
                f"Provide a comma delimited list of 20 titles for audiobooks in the {lower_genre} genre. Do not use titles of real books, invent new titles that don't exist. Do not make another other comments or acknowledgements.")
            print(f"Genre: {genre}")
            print(f"Titles: {titles_string}")
            for title in titles_string.split(','):
                all_titles[title.strip()] = genre

        all_titles_shuffled_keys = list(all_titles.keys())
        random.shuffle(all_titles_shuffled_keys)
        for title in all_titles_shuffled_keys:
            genre = all_titles[title].lower()
            base_prompt = f"Write a scene for a single chapter of an audiobook called `{title}`."
            script = prompt_ollama(f"{base_prompt} The book's genre is `{genre}`. Do not make another other comments or acknowledgements.")

            if index % 50 == 0:
                file_number += 1
            index += 1

            yield file_number, base_prompt, script


if __name__ == '__main__':
    generate_training_files("generated-scenes", entry_generator)
