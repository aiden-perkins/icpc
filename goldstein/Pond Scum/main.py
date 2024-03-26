import sys

ponds = []
for line in sys.stdin:
    line = line[:-1].split(',')
    row = []
    for pond in line:
        if '!' in pond:
            row.append(-1)
        else:
            row.append(int(pond))
    ponds.append(row)

equations = {}
variables_all = []
for i in range(1, len(ponds) - 1):
    for j in range(1, len(ponds[i]) - 1):
        variables_all.append((i, j))
        connected = [0]
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            pipe = ponds[x][y]
            if pipe != -1:
                connected[0] += pipe
            else:
                connected.append((x, y))
        equations[(i, j)] = connected

gaussian = [[0 for _ in range(len(variables_all) + 1)] for _ in equations]
for i, (current, j) in enumerate(equations.items()):
    gaussian[i][-1] = j[0]
    gaussian[i][variables_all.index(current)] = 4
    for n in j[1:]:
        gaussian[i][variables_all.index(n)] -= 1

for i in range(len(gaussian)):
    gaussian[i:] = sorted(gaussian[i:], reverse=True)
    leading_coefficient = 0
    for m, v in enumerate(gaussian[i]):
        if round(v, 10) != 0:
            leading_coefficient = m
            break
    if gaussian[i][leading_coefficient] != 1:
        reciprocal = 1 / gaussian[i][leading_coefficient]
        for j in range(leading_coefficient, len(gaussian[0])):
            gaussian[i][j] *= reciprocal
    for k in range(i + 1, len(gaussian)):
        multiplicand = gaussian[k][leading_coefficient]
        for j in range(leading_coefficient, len(gaussian[0])):
            gaussian[k][j] -= gaussian[i][j] * multiplicand
for i in range(len(gaussian) - 1):
    start = 0
    for m, v in enumerate(gaussian[i]):
        if round(v, 10) == 1:
            start = m + 1
            break
    for j in range(start, len(gaussian[0]) - 1):
        multiplicand = gaussian[i][j]
        for k in range(j, len(gaussian[0])):
            gaussian[i][k] -= multiplicand * gaussian[j][k]

for ans in [a[-1] for a in gaussian]:
    print(round(ans))
