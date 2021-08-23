import numpy

problems = [
    {
        'left': '   32',
        'right': '+ 698',
        'dash': '-----',
        'solution': '  730'
    },
    {
        'left': '  3801',
        'right': '-    2',
        'dash': '------',
        'solution': '  3799'
    }
]

# matrix = numpy.transpose(matrix)

whitespace = 4*' '
next_line_char = '\n'

left = []
right = []
dash = []
solution = []
for problem in problems:
    left.append(problem['left'])
    right.append(problem['right'])
    dash.append(problem['dash'])
    solution.append(problem['solution'])

left = whitespace.join(left)
right = whitespace.join(right)
dash = whitespace.join(dash)
solution = whitespace.join(solution)

result = next_line_char.join([left, right, dash, solution])
print(result)
