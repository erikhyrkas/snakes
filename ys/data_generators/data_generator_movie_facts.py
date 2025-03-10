import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files, generate_training_files_v2
from ys.data_generators.util.item_loader import file_to_list
from ys.data_generators.util.ollama_prompter import prompt_ollama


def entry_generator() -> Tuple[str, str]:
    movie_titles_and_release_dates = file_to_list('top_movies.txt')

    while True:
        random.shuffle(movie_titles_and_release_dates)
        for movie_title_and_release_date in movie_titles_and_release_dates:
            theme = random.choice(["power", "love", "betrayal"])
            movie_questions = [
                f"What is the movie {movie_title_and_release_date} about?",
                f"Who is the main character in the movie {movie_title_and_release_date}, and what is their goal?",
                f"What genre is the movie {movie_title_and_release_date}, and what makes it unique?",
                f"Where and when does the movie {movie_title_and_release_date} take place?",
                f"What is the main conflict in the movie {movie_title_and_release_date}?",
                f"What are the main themes explored in the movie {movie_title_and_release_date}?",
                f"How does the movie {movie_title_and_release_date} explore {theme}?",
                f"What is the moral or lesson of the movie {movie_title_and_release_date}?",
                f"How does the protagonist change over the course of the movie {movie_title_and_release_date}?",
                f"Who is the most interesting side character in the movie {movie_title_and_release_date}, and why?",
                f"What is the climax of the movie {movie_title_and_release_date}?",
                f"Does the movie {movie_title_and_release_date} have a satisfying ending? Why or why not?",
                f"What did you like most about the movie {movie_title_and_release_date}?",
                f"How does the movie {movie_title_and_release_date} compare to others in the same genre?",
                f"Would you recommend the movie {movie_title_and_release_date}? Why or why not?",
                f"Who would enjoy the movie {movie_title_and_release_date} the most?"
            ]
            random.shuffle(movie_questions)
            for question in movie_questions:
                response = prompt_ollama(question)
                yield question, response


if __name__ == '__main__':
    generate_training_files_v2("generated-movie-facts", entry_generator)
