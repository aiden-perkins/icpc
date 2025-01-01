
def gaussian_elimination_mod(a, b, mod):
    n = len(a)
    m = len(a[0])
    nm = [[a[i][j] for j in range(m)] + [b[i]] for i in range(n)]

    rank = 0
    for col in range(m):
        pivot_row = -1
        for row in range(rank, n):
            if nm[row][col] % mod != 0:
                pivot_row = row
                break
        if pivot_row == -1:
            continue
        if pivot_row != rank:
            nm[rank], nm[pivot_row] = nm[pivot_row][:], nm[rank][:]
        pivot = nm[rank][col]
        inv = mod_inverse(pivot, mod)
        if inv is None:
            return None
        for j in range(col, m + 1):
            nm[rank][j] = (nm[rank][j] * inv) % mod
        for i in range(n):
            if i != rank and nm[i][col] != 0:
                factor = nm[i][col]
                for j in range(col, m + 1):
                    nm[i][j] = (nm[i][j] - factor * nm[rank][j]) % mod
        rank += 1
    for i in range(rank, n):
        if nm[i][-1] != 0:
            return None
    return True

n, p = map(int, input().split())
initial = list(map(int, input().split()))
m = int(input())
spells = [list(map(int, input().split())) for _ in range(m)]

def mod_inverse(a, m):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        return gcd, y1 - (b // a) * x1, x1

    gcd, x, _ = extended_gcd(a % m, m)
    if gcd != 1:
        return None
    return x % m

tA = [[-1 for _ in range(m + 1)] for _ in range(n)]
for o, spell in enumerate(spells):
    for w, spv in enumerate(spell):
        tA[w][o] = spv

rv = gaussian_elimination_mod(tA, [a * -1 for a in initial], p)
if rv is None:
    print('Impossible')
else:
    print('Possible')
