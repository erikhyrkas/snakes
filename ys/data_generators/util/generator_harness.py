from ys.data_generators.util.ollama_prompter import ensure_ollama_model_is_loaded
from ys.data_generators.util.result_writer import append_prompt_response_to_file, remove_existing_files


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