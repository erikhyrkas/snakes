import os
import random

from ollama import generate

genres = ['fantasy', 'sci-fi', 'mystery', 'adventure', 'horror', 'urban fantasy', "children's"]
genders = ['male', 'female', 'non-binary']
settings = ['forest', 'city', 'village', 'space station', 'desert', 'hidden city', 'jungle']
plot_keywords = ['discovery', 'escape', 'friendship', 'revenge', 'the return home', 'love', 'greed']
extra = ['', 'The antagonist is a relative of the main character. ', 'The main character has two friends. ',
         'The main character has a pet. ', 'The world has magic. ']


def generate_story_seed():
    genre = random.choice(genres)
    age = random.randint(5, 80)
    gender = random.choice(genders)
    setting = random.choice(settings)
    plot_keyword = random.choice(plot_keywords)
    extra_requirement = random.choice(extra)

    story_seed = (
        f"Write a {genre} story where the main character is {gender}, {age}-year-old, and "
        f"in a {setting}. The plot revolves around {plot_keyword}. {extra_requirement}"
        f"Keep the vocabulary and grammatical structure simple. Please provide only the "
        f"story without any additional information."
    )

    return story_seed


def generate_stories(num_stories, model_name='llama3.1', output_file='training_data\\llama-stories.md'):
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
    with open(output_file, 'w', encoding="utf-8") as file:
        for _ in range(num_stories):
            print(f"Writing story {progress_count} of {num_stories}")
            seed = generate_story_seed()
            story_response = generate(model_name, seed)
            story = story_response['response'].strip()
            user_prompt = f" Write a prompt that asks for this story. Only respond with the prompt. The story:\n{story}"
            user_prompt_response = generate(model_name, user_prompt)
            full_story = user_prompt_response[
                             'response'].strip() + "<start>" + story + "\n<end>"
            for phrase_to_remove in phrases_to_remove:
                full_story = full_story.replace(phrase_to_remove, "")
            file.write(full_story.strip() + '\n\n')
            file.flush()
            progress_count += 1


if __name__ == '__main__':
    for _ in range(20):
        generate_stories(100)
