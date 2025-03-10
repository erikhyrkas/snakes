import os
import random

from ys.data_generators.factory.structured_data_generator import StructuredDataGenerator
from ys.data_generators.util.tabular_formatter import TabularDataFormatter, pick_random_file_format


# a bunch of conversions from json<->csv<->md table<->text


def generate_format_conversion_prompt_and_response(structured_data):
    formatter = TabularDataFormatter(structured_data)
    to_format = pick_random_file_format()
    from_format = pick_random_file_format(avoid_format=to_format)

    # Get data in the 'from' format
    data_in_format = formatter.to(from_format)

    # Convert the data to the 'to' format
    response_data = formatter.to(to_format)

    # Wrap the response in <start><end> tags
    response = f"<start>\n{response_data.strip()}\n<end>"

    if random.choice([True, False]):
        if random.choice([True, False]):
            to_format = to_format.upper()
        else:
            to_format = to_format.capitalize()
    if random.choice([True, False]):
        if random.choice([True, False]):
            from_format = from_format.upper()
        else:
            from_format = from_format.capitalize()

    # Generate the prompt with variations
    prompts = [
        f"Convert this {from_format} to {to_format}:\n{data_in_format}",
        f"Please transform the following {from_format} data into {to_format}:\n{data_in_format}",
        f"Here's some {from_format} data, can you convert it to {to_format}?\n{data_in_format}",
        f"Can you change this {from_format} into {to_format}?\n{data_in_format}",
        f"Transform this {from_format} structure to a {to_format} format:\n{data_in_format}",
    ]

    prompt = random.choice(prompts)

    return prompt, response


def main():
    base_file_name = 'format-convertion'
    structured_data_generator = StructuredDataGenerator('names.txt', 'cities.tsv')
    for file_count in range(20):
        output_file = f'./training_data_v2/{base_file_name}-{file_count}.md'
        if os.path.exists(output_file):
            continue
        with open(output_file, 'w', encoding="utf-8") as file:
            for _ in range(200):
                structured_data = structured_data_generator.generate_random_structured_data()
                prompt, response = generate_format_conversion_prompt_and_response(structured_data)
                record = f"{prompt}{response}"
                record = record.replace("\n\n", "\n")
                record = record.replace("\r", "")
                print(record)
                print('-' * 80)
                file.write(record)
                file.flush()


if __name__ == '__main__':
    main()
