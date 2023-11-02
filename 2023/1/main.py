from collections import Counter
import sys

for line in sys.stdin:
    cost_i = Counter(line)['D']
    pos = [0, 0]
    direction_m = {
        'N': (1, 0),
        'S': (-1, 0),
        'E': (0, 1),
        'W': (0, -1),
    }
    current_d = 'N'
    d_left = {
        'N': 'W',
        'S': 'E',
        'E': 'N',
        'W': 'S'
    }
    d_right = {
        'N': 'E',
        'S': 'W',
        'E': 'S',
        'W': 'N'
    }
    for instruc in list(line):
        if instruc == 'D':
            pos[0] += direction_m[current_d][0]
            pos[1] += direction_m[current_d][1]
        if instruc == 'L':
            current_d = d_left[current_d]
        if instruc == 'R':
            current_d = d_right[current_d]
    fastest = abs(pos[0]) + abs(pos[1])
    if fastest == cost_i:
        print('fair fare')
    else:
        print(f'overpaid by {cost_i - fastest}')
