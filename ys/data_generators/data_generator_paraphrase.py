import random
from typing import Tuple

from ys.data_generators.data_generator_stories import generate_story_seed
from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.ollama_prompter import prompt_ollama


def entry_generator() -> Tuple[str, str]:
    phrases_to_remove = [
        "Here is a prompt that asks for this story:",
        "Here is a prompt that asks for the story:",
        "Here's a prompt that asks for this story:",
        "Here is a prompt to request this story:",
        "Here is a prompt asking for this story:",
        "Here is a prompt to ask for this story:",
        "Here is a prompt for this story:",
        "Here's a prompt for you:",
        "Here is your prompt:",
        "Here is the prompt:",
        "Here's your prompt:",
        "Here's the prompt:",
        "Prompt:",
    ]
    while True:
        seed = generate_story_seed()
        story = prompt_ollama(seed)
        summary_prompt = (f"Paraphrase the following story concisely--using at most a single paragraph. Only respond "
                          f"with the rewrite and no additional commentary.\nStory:\n{story}")
        summary = prompt_ollama(summary_prompt)
        for phrase_to_remove in phrases_to_remove:
            summary = summary.replace(phrase_to_remove, "").strip()
        verb = random.choice(['Paraphrase', 'Rephrase', 'Interpret'])
        prompt = f"{verb} this story:\n{story}"
        yield prompt, summary


if __name__ == '__main__':
    generate_training_files_v2("generated-paraphrase", entry_generator)

