import random
from typing import Tuple

from data_generator_wiki import load_topics
from ys.data_generators.util.generator_harness import generate_training_files_v2
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


def entry_generator() -> Tuple[str, str]:
    topics = load_topics()

    while True:
        random.shuffle(topics)
        for idx, topic in enumerate(topics):
            print(f"Generating blog post {idx + 1} of {len(topics)}: {topic}")
            article = generate_blog_post(topic)
            yield f"Write a blog post about {topic}.", article


if __name__ == '__main__':
    generate_training_files_v2("generated-blog", entry_generator)
