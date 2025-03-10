import os

from ys.data_generators.util.ollama_prompter import ensure_ollama_model_is_loaded
from ys.data_generators.util.result_writer import append_prompt_response_to_file, remove_existing_files, \
    append_prompt_response_to_file_v2


def generate_training_files_v2(base_file_name: str, generator_func, max_files=20, remove_old_files=True):
    if remove_old_files:
        remove_existing_files(base_file_name)
    ensure_ollama_model_is_loaded()
    record_number = 1
    last_file_number = -1
    for result in generator_func():
        prompt, response = result
        if prompt is None or response is None:
            break

        file_number = max(last_file_number, 1)
        output_file_name = f'./training_data_v2/{base_file_name}-{file_number}.md'
        while os.path.exists(output_file_name) and os.stat(output_file_name).st_size > 100000:
            file_number += 1
            output_file_name = f'./training_data_v2/{base_file_name}-{file_number}.md'
        if file_number > max_files:
            break
        if file_number != last_file_number:
            record_number = 1
            last_file_number = file_number
        else:
            record_number += 1
        print(f"({file_number}/{record_number}): {prompt}\n{response}\n\n")
        append_prompt_response_to_file_v2(prompt, response, base_file_name, file_number)

def generate_training_files(base_file_name: str, prompt_response_func, remove_old_files=True):
    if remove_old_files:
        remove_existing_files(base_file_name)
    ensure_ollama_model_is_loaded()
    record_number = 1
    last_file_number = -1
    for result in prompt_response_func():
        file_number, prompt, response = result
        if prompt is None or response is None:
            break
        if file_number != last_file_number:
            record_number = 1
            last_file_number = file_number
        else:
            record_number += 1
        print(f"({file_number}/{record_number}): {prompt}\n{response}\n\n")
        append_prompt_response_to_file(prompt, response, base_file_name, file_number)