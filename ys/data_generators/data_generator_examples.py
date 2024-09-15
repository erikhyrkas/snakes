import random

from ys.data_generators.util.ollama_prompter import prompt_ollama


# run from root folder

def load_words(file_path='./ys/data_generators/english.txt'):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    random.shuffle(words)
    return words


def generate_example_sentence(word):
    prompt = (
        f"Generate several example sentences using the word '{word}' in different contexts. "
        "Include various meanings and uses of the word if applicable."
    )
    return prompt_ollama(prompt)


def write_sentences_to_file(sentences: dict, base_file_name, file_count):
    output_file = f'./training_data/{base_file_name}-{file_count}.md'
    with open(output_file, 'w', encoding="utf-8") as file:
        for word in sentences:
            examples = sentences[word]
            file.write(f"Generate example sentences using the word '{word}'.<start>{examples}\n<end>\n\n")
        file.flush()


def generate_example_sentences():
    words = load_words()

    base_file_name = 'llama-sentences'
    file_count = 0
    sentences = dict()

    for idx, word in enumerate(words):
        print(f"Generating example sentences {idx + 1} of {len(words)}: {word}")
        examples = generate_example_sentence(word)
        sentences[word] = examples

        if len(sentences) == 200:
            write_sentences_to_file(sentences, base_file_name, file_count)
            sentences = dict()
            file_count += 1

    if sentences:
        write_sentences_to_file(sentences, base_file_name, file_count)


if __name__ == '__main__':
    generate_example_sentences()
