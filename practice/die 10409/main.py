ll = open('input.txt', 'r').read().split('\n')
[1, 2, 3, 4, 5, 6]  # top, north, west, east, south, bottom

p = [0, 0]
for instruction in ll:
    if instruction == 'north':
        p[0] += 1
    if instruction == 'west':
        p[1] -= 1
    if instruction == 'south':
        p[0] -= 1
    if instruction == 'east':
        p[1] += 1
print(p)

