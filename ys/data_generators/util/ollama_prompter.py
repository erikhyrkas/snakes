import ollama
from ollama import generate, ProgressResponse

OLLAMA_MODEL = 'llama3.1'

def ensure_ollama_model_is_loaded():
    try:
        prompt_ollama('hello')
    except ollama.ResponseError as e:
        if e.status_code == 404:
            response: ProgressResponse = ollama.pull(OLLAMA_MODEL)
            if response.get('status') != 'success':
                raise e

def prompt_ollama(prompt: str) -> str:
    response = generate(OLLAMA_MODEL, prompt)
    return response['response'].strip()
