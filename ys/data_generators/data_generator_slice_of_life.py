import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.ollama_prompter import prompt_ollama


# I got the list of names from: https://www.ssa.gov/oact/babynames/decades/ and
# https://www.ssa.gov/oact/babynames/index.html

# I removed Adolf manually, because we don't need that, but otherwise,
# combined the names of every decade and then sorted and de-duped tne names.

# This is the command I used to de-dupe:
# awk '!seen[$0]++' names_with_dupes.txt > names.txt

# There are many, many great ethnic names that are missing because this list is based on what the ssa registered.
# No offense intended. If you retrain this model, I'm sure there are many great opportunities to improve the list.

def load_items(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        topics = [line.strip() for line in file if line.strip()]
    random.shuffle(topics)
    return topics


def group_names(names):
    result = []
    while names:
        # Randomly choose to group 1, 2, or 3 names
        group_size = random.randint(1, 3)

        # Ensure we don't try to group more names than are left in the list
        group_size = min(group_size, len(names))

        # Pop names from the list and create a group
        group = [names.pop() for _ in range(group_size)]

        # Format the group of names into a string
        if len(group) == 3:
            result.append(f"{group[0]}, {group[1]}, and {group[2]}")
        elif len(group) == 2:
            result.append(f"{group[0]} and {group[1]}")
        else:
            result.append(group[0])

    return result


def generate_slice_of_life_story(group, location, topic):
    prompt = (
        f"Write a simple, legible slice-of-life story about {group} who are together {location} "
        f"discussing the topic of {topic}.\n"
        "Keep the vocabulary and grammatical structure simple. "
        "Focus on clarity and providing essential information. The story should be about two pages long.\n"
        "Respond with only the story."
    )
    return prompt_ollama(prompt)


def entry_generator() -> Tuple[str, str]:
    names = load_items('./ys/data_generators/names.txt')
    groups = group_names(names)
    locations = load_items('./ys/data_generators/locations.txt')
    topics = load_items('./ys/data_generators/wiki_topics.txt')

    while True:
        for idx, group in enumerate(groups):
            location = random.choice(locations)
            topic = random.choice(topics)
            prompt = f"Write a slice-of-life story about {group} discussing {topic} {location}."
            story = generate_slice_of_life_story(group, location, topic)
            yield prompt, story



if __name__ == '__main__':
    generate_training_files_v2("generated-slice-of-life", entry_generator)
