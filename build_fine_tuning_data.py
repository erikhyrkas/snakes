import os
from collections import deque
from tokenizer import Tokenizer


def write_records(records, target_folder, items_per_file, tokenizer):
    # Tokenize each record and store the length with the record for sorting
    token_lengths = [(record, len(tokenizer.tokenize(record))) for record in records]

    # Sort based on the number of tokens
    token_lengths.sort(key=lambda x: x[1])

    queue = deque(token_lengths)
    file_index = 0
    while queue:
        with open(os.path.join(target_folder, f"batch_{file_index}.txt"), 'w', encoding='utf-8') as file:
            for _ in range(min(items_per_file, len(queue))):
                record, _ = queue.popleft()
                file.write(record + '\n')
        file_index += 1


def bucket_data(source_folder, target_folder, items_per_file=256, max_records_in_memory=3000):
    base_path = os.getenv("YS_LLM_BASE_PATH", "./")
    tokenizer_path = f"{base_path}tokenizer.pkl"
    tokenizer = Tokenizer()
    if os.path.exists(tokenizer_path):
        tokenizer.load(tokenizer_path)
        print("Loaded existing tokenizer.")
    else:
        print("Tokenizer not found.")
        return
    os.makedirs(target_folder, exist_ok=True)
    all_records = []

    # Load records from files until a limit is reached
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        records = [rec.strip() + '<end>' for rec in text.split('<end>') if rec.strip()]  # Split and keep <end>

        all_records.extend(records)
        if len(all_records) >= max_records_in_memory:
            # Process and clear records in memory
            write_records(all_records, target_folder, items_per_file, tokenizer)
            all_records = []

    # Final batch processing if there are any records left
    if all_records:
        write_records(all_records, target_folder, items_per_file, tokenizer)


if __name__ == '__main__':
    bucket_data('./training_data/', './fine_tuning/')
