import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.ollama_prompter import prompt_ollama


def load_explanation_topics():
    with open('./ys/data_generators/eli5_topics.txt', 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    random.shuffle(words)
    return words


def generate_explanation_result(topic):
    prompt = (
        f"Explain {topic} in simple terms."
    )
    return prompt_ollama(prompt)


def entry_generator() -> Tuple[str, str]:
    topics = load_explanation_topics()

    while True:
        for idx, topic in enumerate(topics):
            print(f"Generating explanations {idx + 1} of {len(topics)}: {topic}")
            answer = generate_explanation_result(topic)
            prompt = f"Explain {topic} in simple terms."
            yield answer, prompt


if __name__ == '__main__':
    generate_training_files_v2("generated-sentences", entry_generator)
