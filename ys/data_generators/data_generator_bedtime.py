import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.ollama_prompter import prompt_ollama


def entry_generator() -> Tuple[str, str]:
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

    verbs = ['an exciting', 'a', 'a fun', 'an interesting', 'a long', 'a short', 'a thought provoking', 'an unexpected', 'a silly', 'a funny', 'a humorous', 'a playful']
    while True:
        all_titles = dict()
        for genre in genres:
            lower_genre = genre.lower()
            titles_string = prompt_ollama(
                f"Provide a comma delimited list of 20 titles for bedtime stories in the {lower_genre} genre. Do not use titles of real books, invent new titles that don't exist. Do not make another other comments or acknowledgements.")
            print(f"Genre: {genre}")
            print(f"Titles: {titles_string}")
            for title in titles_string.split(','):
                all_titles[title.strip()] = genre

        all_titles_shuffled_keys = list(all_titles.keys())
        random.shuffle(all_titles_shuffled_keys)
        for title in all_titles_shuffled_keys:
            genre = all_titles[title].lower()
            verb = random.choice(verbs)
            base_prompt = f"Write {verb} bedtime story called `{title}`."
            story = prompt_ollama(f"{base_prompt} The genre is `{genre}`. Do not make another other comments or acknowledgements.")

            yield base_prompt, story


if __name__ == '__main__':
    generate_training_files_v2("generated-bedtime", entry_generator)
