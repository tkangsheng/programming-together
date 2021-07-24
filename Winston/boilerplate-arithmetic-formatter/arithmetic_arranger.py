def arithmetic_arranger(problems : list, isSolved = False):
    arranged_problems = list()

    left_operand_line = "" #create_with_left_operands()
    operator_and_right_operand_line = "" #create_with_operator_and_right_operands()
    dash_line = "" #dashes_with_padding(left, right)
    solution_line = "" #answers_with_padding()

    if there_are_too_many_problems(problems):
        return "Error: Too many problems."

    for problem in problems:
        (left, operator, right) = parse(problem)

        if is_division_or_multiplication(operator):
            return "Error: Operator must be '+' or '-'."

        if is_not_number(left) or is_not_number(right):
            return "Error: Numbers must only contain digits."

        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        problem_width = get_problem_width(left, right)
        gap_separating_problems = "    "

        padded_left_operand_line = pad_left(left, problem_width)
        left_operand_line = f"{left_operand_line}{gap_separating_problems}{padded_left_operand_line}"

        padded_operator_and_right_operand_line = pad_left(f"{operator} {right}", problem_width)
        operator_and_right_operand_line = f"{operator_and_right_operand_line}{gap_separating_problems}{padded_operator_and_right_operand_line}"

        dash_line = f"{dash_line}{gap_separating_problems}{'-' * problem_width}"

        if isSolved:
            solution = evaluate(left, operator, right)
            padded_solution_line = pad_left(str(solution), problem_width)
            solution_line = f"{solution_line}{gap_separating_problems}{padded_solution_line}"

    arranged_problems.append(left_operand_line)
    arranged_problems.append(operator_and_right_operand_line)
    arranged_problems.append(dash_line)
    arranged_problems.append(solution_line)

    return '\n'.join(arranged_problems)

def get_problem_width(left : str, right : str) -> int:
    return len("+ ") + max(len(left), len(right))

def pad_left(solution_str : str, problem_width : int):
    number_of_whitespaces = problem_width - len(solution_str)
    white_spaces = ' ' * number_of_whitespaces

    # pads the left side of the solution with whitespace
    solution_with_padding = f'{white_spaces}{solution_str}'
    return solution_with_padding

def there_are_too_many_problems(problems : list):
    return len(problems) > 5

def is_division_or_multiplication(operator : str):
    return operator == '*' or operator == '/'

def is_not_number(operand : str):
    return not str.isnumeric(operand)

def parse(problem : str):
    symbols = problem.split()
    left = symbols[0]
    operator = symbols[1]
    right = symbols[2]
    return (left, operator, right)

def evaluate(left: str, operand: str, right: str) -> str:
    left_number = int(left)
    right_number = int(right)
    if operand == '+':
        return left_number + right_number
    else: # operand == '-'
        return left_number - right_number

answer = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
print(answer)

# (left, operator, right) = parse("32 + 698")
# print(left)
# print(operator)
# print(right)
