import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.ollama_prompter import prompt_ollama


def load_howto_topics():
    with open('./ys/data_generators/howto_topics.txt', 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    random.shuffle(words)
    return words


def generate_howto_result(topic):
    prompt = (
        f"How do I {topic}?"
    )
    howto = prompt_ollama(prompt)
    print(f"{prompt}\n{howto}")
    return howto


def write_howto_to_file(howtos: dict, base_file_name, file_count):
    output_file = f'./training_data/{base_file_name}-{file_count}.md'
    with open(output_file, 'w', encoding="utf-8") as file:
        for howto_topic in howtos:
            howto_answer = howtos[howto_topic]
            file.write(f"How do I {howto_topic}?<start>{howto_answer}\n<end>\n\n")
        file.flush()


def entry_generator() -> Tuple[str, str]:
    topics = load_howto_topics()

    while True:
        for idx, topic in enumerate(topics):
            howto_answer = generate_howto_result(topic)
            howto_prompt = f"How do I {topic}?"
            yield howto_prompt, howto_answer


if __name__ == '__main__':
    generate_training_files_v2("generated-howto", entry_generator)
