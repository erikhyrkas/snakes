import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files, generate_training_files_v2
from ys.data_generators.util.ollama_prompter import prompt_ollama


def entry_generator() -> Tuple[str, str]:
    # I had to really restrict the categories to avoid jokes that were not remotely jokes.
    # I'm not really impressed with any of the jokes it did generate, but it's text.
    joke_category = ['Tell a joke', 'Tell a knock-knock joke', 'Tell a dad joke', 'Tell a pun-based joke',
                     'Give me a riddle', 'Write a limerick',
                     'Tell a joke using wordplay', 'Tell a slapstick joke'
                     ]
    joke_subjects = ['animals', 'sports', 'food', 'technology', 'science', 'math', 'history', 'geography',
                     'screwing in a light bulb', 'school', 'teachers', 'doctors', 'lawyers', 'engineers', 'music',
                     'art', 'pop culture', 'work', 'office', 'marriage', 'parenting', 'politics', 'holidays', 'space',
                     'relationships', 'dating', 'fantasy', 'sci-fi', 'books', 'video games']

    while True:
        joke_instruction_start = random.choice(joke_category)
        joke_subject = random.choice(joke_subjects)
        joke_instruction_finish = random.choice(['', f' involving {joke_subject}'])
        prompt: str = f"{joke_instruction_start}{joke_instruction_finish}."
        if 'riddle' in prompt:
            final_instruction = " Do not provide any additional acknowledgements or text beyond the riddle. Include the riddle's answer at the end."
        elif 'limerick' in prompt:
            final_instruction = " Do not provide any additional acknowledgements or text beyond the limerick."
        else:
            final_instruction = " Do not provide any additional acknowledgements or text beyond the joke."
        ollama_prompt = f"{prompt} Respond in English. Be witty and funny. Do not be racist, sexist, or lewd. Do not body shame. Use clear and easy to understand language. {final_instruction}"
        response = prompt_ollama(ollama_prompt)
        yield prompt, response


if __name__ == '__main__':
    generate_training_files_v2("generated-jokes", entry_generator)
