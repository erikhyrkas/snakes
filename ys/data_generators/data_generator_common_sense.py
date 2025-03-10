import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.item_loader import file_to_list
from ys.data_generators.util.ollama_prompter import prompt_ollama


def entry_generator() -> Tuple[str, str]:
    common_sense_topics = file_to_list('common_sense.txt')

    verbs = ['an exciting', 'a', 'a fun', 'an interesting', 'a long', 'a short', 'a thought provoking', 'an unexpected']
    while True:
        random.shuffle(common_sense_topics)
        for topic in common_sense_topics:
            verb = random.choice(verbs)

            ollama_prompt = prompt_ollama(f"Write {verb} question related to the topic of: {topic}")
            question = prompt_ollama(ollama_prompt)
            response = prompt_ollama(question)
            yield question, response


if __name__ == '__main__':
    generate_training_files_v2("generated-common-sense", entry_generator)
