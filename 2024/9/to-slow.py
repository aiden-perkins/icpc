from fractions import Fraction
from decimal import Decimal

s = input().replace('\r', '').replace('\n', '')

cs = {}

for l in 'abcdefghijklmnopqrstuvwxyz'.upper():
    cs[l] = [0, 0, 0]

ans = 0
for i in range(len(s)):
    ans += Fraction(i * (i+1) * (2 * i+1), 6)

ans = int(ans)
to_sub = 0
for c in s:
    to_sub += cs[c][0]

    cs[c][2] += 1

    for cc in cs:
        cs[cc][1] += cs[cc][2]
        cs[cc][0] += cs[cc][1]

    cs[c][2] += 1

print(Decimal(ans - to_sub) % Decimal((10 ** 9) + 7))
