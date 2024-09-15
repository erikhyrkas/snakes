from ollama import generate


def prompt_ollama(prompt: str) -> str:
    response = generate('llama3.1', prompt)
    return response['response'].strip()
