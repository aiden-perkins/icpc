import sys
import re
import time
from collections import defaultdict
def parttwo(charpos):
    k = len(charpos)
    eq1 = 0
    eq2 = 0
    #equation 1 of part2
    for i in range(k):
        eq1 += (charpos[i])**2
    eq1 *= (k-1)
    #equation 2 of part2
    S = sum(charpos)
    for i in charpos:
        eq2 += i * (S - i)
    return eq1 - eq2


for line in sys.stdin:
    line = line.replace("\n","").replace("\r","")
    line = re.sub(r"\s+", ' ', line).strip()
    start = time.time()
    #part1
    n = len(line)
    total = (((n**2) * (n + 1) * ((2*n) + 1))/6) - (((n*(n+1))/2)**2)
    positions = defaultdict(list)

    #part2
    for idx in range(n):
        positions[line[idx]].append(idx + 1)

    for k, v in positions.items():
        if len(v) >= 2:
            total -= parttwo(v)
            total = total % (10**6 + 7)

    print(int(total))
    print(time.time() - start)
