import sys
from collections import defaultdict
from decimal import Decimal

# Credit to Dr. Todd Ebert for the coming up with the solution and Phu Nguyen for coding the solution
for line in sys.stdin:
    mem = defaultdict(list)
    idx = 1
    for char in line.strip():
        mem[char].append(idx)
        idx += 1

    n = idx - 1
    summation1 = Decimal((Decimal(n**2) * (n+1) * (2 * n + 1)) / 6)
    summation2 = Decimal((Decimal(n * (n+1)) / 2) ** 2)
    total = summation1 - summation2

    subtracted = 0
    for key in mem:
        k = len(mem[key])
        if k <= 1:
            continue
        sum_k = sum(mem[key])
        a = 0
        b = 0
        for i in mem[key]:
            a += i**2
            b += i * (sum_k - i)

        subtracted += (k-1) * a - b
    final_answer = Decimal(total - subtracted) % Decimal(Decimal(10**9) + 7)
    print(final_answer)
