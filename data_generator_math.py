import random


# a bunch of basic math, just so it has seen it.

data_counter = 0
def generate_simple_math_word_problem_type_1(op1, num1, num2):
    # Create the problem string
    word_problem = f"{number_to_text(num1)} {math_operator_to_text(op1)} {number_to_text(num2)}"
    question = f"What is {word_problem}?"
    # Evaluate the problem step by step
    step1 = None
    try:
        step1 = eval(f"{num1} {op1} {num2}")
        if op1 == '/':
            if float(step1).is_integer():
                step1 = f"{int(step1)}"
            else:
                step1 = f"{float(step1):.3f}"
    except ZeroDivisionError:
        pass
    # Formatting the question and answer
    if step1 is None:
        answer_text = f"```\nStep 1:\nIt is not possible to divide by zero\nFinal Answer:\nUnsolvable\n```\n\nUnsolvable"
    else:
        answer_text = f"```\nStep 1:\n{num1} {op1} {num2} = {step1}\n" \
                      f"Final Answer:\n{step1}\n```\n\n{step1}"

    print(f"{question}\n{answer_text}")
    return {"Request": question, "Response": answer_text}


def generate_complex_math_problem_type_1(op1, op2, num1, num2, num3):
    # Create the problem string
    problems = [
        f"({num1} {op1} {num2}) {op2} {num3}",
        f"{num3} {op2} ({num1} {op1} {num2})"
    ]
    problem_index = random.randint(0, 1)
    problem = problems[problem_index]
    question = f"What is {problem}?"
    # Evaluate the problem step by step
    step1 = None
    answer = None
    problem_answer_text = "divides by zero"
    try:
        step1 = eval(f"{num1} {op1} {num2}")
        if op1 == '/':
            if float(step1).is_integer():
                step1 = f"{int(step1)}"
            else:
                step1 = f"{float(step1):.3f}"
        problem_answer_math = [
            f"{step1} {op2} {num3}",
            f"{num3} {op2} {step1}"
        ]
        problem_answer_text = problem_answer_math[problem_index]
        answer = eval(problem_answer_text)
        if op1 == '/' or op2 == '/':
            if float(answer).is_integer():
                answer = f"{int(answer)}"
            else:
                answer = f"{float(answer):.3f}"
    except ZeroDivisionError:
        pass
    # Formatting the question and answer
    if step1 is None:
        answer_text = f"```\nStep 1:\nSolve the parentheses:\n" \
                      f"{num1} {op1} {num2}\n" \
                      f"However, it is not possible to divide by zero\nFinal Answer:\nUnsolvable\n```\n\nUnsolvable"
    elif answer is None:
        answer_text = f"```\n\nStep 1:\nSolve the parentheses:\n" \
                      f"{num1} {op1} {num2} = {step1}\n" \
                      f"Step 2:\n{problem_answer_text}, but it is not possible to divide by zero\n" \
                      "Final Answer:\nUnsolvable\n```\n\nUnsolvable"
    else:
        answer_text = f"```\nStep 1:\nSolve the parentheses:\n" \
                      f"{num1} {op1} {num2} = {step1}\n" \
                      f"Step 2:\n{problem_answer_text} = {answer}\nFinal Answer:\n{answer}\n```\n\n{answer}"

    print(f"{question}\n{answer_text}")
    return {"Request": question, "Response": answer_text}


