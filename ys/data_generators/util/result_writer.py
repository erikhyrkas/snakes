import glob
import os


def append_prompt_responses_to_file(prompt_responses: dict, base_file_name, file_count):
    output_file = f'./training_data/{base_file_name}-{file_count}.md'
    with open(output_file, 'a', encoding="utf-8") as file:
        for prompt in prompt_responses:
            response = prompt_responses[prompt]
            if "<start>" not in response:
                response = "<start>" + response
            if "<end>" not in response:
                response = response + "<end>"
            file.write(f"{prompt}{response.strip()}\n\n")
        file.flush()

def append_prompt_response_to_file(prompt: str, response: str, base_file_name, file_count):
    output_file = f'./training_data/{base_file_name}-{file_count}.md'
    with open(output_file, 'a', encoding="utf-8") as file:
        if "<start>" not in response:
            response = "<start>" + response
        if "<end>" not in response:
            response = response + "<end>"
        file.write(f"{prompt}{response.strip()}\n\n")
        file.flush()

def remove_existing_files(base_file_name):
    output_file_pattern = f'./training_data/{base_file_name}-*.md'
    for file_path in glob.glob(output_file_pattern):
        os.remove(file_path)
