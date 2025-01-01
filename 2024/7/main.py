N = int(input())
C = int(input())
char_def = {}
for _ in range(C):
    char, *segId = input().strip()
    char_def[char] = set(segId)
K = int(input())
R = int(input())
not_burned = [set()] * K
readingss = []
for _ in range(R):
    readings = input().strip().split(',')
    readingss.append(readings)
    for i, reading in enumerate(readings):
        not_burned[i] = not_burned[i].union(set(reading))

for readings in readingss:
    for i, reading in enumerate(readings):
        poss = set()
        for ch, ch_set in char_def.items():
            if set(reading).issubset(ch_set):
                if not ch_set.difference(set(reading)).intersection(not_burned[i]):
                    poss.add(ch)
        print(''.join(sorted(list(poss))), end=' ')
    print()
