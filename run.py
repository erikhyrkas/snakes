import os

from model_interface import ModelInterface


def interactive_interface():
    base_path = os.getenv("YS_LLM_BASE_PATH", "./")
    model_path = f"{base_path}model.bin"
    tokenizer_path = f"{base_path}tokenizer.pkl"
    print("Loading...")
    interface = ModelInterface(model_save_path=model_path, tokenizer_save_path=tokenizer_path)
    params = interface.count_parameters()
    print(f"Number of parameters: {params}")
    print(f"Vocabulary size: {interface.vocab_size()}")
    print("Type a prompt that the model will write a story about. Type 'exit' to exit.")
    while True:
        next_input = input("> ")
        if next_input == 'exit':
            break
        result = interface.prompt(next_input.strip(), max_tokens=100)
        print(f"\n{result}")


if __name__ == "__main__":
    interactive_interface()
