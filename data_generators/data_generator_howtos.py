import random

from ollama import generate


def load_howto_topics():
    with open('./howto_topics.txt', 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    random.shuffle(words)
    return words


def generate_howto_result(topic):
    prompt = (
        f"How do I {topic}?"
    )
    response = generate('llama3.1', prompt)
    howto = response['response'].strip()
    print(f"{prompt}\n{howto}")
    return howto


def write_howto_to_file(howtos: dict, base_file_name, file_count):
    output_file = f'../training_data/{base_file_name}-{file_count}.md'
    with open(output_file, 'w', encoding="utf-8") as file:
        for howto_topic in howtos:
            howto_answer = howtos[howto_topic]
            file.write(f"How do I {howto_topic}?<start>{howto_answer}\n<end>\n\n")
        file.flush()


def generate_howtos():
    topics = load_howto_topics()

    base_file_name = 'llama-howto'
    file_count = 0
    howtos = dict()

    for idx, topic in enumerate(topics):
        print(f"Generating howto {idx + 1} of {len(topics)}: {topic}")
        howto_answer = generate_howto_result(topic)
        howtos[topic] = howto_answer

        if len(howtos) == 25:
            write_howto_to_file(howtos, base_file_name, file_count)
            howtos = dict()
            file_count += 1

    if howtos:
        write_howto_to_file(howtos, base_file_name, file_count)


if __name__ == '__main__':
    generate_howtos()
