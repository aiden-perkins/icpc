import sys

def r_prime(x, y):
    # x & y are not prime
    factors = []
    for i in range(2, x):
        if x // i == x / i:
            factors.append(x // i)
    for i in range(2, y):
        if y // i == y / i:
            if y // i in factors:
                return False
    return True

def is_prime(num) -> bool:
    for i in range(2, num):
        if num // i == num / i:
            return False
    return True

for line in sys.stdin:
    t = 0
    k = int(line)
    for x in range(1, 2 * k):
        y = ((x ** 2) / (-4 * k)) + k
        if y // 1 == y:
            if is_prime(x) or is_prime(int(y)) or r_prime(x, int(y)):
                t += 1
    print(f'{k} {t}')



