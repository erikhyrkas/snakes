import random

from ys.data_generators.util.ollama_prompter import prompt_ollama


# run from root folder

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


def write_eli5_to_file(eli5s: dict, base_file_name, file_count):
    output_file = f'./training_data/{base_file_name}-{file_count}.md'
    with open(output_file, 'w', encoding="utf-8") as file:
        for eli5_topic in eli5s:
            eli5_answer = eli5s[eli5_topic]
            file.write(f"Explain {eli5_topic} like I'm five years old.<start>{eli5_answer}\n<end>\n\n")
        file.flush()


def generate_eli5s():
    topics = load_eli5_topics()

    base_file_name = 'llama-eli5'
    file_count = 0
    eli5s = dict()

    for idx, topic in enumerate(topics):
        print(f"Generating eli5 {idx + 1} of {len(topics)}: {topic}")
        eli5_answer = generate_eli5_result(topic)
        eli5s[topic] = eli5_answer

        if len(eli5s) == 25:
            write_eli5_to_file(eli5s, base_file_name, file_count)
            eli5s = dict()
            file_count += 1

    if eli5s:
        write_eli5_to_file(eli5s, base_file_name, file_count)


if __name__ == '__main__':
    generate_eli5s()
