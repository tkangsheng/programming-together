
class Problem:
    left = ''
    right = ''
    operator = ''
    solution = ''

    def set_left(self, left_operand):
        self.left = left_operand
    def set_right(self, right_operand):
        self.right = right_operand

    def join(self, other_problem):
        whitespace = '    '
        new_problem = Problem()
        new_problem.left = whitespace.join([self.left, other_problem.left])
        new_problem.right = whitespace.join([self.right, other_problem.right])
        return new_problem

problem_one = Problem()
problem_one.left = '   32'
problem_one.right = '+ 698'

problem_two = Problem()
problem_two.left = '  3801'

problem_three = Problem()
problem_three = '   45'

result = problem_one.join(problem_two).join(problem_three)
print(result.left)
