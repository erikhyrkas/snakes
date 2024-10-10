from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files
from ys.data_generators.util.item_loader import file_to_list
from ys.data_generators.util.ollama_prompter import prompt_ollama


def entry_generator() -> Tuple[int, str, str]:
    topics = file_to_list('wiki_topics.txt')
    full_topics = []
    for topic in topics:
        subtopics_string = prompt_ollama(f"Provide a comma delimited list of 20 subtopics for the topic '{topic}'. Do not make another other comments or acknowledgements.")
        print(f"Topic: {topic}")
        print(f"Subtopics: {subtopics_string}")
        for subtopic in subtopics_string.split(','):
            full_topics.append({
                'topic': topic,
                'subtopic': subtopic.strip()
            })
    file_number: int = 0
    index = 0
    for full_topic in full_topics:
        topic = full_topic['topic']
        subtopic = full_topic['subtopic']
        base_prompt = f"Write a podcast about {subtopic} as it relates to {topic}."
        prompt = f"{base_prompt} Make the podcast interesting, fun, and informative.\nThe podcast script should include two participants labeled '[Host]: ' and, if a guest expert is useful, '[Guest]: '. Don't provide links or urls. This is a script that will be read and used to direct music and sound effects."
        podcast = prompt_ollama(prompt)
        if index % 100 == 0:
            file_number = file_number + 1
        index += 1
        yield file_number, base_prompt, podcast


if __name__ == '__main__':
    generate_training_files("generated-podcast", entry_generator)
