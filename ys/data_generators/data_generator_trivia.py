import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files
from ys.data_generators.util.ollama_prompter import prompt_ollama


def get_trivia_question(trivia):
    prompt = (
        f"Generate a concise and simple question where the only answer is: {trivia}\n\n"
        f"Do not include any extra details beyond what's necessary for the answer. "
        f"The question should avoid adding dates, locations, or specific descriptions unless essential to identifying the answer. "
        f"Keep the question as general as possible while still having only one correct answer. "
        f"Do not provide additional comments or explanations."
    )
    trivia_question = prompt_ollama(prompt)
    return trivia_question


def get_trivia_statement(category, time_period):
    time_period_criteria = ''
    if len(time_period) > 0:
        time_period_criteria = f' from the {time_period}.'
    prompt = f"Generate an interesting or fun factual bit of trivia in the '{category}' category{time_period_criteria}. Only provide the trivia, not any extraneous statements. Do not provide additional comments or explanations."
    trivia = prompt_ollama(prompt)
    return trivia


def entry_generator() -> Tuple[int, str, str]:
    categories = ['History', 'Geography', 'Science', 'Literature', 'Movies', 'Music', 'Art', 'Sports', 'World Capitals',
                  'Famous People', 'Animals', 'Mythology and Religion', 'Technology', 'Inventions', 'Space',
                  'Food and Drink', 'Television Show', 'Video Game', 'Books and Authors', 'Politics', 'Famous Quotes',
                  'Architecture', 'Languages', 'Mathematics', 'Comics and Graphic Novels', 'Fashion',
                  'Theater and Plays', 'Nature and Environment', 'Pop Culture']
    timeless_categories = [
        "Mythology and Religion", "Geography", "Science", "Literature", "Animals", "Space", "Mathematics",
        "Architecture", "Nature and Environment", "Languages", "Art", "Famous Quotes", "Inventions"
    ]
    decades = ['', '1920s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
    file_number: int = 0
    index = 0
    for _ in range(200):
        random.shuffle(categories)
        for category in categories:
            time_period_list = ['']
            if category not in timeless_categories:
                time_period_list = decades
                random.shuffle(time_period_list)
            for time_period in time_period_list:
                trivia_answer = get_trivia_statement(category, time_period)
                trivia_question = get_trivia_question(trivia_answer)
                q_prefix = random.choice(['', '', '', 'Q: ', 'Question: '])
                a_prefix = ''
                if q_prefix == 'Q: ':
                    a_prefix = 'A: '
                elif q_prefix == 'Question: ':
                    a_prefix = 'Answer: '
                trivia_answer = f"{a_prefix}{trivia_answer}"
                trivia_question = f"{q_prefix}{trivia_question}"
                if index % 500 == 0:
                    file_number = file_number + 1
                index += 1
                yield file_number, trivia_question, trivia_answer


if __name__ == '__main__':
    generate_training_files("generated-trivia", entry_generator)
