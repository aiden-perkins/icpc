import random

print('20')
for i in range(20):
    d = random.randint(3*(10**8), 3*(10**10))
    print(f'30 {d}')
    ns = []
    for j in range(30):
        ns.append(str(random.randint(0, 10**9)))
    print(' '.join(ns))
