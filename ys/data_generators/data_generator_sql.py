# todo: write sql that does
# example sql. We'll use our format classes to generate some data as md, generate sql to query it, then
# generate a prompt. We need to demonstrate how to select, insert, delete, drop, create. We'll keep it
# reasonably simple. Just generating some basic syntax.
from typing import Tuple

from ys.data_generators.factory.structured_data_generator import StructuredDataGenerator
from ys.data_generators.util.generator_harness import generate_training_files
from ys.data_generators.util.ollama_prompter import prompt_ollama
from ys.data_generators.util.tabular_formatter import TabularDataFormatter


def entry_generator() -> Tuple[int, str, str]:
    structured_data_generator = StructuredDataGenerator('names.txt', 'cities.tsv')
    operations = ['SELECT', 'SELECT with a LEFT JOIN', 'SELECT with a RIGHT JOIN', 'SELECT with a INNER JOIN',
                  'SELECT with a FULL JOIN', 'SELECT with a self JOIN', 'SELECT with a like in the WHERE',
                  'SELECT with a is NULL in the WHERE', 'SELECT with a is NOT NULL in the WHERE',
                  'SELECT with HAVING', 'SELECT with a OVER window function', 'SELECT with LAG',
                  'SELECT with LEAD', 'ORDER BY', 'GROUP BY', 'DROP TABLE', 'INSERT', 'DELETE', 'UPDATE',
                  'CREATE TABLE', 'ALTER TABLE']

    file_number: int = 0
    index = 0
    for _ in range(50):
        for operation in operations:
            structured_data = structured_data_generator.generate_random_structured_data()
            formatter = TabularDataFormatter(structured_data)
            md = formatter.to_markdown()
            problem = prompt_ollama(
                f'Generate an example sql problem that requires {operation} that a programmer might ask for help with. Write the problem in the form of a question. Include the relevant details of the table or tables to ensure the problem can be solved with SQL using the correct column and table names. If the problem needs column names or example data, you can use:\n{md}\n\nBeyond the problem, do not provide any comments or acknowledgements.')
            solution = prompt_ollama(problem)
            if index % 200 == 0:
                file_number = file_number + 1
            index += 1
            yield file_number, problem, solution


if __name__ == '__main__':
    generate_training_files("generated-sql", entry_generator)
