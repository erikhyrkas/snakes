import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.item_loader import file_to_list
from ys.data_generators.util.ollama_prompter import prompt_ollama


def entry_generator() -> Tuple[str, str]:
    book_title_and_by_lines = file_to_list('top_books.txt')

    while True:
        random.shuffle(book_title_and_by_lines)
        for book_title_and_by_line in book_title_and_by_lines:
            book_questions = [
                f"What is {book_title_and_by_line} about?",
                f"Who is the main character in {book_title_and_by_line}, and what is their goal?",
                f"What genre is {book_title_and_by_line}, and what makes it unique?",
                f"Where and when does {book_title_and_by_line} take place?",
                f"What is the main conflict in {book_title_and_by_line}?",
                f"What are the main themes explored in {book_title_and_by_line}?",
                f"How does {book_title_and_by_line} explore [specific theme, e.g., power, love, betrayal]?",
                f"What is the moral or lesson of {book_title_and_by_line}?",
                f"How does the protagonist change over the course of {book_title_and_by_line}?",
                f"Who is the most interesting side character in {book_title_and_by_line}, and why?",
                f"What is the climax of {book_title_and_by_line}?",
                f"Does {book_title_and_by_line} have a satisfying ending? Why or why not?",
                f"What did you like most about {book_title_and_by_line}?",
                f"How does {book_title_and_by_line} compare to others in the same genre?",
                f"Would you recommend {book_title_and_by_line}? Why or why not?",
                f"Who would enjoy {book_title_and_by_line} the most?"
            ]
            random.shuffle(book_questions)
            for question in book_questions:
                response = prompt_ollama(question)
                yield question, response


if __name__ == '__main__':
    generate_training_files_v2("generated-book-facts", entry_generator)
