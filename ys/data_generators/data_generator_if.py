import random
import string
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files, generate_training_files_v2
from ys.data_generators.util.ollama_prompter import prompt_ollama


def entry_generator() -> Tuple[str, str]:
    """
    A generator that yields a file number, a dynamically generated training prompt, and a validated response.
    Each iteration generates a new prompt and response, validates the response, and retries if necessary.
    """
    instruction_checks = [
        # Case modification instructions
        "The answer must have every word capitalized.",
        "The answer must have every word in lowercase.",
        "A [percent]% of words in the answer must be capitalized.",

        # Format-based instructions
        "The answer must be in valid JSON format.",
        "The answer must be separated into [sections] sections, with a blank line between sections.",
        "The answer must be under [character_length] characters in length.",
        "The answer must contain exactly [paragraph_count] paragraphs.",
        "The answer must contain a bullet-point list with the [list_length] items or more.",

        # Keyword-based instructions
        "The answer must include the [word_count] words.",
        "The answer must not include the word `[not_word]`.",
        "The word `[specific_word]` must appear at least [word_count] times in the answer.",
        "The letter `[specific_letter]` must appear at least [word_count] times in the answer.",

        # Response structure and content
        "The answer must repeat the question before answering.",
        "The answer must end with `[specified_text]`.",
        "The first sentence of the second paragraph of the answer must start with the word `[specific_word]`.",
        "The answer must include at least one quotation (e.g., 'quoted text').",

        # Special instructions
        "The answer must contain no commas.",
        "The answer must end with the sentence `[specified_text]`.",
        "The answer must contain exactly [sentence_count] sentences.",
        "The answer must contain the [word_range] words."
    ]

    # Initialize counters

    max_retries = 5
    categories = ['History', 'Geography', 'Science', 'Literature', 'Movies', 'Music', 'Art', 'Sports', 'World Capitals',
                  'Famous People', 'Animals', 'Mythology and Religion', 'Technology', 'Inventions', 'Space',
                  'Food and Drink', 'Television Show', 'Video Game', 'Books and Authors', 'Famous Quotes',
                  'Architecture', 'Languages', 'Mathematics', 'Comics and Graphic Novels', 'Fashion',
                  'Theater and Plays', 'Nature and Environment', 'Pop Culture', "Mythology and Religion", "Geography",
                  "Science", "Literature", "Animals", "Space", "Mathematics", "Architecture", "Nature and Environment",
                  "Languages", "Art", "Famous Quotes", "Inventions"
                  ]
    while True:
        num_instructions = random.randint(1, 3)
        category = random.choice(categories)
        question = prompt_ollama(
            f"Generate a single question related to `{category}`. Do not include any other acknowledgements or extraneous text that isn't the single question.")
        print(question)
        question += "\n"
        used_instruction = set()
        for _ in range(num_instructions):
            instruction_generation_prompt = random.choice(instruction_checks)
            if instruction_generation_prompt in used_instruction:
                continue
            used_instruction.add(instruction_generation_prompt)
            question += f" * {instruction_generation_prompt}\n"
        percent = random.randint(5, 15)
        question = question.replace('[percent]', f'{percent}')
        section_count = random.randint(2, 3)
        question = question.replace('[sections]', f'{section_count}')
        character_length = random.randint(200, 500)
        question = question.replace('[character_length]', f'{character_length}')
        paragraph_count = random.randint(1, 5)
        question = question.replace('[paragraph_count]', f'{paragraph_count}')
        list_length = random.randint(2, 10)
        question = question.replace('[list_length]', f'{list_length}')
        word_count = random.randint(100, 150)
        question = question.replace('[word_count]', f'{word_count}')
        not_word = random.choice(['and', 'or', 'but', 'the', 'an', 'a'])
        question = question.replace('[not_word]', not_word)
        specific_word = random.choice(
            ['penguin', 'pig', 'joker', 'chest', 'pink', 'balloon', 'cliff', 'island', 'sun', 'moon', 'blank', 'bang'])
        question = question.replace('[specific_word]', specific_word)
        specific_letter = random.choice(string.ascii_lowercase)
        question = question.replace('[specific_letter]', specific_letter)
        specified_text = random.choice(['The end.', "Fin.", "All done."])
        question = question.replace('[specified_text]', specified_text)
        sentence_count = random.randint(1, 10)
        question = question.replace('[sentence_count]', f'{sentence_count}')
        word_range = word_count + random.randint(50, 100)
        question = question.replace('[word_range]', f'{word_count}-{word_range}')
        answer = ''
        retry_count = 0
        valid_response = False
        while not valid_response and retry_count < max_retries:
            answer = prompt_ollama(question)
            full_validation_prompt = f"Answer Yes or No, with no other response.\nDoes this response answer the question exactly, formatting the answer perfectly?\n\nQuestion: {question}\n\nAnswer:\n```{answer}```"
            valid = prompt_ollama(full_validation_prompt)
            valid_response = 'Yes' == valid.strip()
            if not valid_response:
                retry_count += 1
                print(f"Retrying prompt (attempt {retry_count}) for instruction '{question}' and answer '{answer}'")

        if not valid_response:
            print(
                f"Failed to generate valid response after {max_retries} attempts for instruction '{question}' and answer '{answer}'")
            continue

        yield question, answer


if __name__ == '__main__':
    generate_training_files_v2("generated-if", entry_generator)
