import sys
from collections import defaultdict
from heapq import heappop, heappush

current_graph = defaultdict(list)
equations = defaultdict(dict)

for line in sys.stdin:
    line = line[:-1]
    line = line.split(' ')
    idxs = []
    action = line[0]
    if action == 'K':
        unit = line[1]
        val = float(line[3])
        unit2 = line[4]
        extra = 0
        if len(line) > 5:
            extra = float(line[6])
            sign = line[5]
        if sign == '-':
            extra *= -1

        equations[unit][unit2] = (val, extra)
        equations[unit2][unit] = (1/val, (extra * -1) / val)
        current_graph[unit].append(unit2)
        current_graph[unit2].append(unit)

    elif action == 'H':
        v1 = float(line[1])
        n1 = line[2]
        n2 = line[5]

        queue = [([], n1)]
        distance_mins = defaultdict(lambda: float('inf'))
        while queue:
            current_cost, current_unit = heappop(queue)
            if current_unit == n2:
                queue = []
            for new_unit in current_graph[current_unit]:
                new_cost = current_cost + [new_unit]
                if new_unit not in distance_mins or len(new_cost) < len(distance_mins[new_unit]):
                    distance_mins[new_unit] = new_cost
                    if new_unit == n2:
                        queue = []
                    heappush(queue, (new_cost, new_unit))
        if n2 not in distance_mins:
            print('Too hard!')
        else:
            ov = n1
            for nu in distance_mins[n2]:
                mf, ex = equations[nu][ov]
                v1 *= mf
                v1 += ex
                ov = nu
            print(v1)

    else:
        exit(0)
