import os

from ys.inference.model_interface import ModelInterface


def interactive_interface():
    print("This is a usage example. This LLM will completely make up things and be wrong. Don't follow its advice and "
          "don't expect good results. There is no warranty. Use at your own risk.")
    base_path = os.getenv("YS_LLM_BASE_PATH", "./")

    model_path = f"{base_path}model/model.bin"
    if not os.path.isfile(model_path):
        model_path = f"{base_path}model/model_checkpoint.bin"

    tokenizer_path = f"{base_path}model/tokenizer.pkl"
    config_save_path = f"{base_path}model/model_config.json"
    if not os.path.exists(model_path):
        print("Did you forget to train the model?")
        return
    if not os.path.exists(tokenizer_path):
        print("Did you forget to train the tokenizer?")
        return

    print("Loading...")
    interface = ModelInterface(model_save_path=model_path, tokenizer_save_path=tokenizer_path, config_save_path=config_save_path)
    params = interface.count_parameters()

    print(f"Number of parameters: {params:,}")
    print(f"Vocabulary size: {interface.vocab_size():,}")
    print()
    print("Type text that the model will complete. Type 'exit' to exit.")
    while True:
        next_input = input("> ")
        if next_input == 'exit':
            break
        result = interface.instruct(next_input.strip(), top_p=1.0, max_tokens=64)
        print(f"\n{result}")


if __name__ == "__main__":
    interactive_interface()