def generate_boolean_logic_problem(num1, num2, comparison_operator, logic_operator):
    # Generate two boolean expressions
    num3 = num1 - random.randint(-10, 10)
    num4 = num2 - random.randint(-10, 10)
    if random.choice([True, False]):
        num1 += (random.randint(0, 999) / 1000)
        num2 += (random.randint(0, 999) / 1000)
        num3 += (random.randint(0, 999) / 1000)
        num4 += (random.randint(0, 999) / 1000)
    expression1 = f"{num1} {comparison_operator} {num2}"
    expression2 = f"{num3} {comparison_operator} {num4}"
    full_expression = f"{expression1} {logic_operator} {expression2}"
    question = f"What is the result of {full_expression}?"

    # Evaluate each part of the expression
    try:
        step1 = eval(expression1)
        step2 = eval(expression2)
        answer = eval(full_expression)
    except Exception as e:
        return {"Request": question, "Response": f"Error: {str(e)}"}

    # Formatting the question and answer with steps
    answer_text = f"```\nStep 1:\nEvaluate the first part:\n{expression1} = {step1}\n" \
                  f"Step 2:\nEvaluate the second part:\n{expression2} = {step2}\n" \
                  f"Step 3:\nCombine the results with '{logic_operator}':\n" \
                  f"{step1} {logic_operator} {step2} = {answer}\nFinal Answer:\n{answer}\n```\n\n{answer}"

    print(f"{question}\n{answer_text}")
    return {"Request": question, "Response": answer_text}


def skip(num1, num2):
    # # don't skip numbers -100->100, otherwise skip 98% of the time.
    # if -11 < num1 < 11 and -11 < num2 < 11:
    #     return random.randint(0, 10) < 9
    return random.randint(0, 10000) != 10000


def save_data(data, filename):
    global data_counter
    data_counter += 1
    file_ext = data_counter // 2000
    with open(f"{filename}-{file_ext}", 'a', encoding='utf-8') as f:
        f.write(data)


def save_entries(file_name: str, entries: list):
    for entry in entries:
        next_text = f'{entry["Request"]}<start>{entry["Response"]}<end>\n'
        save_data(next_text, file_name)
        print(next_text)


def number_to_text(n):
    # Define mappings for numbers
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    # Convert number to int and handle negative numbers
    n = int(n)
    negative = False
    if n < 0:
        negative = True
        n = -n

    # Check for specific cases
    if n == 0:
        return "zero"

    # General case
    text = ""
    if n >= 1000:
        text += ones[n // 1000] + "-thousand"
        n = n % 1000
        if n > 0:
            text += "-"

    if n >= 100:
        text += ones[n // 100] + "-hundred"
        n = n % 100
        if n > 0:
            text += "-"

    if n >= 20:
        text += tens[n // 10]
        n = n % 10
        if n > 0:
            text += "-" + ones[n]
    elif n > 0:
        text += teens[n - 10] if n > 9 else ones[n]

    return "negative " + text if negative else text


def math_operator_to_text(operator):
    operator_dict = {
        '+': 'plus',
        '-': 'minus',
        '*': 'multiplied by',
        '/': 'divided by'
    }

    return operator_dict.get(operator, "unknown operator")


def learn_math(file_path: str):
    entry_pairs = []
    comparison_operators = ['<', '>', '==', '!=', '>=', '<=']
    logic_operators = ['and', 'or']
    for num1 in range(-999, 1000):
        for num2 in range(-999, 1000):
            for comparison_operator in comparison_operators:
                for logic_operator in logic_operators:
                    if skip(num1, num2):
                        continue
                    entry_pairs.append(generate_boolean_logic_problem(num1, num2, comparison_operator, logic_operator))
                    if len(entry_pairs) > 1000:
                        save_entries(file_path, entry_pairs)
                        entry_pairs = []

    operations = ['+', '-', '*', '/']
    for op1 in operations:
        for num1 in range(-999, 1000):
            for num2 in range(-999, 1000):
                if skip(num1, num2):
                    continue
                entry_pairs.append(generate_simple_math_word_problem_type_1(op1, num1, num2))
    for op1 in operations:
        for op2 in operations:
            for num1 in range(-100, 101):
                for num2 in range(-100, 101):
                    for num3 in range(-100, 101):
                        if random.randint(0, 10000) != 10000:
                            continue
                        entry_pairs.append(generate_complex_math_problem_type_1(op1, op2, num1, num2, num3))
                        if len(entry_pairs) > 1000:
                            save_entries(file_path, entry_pairs)
                            entry_pairs = []
    save_entries(file_path, entry_pairs)


if __name__ == '__main__':
    learn_math(".\\training_data\\step-by-step-math.md")
