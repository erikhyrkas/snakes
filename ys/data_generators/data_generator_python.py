import random

from ys.data_generators.util.ollama_prompter import prompt_ollama


# learn python

def func_prompt(task: str, signature: str) -> str:
    prompt = f"Write a python function that performs the following task:\n{task}\n\nThe function's signature looks like:\n{signature}"
    return prompt.strip()


def class_prompt(task: str, class_name: str) -> str:
    prompt = f"Write an example python class named {class_name} that is used to:\n{task}"
    return prompt.strip()


def load_tsv(file_name: str) -> list:
    with open(f'./ys/data_generators/{file_name}', 'r', encoding='utf-8') as file:
        words = [line.strip().split('\t') for line in file if line.strip()]
    random.shuffle(words)
    return words


def generate_python():
    results = []
    task_func_list = load_tsv('python_tasks.tsv')
    print(task_func_list)
    for task_func in task_func_list:
        task = task_func[0]
        func = task_func[1]
        prompt = func_prompt(task, func)
        print(prompt)
        result = prompt_ollama(prompt)
        results.append(f"{task} in Python.<start>{result}\n<end>")
        print(result)

    task_class_list = load_tsv('python_classes.tsv')
    print(task_class_list)
    for task_class in task_class_list:
        task = task_class[0]
        class_name = task_class[1]
        prompt = class_prompt(task, class_name)
        print(prompt)
        result = call_llm(prompt)
        print(result)
        results.append(f"{task} using a Python class.<start>{result}\n<end>")

    # note: i manually split the file after it ran.
    with open(f'./training_data/llama-python.md', 'w', encoding='utf-8') as result_file:
        result_file.write('\n'.join(results))


if __name__ == '__main__':
    generate_python()
