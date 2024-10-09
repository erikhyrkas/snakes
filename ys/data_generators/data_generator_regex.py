from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files
from ys.data_generators.util.item_loader import tsv_to_list_of_lists


def entry_generator() -> Tuple[int, str, str]:
    tasks_and_solutions = tsv_to_list_of_lists('regex_tasks.tsv')
    for item in tasks_and_solutions:
        print(f"item: {item}")
        task = item[0]
        solution = item[1]
        yield 1, task, solution


if __name__ == '__main__':
    generate_training_files("generated-regex-tasks", entry_generator)
