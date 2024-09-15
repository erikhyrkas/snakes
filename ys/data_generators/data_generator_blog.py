from data_generator_wiki import load_topics
from ys.data_generators.util.ollama_prompter import prompt_ollama


# run from root folder

def generate_blog_post(topic):
    article_seed = (
        f"Write a simple, legible blog post about {topic}. "
        "Keep the vocabulary and grammatical structure simple. "
        "Focus on clarity and providing essential information."
    )
    return prompt_ollama(article_seed)


def write_blogs_to_file(articles: dict, base_file_name, file_count):
    output_file = f'./training_data/{base_file_name}-{file_count}.md'
    with open(output_file, 'w', encoding="utf-8") as file:
        for topic in articles:
            article = articles[topic]
            file.write(f"Write a blog post about {topic}.<start>{article}\n<end>\n\n")
        file.flush()


def generate_wiki_articles():
    topics = load_topics()

    base_file_name = 'llama-blog'
    file_count = 0
    articles = dict()

    for idx, topic in enumerate(topics):
        print(f"Generating blog post {idx + 1} of {len(topics)}: {topic}")
        article = generate_blog_post(topic)
        articles[topic] = article

        if len(articles) == 20:
            write_blogs_to_file(articles, base_file_name, file_count)
            articles = dict()
            file_count += 1

    if articles:
        write_blogs_to_file(articles, base_file_name, file_count)


if __name__ == '__main__':
    generate_wiki_articles()
