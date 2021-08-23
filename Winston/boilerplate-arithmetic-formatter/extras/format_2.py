import numpy

problems = [
    [
        '   32',
        '+ 698',
        '-----',
        '  730'
    ],
    [
        '  3801',
        '-    2',
        '------',
        '  3799'
    ]
]

# matrix = numpy.transpose(matrix)

whitespace = 4*' '
next_line_char = '\n'

left = []
right = []
dash = []
solution = []
for problem in problems:
    left.append(problem[0])
    right.append(problem[1])
    dash.append(problem[2])
    solution.append(problem[3])

left = whitespace.join(left)
right = whitespace.join(right)
dash = whitespace.join(dash)
solution = whitespace.join(solution)

result = next_line_char.join([left, right, dash, solution])
print(result)
