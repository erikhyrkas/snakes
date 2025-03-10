import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.ollama_prompter import prompt_ollama


def load_eli5_topics():
    with open('./ys/data_generators/eli5_topics.txt', 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    random.shuffle(words)
    return words


def generate_eli5_result(topic):
    prompt = (
        f"Explain {topic} like I'm five years old."
    )
    return prompt_ollama(prompt)


def entry_generator() -> Tuple[str, str]:
    topics = load_eli5_topics()

    while True:
        for idx, topic in enumerate(topics):
            eli5_answer = generate_eli5_result(topic)
            prompt = f"Explain {topic} like I'm five years old."
            yield prompt, eli5_answer


if __name__ == '__main__':
    generate_training_files_v2("generated-eli5", entry_generator)
