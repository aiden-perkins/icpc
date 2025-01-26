import random

n = 2000
queries = 100000
denominations = list(range(1, n + 1))
print(f"{n} {queries}")
print(" ".join(map(str, denominations)))
for i in range(queries):
    if random.randint(1, 100) < 3:
        if len(denominations) > 1:
            d_idx = random.randint(0, len(denominations) - 1)
            print(f'X {denominations[d_idx]}')
            denominations.pop(d_idx)
    else:
        print(f'Q {random.randint(1, 100000)}')
