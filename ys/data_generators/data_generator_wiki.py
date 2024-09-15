import random

from ys.data_generators.util.ollama_prompter import prompt_ollama


def load_topics(file_path='./ys/data_generators/wiki_topics.txt'):
    with open(file_path, 'r', encoding='utf-8') as file:
        topics = [line.strip() for line in file if line.strip()]
    random.shuffle(topics)
    return topics


def generate_wiki_article(topic):
    article_seed = (
        f"Write a simple, legible wiki article about {topic}. "
        "Keep the vocabulary and grammatical structure simple. "
        "Focus on clarity and providing essential information."
    )
    return prompt_ollama(article_seed)


def write_articles_to_file(articles: dict, base_file_name, file_count):
    output_file = f'./training_data/{base_file_name}-{file_count}.md'
    with open(output_file, 'w', encoding="utf-8") as file:
        for topic in articles:
            article = articles[topic]
            file.write(f"Write a wiki article about {topic}.<start>{article}\n<end>\n\n")
        file.flush()


def generate_wiki_articles():
    topics = load_topics()

    base_file_name = 'llama-wiki'
    file_count = 0
    articles = dict()

    for idx, topic in enumerate(topics):
        print(f"Generating article {idx + 1} of {len(topics)}: {topic}")
        article = generate_wiki_article(topic)
        articles[topic] = article

        if len(articles) == 20:
            write_articles_to_file(articles, base_file_name, file_count)
            articles = dict()
            file_count += 1

    if articles:
        write_articles_to_file(articles, base_file_name, file_count)


if __name__ == '__main__':
    generate_wiki_articles()
