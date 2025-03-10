import random
from typing import Tuple

from ys.data_generators.factory.structured_data_generator import StructuredDataGenerator
from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.ollama_prompter import prompt_ollama
from ys.data_generators.util.tabular_formatter import TabularDataFormatter, pick_random_file_format


def entry_generator() -> Tuple[str, str]:
    structured_data_generator = StructuredDataGenerator('names.txt', 'cities.tsv')

    while True:
        structured_data = structured_data_generator.generate_random_structured_data()
        formatter = TabularDataFormatter(structured_data)
        file_format = pick_random_file_format()
        formatted_data: str = formatter.to(file_format)
        unstructured_data = prompt_ollama(
            f"Write one or more paragraphs of text that leverages all of the data within this {file_format} file. The goal of this report is to capture all of the details (pay extra attention to making sure all numbers are captures exactly), but in plain English rather than as structured data. Respond only with the requested text. Do not provide any other acknowledgements (like 'Here is the text that leverages all of the data' or similar unnecessary text) or other comments beyond the text necessary to convert the structured data to unstructured text.\n\n{file_format} file:\n```\n{formatted_data}\n```")

        if "markdown" == file_format:
            output_description = f"a markdown table"
        elif 'plain text' == file_format:
            output_description = f"a plain text table"
        else:
            output_description = random.choice([f"a {file_format} file", f"{file_format} formated data"])
        create_or_generate = random.choice(['Create', 'Generate'])
        optional_following = random.choice(['following ', ''])
        prompt: str = f"{create_or_generate} {output_description} from the {optional_following}text:\n```\n{unstructured_data}\n```"
        yield prompt, formatted_data


if __name__ == '__main__':
    generate_training_files_v2("generated-extract", entry_generator)
