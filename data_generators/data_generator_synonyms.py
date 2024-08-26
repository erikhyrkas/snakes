import random

from ollama import generate

from data_generator_examples import load_words


def generate_synonyms(word):
    prompt = (
        f"Provide a list of synonyms for the word '{word}'. "
        "Include various meanings and uses of the word if applicable."
    )
    response = generate('llama3.1', prompt)
    examples = response['response'].strip()
    return examples


def write_synonyms_to_file(sentences: dict, base_file_name, file_count):
    output_file = f'../training_data/{base_file_name}-{file_count}.md'
    with open(output_file, 'w', encoding="utf-8") as file:
        for word in sentences:
            examples = sentences[word]
            file.write(f"Provide synonyms for the word '{word}'.<start>{examples}\n<end>\n\n")
        file.flush()


def generate_all_synonyms():
    words = load_words()

    base_file_name = 'llama-synonyms'
    file_count = 0
    sentences = dict()

    for idx, word in enumerate(words):
        print(f"Generating synonyms {idx + 1} of {len(words)}: {word}")
        examples = generate_synonyms(word)
        sentences[word] = examples

        if len(sentences) == 200:
            write_synonyms_to_file(sentences, base_file_name, file_count)
            sentences = dict()
            file_count += 1

    if sentences:
        write_synonyms_to_file(sentences, base_file_name, file_count)


if __name__ == '__main__':
    generate_all_synonyms()
