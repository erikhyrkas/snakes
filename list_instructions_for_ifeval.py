import json


def print_ifeval_instructions():
    path = "benchmark_data/ifeval_input_data.jsonl"
    dataset = []

    with open(path, 'r') as file:
        for line in file:
            data = json.loads(line)
            dataset.append(data)

    all_instructions = dict()
    for record in dataset:
        instructions = record['instruction_id_list']
        instruction_args: list[dict] = record['kwargs']
        arg_names = set()
        for instruction_arg in instruction_args:
            arg_names = arg_names.union(instruction_arg.keys())
        for instruction in instructions:
            existing_args = all_instructions.get(instruction, set())
            existing_args.update(arg_names)
            all_instructions[instruction] = existing_args

    sorted_instructions = sorted(all_instructions)
    for instruction in sorted_instructions:
        instruction_args_as_list = list(all_instructions[instruction])
        sorted_args_as_list = sorted(instruction_args_as_list)
        instruction_args_str = ', '.join(sorted_args_as_list)
        print(f"{instruction}({instruction_args_str})")


if __name__ == '__main__':
    print_ifeval_instructions()

# change_case:capital_word_frequency
# change_case:english_capital
# change_case:english_lowercase
# combination:repeat_prompt
# combination:two_responses
# detectable_content:number_placeholders
# detectable_content:postscript
# detectable_format:constrained_response
# detectable_format:json_format
# detectable_format:multiple_sections
# detectable_format:number_bullet_lists
# detectable_format:number_highlighted_sections
# detectable_format:title
# keywords:existence
# keywords:forbidden_words
# keywords:frequency
# keywords:letter_frequency
# language:response_language
# length_constraints:nth_paragraph_first_word
# length_constraints:number_paragraphs
# length_constraints:number_sentences
# length_constraints:number_words
# punctuation:no_comma
# startend:end_checker
# startend:quotation
