import sys
from itertools import combinations

total_players = int(input())
field_players = int(input())
jerseys = []
for _ in range(total_players):
    jerseys.append(int(input().split(',')[0]))
key_set = []
for line in sys.stdin:
    line = line.split()
    key_set.append((set([jerseys.index(a) for a in [int(a) for a in line[2:]]]), int(line[0])))
eligible = []
possible = [set(a) for a in combinations(list(range(total_players)), field_players)]
for idx, p1 in enumerate(possible):
    for p2 in possible[idx + 1:]:
        if len(p1.union(p2)) == total_players:
            eligible.append((p1, p2))
mx = 0
for p1, p2 in eligible:
    p1_skill = 0
    p2_skill = 0
    for p_set, skill_v in key_set:
        if len(p1.intersection(p_set)) == len(p_set):
            p1_skill += skill_v
        if len(p2.intersection(p_set)) == len(p_set):
            p2_skill += skill_v
    if p1_skill + p2_skill > mx:
        mx = p1_skill + p2_skill
print(mx * 2)
