s = input().replace('\r', '').replace('\n', '')

cs = {}

"""

THIS WILL NOT PASS THE COMPETITION TESTS

The competition needs this to run in under 3 seconds, this python code runs in
9 seconds on a maxed input using the optimized algorithm!

I extremely disagree with how this problem was desgined, all problems should
be able to be solved in any language, and the fact that this isn't, and the
fact that this was the 4th easiest problem, shows how bad all the problems
in this competition were.

There may be problems in this code so I can't say its perfect, but I just
don't care enough anymore.

"""

ans = 0
for i, c in enumerate(s):
    print(ans)
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
