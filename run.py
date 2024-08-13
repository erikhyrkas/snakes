from model import Completer


def do_completions():
    print("Loading...")
    completer = Completer()
    print("Type text that the model will complete. Type 'exit' to exit.")
    while True:
        next_input = input("> ")
        if next_input == 'exit':
            break
        # clean input slightly by treating it as a complete word
        # This avoids garbage output when the text is out of vocab.
        next_input = next_input.strip() + ' '
        result = completer.complete(next_input)
        print(f"\n{result}")


if __name__ == "__main__":
    do_completions()
