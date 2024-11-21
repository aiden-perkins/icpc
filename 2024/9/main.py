s = input().replace('\r', '').replace('\n', '')

cs = {}

"""

This is broken and doesn't work, but the idea behind it should allow me to solve it.

"""

ans = 0
for i, c in enumerate(s):
    round_potential = int(i * (i+1) * (2 * i+1) / 6)

    if c in cs:
        round_potential -= cs[c][0]
    ans += round_potential

    if c not in cs:
        cs[c] = [0, 0, 1]
    else:
        cs[c][2] += 1

    for cc in cs:
        cs[cc][1] += cs[cc][2]
        cs[cc][0] += cs[cc][1]

    cs[c][2] += 1

print(ans % ((10 ** 9) + 7))
