from model import ModelInterface


def do_completions():
    print("Loading...")
    completer = ModelInterface()
    print("Type a prompt that the model will write a story about. Type 'exit' to exit.")
    while True:
        next_input = input("> ")
        if next_input == 'exit':
            break
        result = completer.prompt(next_input.strip())
        print(f"\n{result}")


if __name__ == "__main__":
    do_completions()
