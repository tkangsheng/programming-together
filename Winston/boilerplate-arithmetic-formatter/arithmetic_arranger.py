def arithmetic_arranger(problems : list, isSolved : bool = False) -> str:
    arranged_problems = list()

    left_operand_line = [] #create_with_left_operands()
    operator_and_right_operand_line = [] #create_with_operator_and_right_operands()
    dash_line = [] #dashes_with_padding(left, right)
    solution_line = [] #answers_with_padding()

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

        padded_left_operand_line = pad_left(left, problem_width)
        left_operand_line.append(padded_left_operand_line)

        padded_operator_and_right_operand_line = ""
        if (len(right) > len(left)):
            padded_operator_and_right_operand_line = f"{operator} {right}"
        else:
            padded_operator_and_right_operand_line = f"{operator}{pad_left(right, problem_width - len(operator))}"
        operator_and_right_operand_line.append(padded_operator_and_right_operand_line)

        dash_line.append('-' * problem_width)

        if isSolved:
            solution = evaluate(left, operator, right)
            padded_solution = pad_left(str(solution), problem_width)
            solution_line.append(padded_solution)

    gap_separating_problems = "    "

    arranged_problems.append( gap_separating_problems.join(left_operand_line) )
    arranged_problems.append( gap_separating_problems.join(operator_and_right_operand_line) )
    arranged_problems.append( gap_separating_problems.join(dash_line) )
    if isSolved:
        arranged_problems.append( gap_separating_problems.join(solution_line) )

    return '\n'.join(arranged_problems)

def get_problem_width(left : str, right : str) -> int:
    return len("+ ") + max(len(left), len(right))

def pad_left(input_str : str, target_length : int):
    number_of_whitespaces = target_length - len(input_str)
    white_spaces = ' ' * number_of_whitespaces

    # pads the left side of the solution with whitespace
    padded_input_str = f'{white_spaces}{input_str}'
    return padded_input_str

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

def evaluate(left: str, operator: str, right: str) -> int:
    left_number = int(left)
    right_number = int(right)
    if operator == '+':
        return left_number + right_number
    else: # operand == '-'
        return left_number - right_number

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
