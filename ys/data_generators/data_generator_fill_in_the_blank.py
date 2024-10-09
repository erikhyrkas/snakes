import random
import string
import re

from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files
from ys.data_generators.util.ollama_prompter import prompt_ollama


# given a question with blanks and a multiple choice fill-in-the-blank collection, select the best choice.

def get_subtopics(category):
    prompt = f"Provide 20 subtopics for the category of {category}. Separate each subtopic with a comma. Do not provide additional comments or explanations."
    subtopics = prompt_ollama(prompt)
    list_of_subtopics = subtopics.strip().split(",")
    list_of_subtopics = [item.strip() for item in list_of_subtopics]
    print(f"Subtopics: {list_of_subtopics}")
    return list_of_subtopics


def get_correct_statement_with_critical_words(subtopic):
    prompt = f"Generate a factual sentence about {subtopic}, and surround 1 to 3 critical words with square brackets []. Do not provide additional comments or explanations."
    statement = prompt_ollama(prompt)
    sentence_with_critical_words = statement.strip()
    print(f"Statement: {sentence_with_critical_words}")
    return sentence_with_critical_words


def create_fill_in_the_blank_from_critical_words(statement):
    # Use regex to find all occurrences of [<term>], where <term> can be multiple words or special characters
    pattern = r"\[(.*?)\]"

    # Correct answers are the matched terms without the square brackets
    correct_answers = re.findall(pattern, statement)

    # Replace the matched terms with blanks and create the final fill-in-the-blank sentence
    blank_length = random.randint(3, 8)
    fill_in_the_blank = re.sub(pattern, "_" * blank_length, statement)

    return fill_in_the_blank, correct_answers


# Step 5: Generate multiple-choice options for the blanks
def get_multiple_choice_options(correct_answers, statement):
    multiple_choice = []
    print(f"Statement: {statement}")
    print(f"correct_answers: {correct_answers}")
    for correct_answer in correct_answers:
        prompt = f"Provide four multiple-choice options for the word '{correct_answer}' in the sentence: {statement}\nOne option should be correct, and the others should be plausible but incorrect. Only provide the plausible words separated by comma. Insure consistent capitalization with the correct answer -- unless it's a proper noun or the correct answer is capitalized, the words should be lower case. Make no other comments or statements."
        options = prompt_ollama(prompt)  # Assume this returns a list of options in a formatted string
        options_list = options.split(",")  # Parse options into a list
        options_list = [option.strip() for option in options_list]
        simplified_list = []
        for option in options_list:
            if option.lower() != correct_answer.lower():
                simplified_list.append(option)

        print(f"Options: {options_list}")
        simplified_list.append(correct_answer)
        random.shuffle(simplified_list)
        multiple_choice.append(simplified_list)
    return multiple_choice


# Step 6: Automate the entire process
def generate_questions_for_category(category):
    questions = []
    subtopics = get_subtopics(category)

    for subtopic in subtopics:
        try:
            # Generate the correct statement with critical words highlighted
            statement = get_correct_statement_with_critical_words(subtopic)

            # Convert the statement into fill-in-the-blank format
            fill_in_the_blank, correct_answers = create_fill_in_the_blank_from_critical_words(statement)

            # Generate multiple-choice options for each blank
            multiple_choice_options = get_multiple_choice_options(correct_answers, statement)

            # Store the generated question
            question = {
                "category": category,
                "subtopic": subtopic,
                "fill_in_the_blank": fill_in_the_blank,
                "correct_answers": correct_answers,
                "multiple_choice": multiple_choice_options
            }
            questions.append(question)

        except Exception as e:
            print(f"Error generating question for {subtopic}: {e}")

    return questions


def entry_generator() -> Tuple[int, str, str]:
    categories = [
        "Mathematics",
        "Science",
        "History",
        "Literature",
        "Technology",
        "Geography",
        "Languages",
        "Social Sciences"
    ]

    file_number: int = 0
    index = 0
    for _ in range(20):
        for category in categories:
            category_questions = generate_questions_for_category(category)
            #             question = {
            #                 "category": category,
            #                 "subtopic": subtopic,
            #                 "fill_in_the_blank": fill_in_the_blank,
            #                 "correct_answers": correct_answers,
            #                 "multiple_choice": multiple_choice_options
            #             }
            for question in category_questions:
                question_category = question["category"]
                use_single_letter_directions = random.choice([True, False, False])
                if use_single_letter_directions:
                    single_letter_directions = f'The following are multiple choice questions (with answers) about {question_category}. Think step by step and then finish your answer with "the answer is (X)" where X is the correct letter choice.\n'
                else:
                    single_letter_directions = ''
                question_tag = random.choice(['Q: ', 'Question: ', ''])
                if question_tag == 'Q: ':
                    answer_tag = 'A: '
                elif question_tag == 'Question: ':
                    answer_tag = 'Answer: '
                else:
                    answer_tag = ''
                prompt = f"{single_letter_directions}{question_tag}{question['fill_in_the_blank']}\n"
                option_index = 0
                punctuation = random.choice(['.', ')', ':'])
                correct_answers = question["correct_answers"]
                if len(correct_answers) == 0:
                    print(f"!!No correct answer for: {prompt}")
                    continue
                answer_list = [correct_answers]
                max_answers = random.randint(1, 15)
                for i in range(max_answers):
                    next_answer = []
                    for option in question["multiple_choice"]:
                        next_answer.append(random.choice(option))
                    if next_answer not in answer_list:
                        answer_list.append(next_answer)

                random.shuffle(answer_list)
                letters = string.ascii_uppercase
                correct_answer = ''
                correct_answer_letter = ''
                for answers in answer_list:
                    letter = letters[option_index]
                    joined_answer = ', '.join(answers)
                    next_answer = f"{letter}{punctuation} {joined_answer}"
                    if answers == correct_answers:
                        correct_answer_letter = letter
                        if use_single_letter_directions:
                            correct_answer = f"{answer_tag}The answer is {letter}"
                        else:
                            correct_answer = f"{answer_tag}{letter}. {joined_answer}"
                    option_index = option_index + 1
                    prompt += next_answer + "\n"

                simple_correct_answer = ", ".join(correct_answers)
                steps = prompt_ollama(
                    f"Provide a step-by-step explanation as to why the answers to the following fill-in-the-blank {question_category} question is ({simple_correct_answer}):\n```{prompt}```\n\nDo not provide additional comments beyond the step-by-step explanation. Each step should start with 'Step (x): ', where x is the step number. After the steps, conclude your explanation with the words 'The answer is {correct_answer_letter}'.")

                formatted_correct_answer_1 = f"The answer is {correct_answer_letter}".lower()
                formatted_correct_answer_2 = f"The answer is {correct_answer_letter}{punctuation}".lower()
                formatted_correct_answer_3 = f"The answer is {correct_answer_letter}.".lower()
                lower_steps = steps.lower()
                if lower_steps.endswith(formatted_correct_answer_1):
                    steps = steps[:-len(formatted_correct_answer_1)]
                elif lower_steps.endswith(formatted_correct_answer_2):
                    steps = steps[:-len(formatted_correct_answer_2)]
                elif lower_steps.endswith(formatted_correct_answer_3):
                    steps = steps[:-len(formatted_correct_answer_3)]

                steps = steps.strip()
                if "I cannot " not in steps:
                    correct_answer = f"{steps}\n\n{correct_answer}"
                if index % 500 == 0:
                    file_number = file_number + 1
                index += 1
                yield file_number, prompt, correct_answer


if __name__ == '__main__':
    generate_training_files("generated-fill-in-the-blank", entry_generator)
