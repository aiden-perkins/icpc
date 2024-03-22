from collections import defaultdict
import sys

n, r, w, h = [float(a) for a in input().split(',')]
gems = []
for line in sys.stdin:
    gems.append(tuple(float(a) for a in line.split(',')))
adj_list = defaultdict(list)
gems.sort(key=lambda x: x[1])
for i in range(len(gems) - 1, -1, -1):
    current = gems[i]
    for j in range(i + 1, len(gems)):
        possible_edge = gems[j]
        if (possible_edge[1] - current[1]) / r >= abs(current[0] - possible_edge[0]):
            adj_list[i].append(j)
finished = {}
for i in range(len(gems) - 1, -1, -1):
    gem_max = gems[i][2]
    gem_idx = []
    for edge in adj_list[i]:
        if finished[edge][0] + gems[i][2] > gem_max:
            gem_max = finished[edge][0] + gems[i][2]
            gem_idx = [edge] + finished[edge][1]
    finished[i] = (gem_max, gem_idx)
finished = list(tuple(finished.items()))
finished.sort(key=lambda x: x[1][0])
path = [finished[-1][0]] + finished[-1][1][1]
for gem in path:
    i, j, v = gems[gem]
    print(f'{i},{j},{v}')
