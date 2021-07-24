def arithmetic_arranger(problems : list, findSolution = False):
    arranged_problems : str

    four_lines = list()
    first_line = '' #create_with_left_operands()
    second_line = '' #create_with_operator_and_right_operands()
    third_line = '' #dashes_with_padding(left, right)
    fourth_line = '' #answers_with_padding()

    if there_are_too_many_problems(problems):
        return "Error: Too many problems."

    solutions = list()
    for problem in problems:
        (left, operator, right) = parse(problem)

        if is_division_or_multiplication(operator):
            return "Error: Operator must be '+' or '-'."

        if is_not_number(left) or is_not_number(right):
            return "Error: Numbers must only contain digits."

        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        problem_width = get_problem_width(left, right)

        if findSolution:
            solution = evaluate(left, operator, right)
            solutions.append(solution)
            padded_fourth_line = answers_with_padding(solution, problem_width)
            fourth_line = f'{fourth_line}    {padded_fourth_line}'

    return arranged_problems

def get_problem_width(left, right):
    return 6

def answers_with_padding(solution, problem_width):
    difference = problem_width - len(solution)
    white_spaces = ' ' * difference
    solution_with_padding = f'{white_spaces}{solution}'
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

answer = arithmetic_arranger(["32.1 / 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
print(answer)

# (left, operator, right) = parse("32 + 698")
# print(left)
# print(operator)
# print(right)
