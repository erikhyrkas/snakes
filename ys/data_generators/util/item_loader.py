import random
from typing import Any

import yaml


def file_to_list(text_file_name: str, shuffle=True) -> list:
    with open(f'./ys/data_generators/{text_file_name}', 'r', encoding='utf-8') as file:
        result_list = [line.strip() for line in file if line.strip()]
        if shuffle:
            random.shuffle(result_list)
        return result_list


def tsv_to_list_of_lists(tsv_file_name: str, shuffle=True) -> list:
    with open(f'./ys/data_generators/{tsv_file_name}', 'r', encoding='utf-8') as file:
        list_of_lists = [line.strip().split('\t') for line in file if line.strip()]
        if shuffle:
            random.shuffle(list_of_lists)
        return list_of_lists


def yaml_to_object(yaml_file_name: str) -> Any:
    with open(f'./ys/data_generators/{yaml_file_name}', 'r') as file:
        result_object = yaml.safe_load(file)
        return result_object
