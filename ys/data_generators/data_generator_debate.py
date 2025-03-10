import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.ollama_prompter import prompt_ollama


# run from root folder

def load_debate_topics():
    with open('./ys/data_generators/debate_topics.txt', 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    random.shuffle(words)
    return words


def generate_debate_result(topic):
    prompt = (
        f"Write a scene where two high school students from different states have a debate about the topic: {topic}"
    )
    return prompt_ollama(prompt)


def entry_generator() -> Tuple[str, str]:
    topics = load_debate_topics()

    while True:
        for idx, topic in enumerate(topics):
            debate_result = generate_debate_result(topic)
            prompt = f"Write a scene where two students have a debate about: {topic}"
            return prompt, debate_result


if __name__ == '__main__':
    generate_training_files_v2("generated-debates", entry_generator)
