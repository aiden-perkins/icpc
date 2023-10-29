import copy
import sys
import math

bookings = {}
for i in range(1, 37):
    bookings[i] = []
m = {
    'N': [0, 0.5, 0, 0],
    'S': [0, 0, 0, 0.5],
    'W': [0, 0, 0.5, 0],
    'E': [0.5, 0, 0, 0],
}
mmm = {
    1: 3,
    2: 0,
    3: 1,
    0: 2
}
for line in sys.stdin:
    info = line.split(' SECTION ')
    s_n = int(info[1])
    parts = info[0].split(' of ')
    s = [0, 0, math.sqrt(640), math.sqrt(640)]
    parts.reverse()
    for part in parts:
        s_old = copy.deepcopy(s)
        if '1/2' in part:
            for j, crd in enumerate(s):
                s[j] += (s_old[mmm[j]] / 2)
        if '1/4' in part:
            for j, crd in enumerate(s):
                s[j] += (s_old[mmm[j]] / 2)
    if s not in bookings[s_n]:
        t = 1
        t *= s[2] - s[0]
        t *= s[3] - s[1]
        print(f'{s_n} {t // 1} ACRES')
        bookings[s_n].append(s)
    else:
        print('OVERLAPS')

# NE1/4 SECTION 1
