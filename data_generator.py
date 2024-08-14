import os
import random

from ollama import generate

genres = ['fantasy', 'sci-fi', 'mystery', 'adventure', 'horror']
genders = ['man', 'woman', 'non-binary person']
settings = ['forest', 'city', 'village', 'space station', 'desert']
plot_keywords = ['discovery', 'escape', 'friendship', 'revenge', 'lost']


def generate_story_seed():
    genre = random.choice(genres)
    age = random.randint(5, 80)
    gender = random.choice(genders)
    setting = random.choice(settings)
    plot_keyword = random.choice(plot_keywords)

    story_seed = (
        f"Write a {genre} story where the main character is a {age}-year-old {gender} "
        f"in a {setting}. The plot revolves around {plot_keyword}. "
        f"Please provide only the story without any additional information."
    )

    return story_seed


def generate_stories(num_stories, model_name='llama3.1', output_file='training_data\\llama-stories.md'):
    progress_count = 1
    base_file_name = output_file.split(".")[0]
    attempt = 0
    while os.path.isfile(output_file):
        output_file = f'{base_file_name}-{attempt}.md'
        attempt += 1
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
            file.write(full_story + '\n\n')
            file.flush()
            progress_count += 1


if __name__ == '__main__':
    generate_stories(100)
