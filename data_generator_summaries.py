import os
import random

from ollama import generate

from data_generator_stories import generate_story_seed


def generate_summaries(num_stories, model_name='llama3.1', output_file='training_data\\llama-summaries.md'):
    progress_count = 1
    base_file_name = output_file.split(".")[0]
    attempt = 0
    while os.path.isfile(output_file):
        output_file = f'{base_file_name}-{attempt}.md'
        attempt += 1
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
    with (open(output_file, 'w', encoding="utf-8") as file):
        for _ in range(num_stories):
            print(f"Writing summary {progress_count} of {num_stories}")
            seed = generate_story_seed()
            story_response = generate(model_name, seed)
            story = story_response['response'].strip()
            summary_prompt = (f"Rewrite the following story concisely--using as most a single paragraph. Only respond "
                              f"with the rewrite and no additional commentary.\nStory:\n{story}")
            summary = generate(model_name, summary_prompt)
            verb = random.choice(['Summarize', 'Rewrite concisely', 'Describe'])
            full_story = f"{verb} this story:\n" + \
                         story + "\n" + \
                         "<start>" + \
                         summary['response'].strip() + \
                         "\n<end>"
            for phrase_to_remove in phrases_to_remove:
                full_story = full_story.replace(phrase_to_remove, "")
            file.write(full_story.strip() + '\n\n')
            file.flush()
            progress_count += 1


if __name__ == '__main__':
    for _ in range(20):
        generate_summaries(100)
