import sys

goal = tuple([int(a) for a in input().split(':')])
ratios = []
for line in sys.stdin:
    ratio = []
    for chemical in line.split(':'):
        if chemical == '':
            ratio.append(0)
        else:
            ratio.append(int(chemical))
    ratios.append(ratio)

ratio_count = len(ratios) + 1
equation_count = len(ratios)
matrix = [[0 for _ in range(ratio_count)] for _ in range(equation_count)]
for y in range(ratio_count - 1):
    for x in range(equation_count):
        matrix[y][x] = ratios[x][y]
    matrix[y][-1] = goal[y]

# Use gaussian elimination to get to echelon form:
# leading coefficient is 1
# Each leading coefficient is in a column to the right of the one above it
# Rows with more leading zeroes go after the ones with less
for i in range(equation_count):
    # matrix[i:] = sorted(matrix[i:])  # I don't think I need this, but I will leave it here just in case.
    leading_coefficient = 0
    for m, v in enumerate(matrix[i]):
        if v != 0:
            leading_coefficient = m
            break
    if matrix[i][leading_coefficient] != 1:
        reciprocal = 1 / matrix[i][leading_coefficient]
        for j in range(leading_coefficient, ratio_count):
            matrix[i][j] *= reciprocal
    for k in range(i + 1, equation_count):
        multiplicand = matrix[k][leading_coefficient]
        for j in range(leading_coefficient, ratio_count):
            matrix[k][j] -= matrix[i][j] * multiplicand

# After we have it in echelon form we want to turn it into the reduced row echelon form:
# The leading coefficient in each row is the only non-zero item
for i in range(equation_count - 1):
    start = 0
    for m, v in enumerate(matrix[i]):
        if v == 1:
            start = m + 1
            break
    for j in range(start, ratio_count - 1):
        multiplicand = matrix[i][j]
        for k in range(j, ratio_count):
            matrix[i][k] -= multiplicand * matrix[j][k]

# Once we have it in reduced row echelon form, the rightmost element in each row is the answer.
answers = [a[-1] for a in matrix]
answers = [round((1 / min(answers)) * a) for a in answers]
if min(answers) < 0:  # Maybe < 1?
    print(-1)
else:
    for ans in answers:
        print(ans)
