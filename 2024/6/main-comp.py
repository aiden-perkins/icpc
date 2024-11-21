import sys
from itertools import permutations, filterfalse

def comb(w1, w2):
    cii = 0
    cl = []
    while cii <= len(w1) and cii <= len(w2):
        if w1[-cii:] == w2[:cii]:
            cl.append(cii)
        cii += 1

    sa = []
    for k in cl:
        sa.append(w1 + w2[k:])
    resul = []
    for vv in sa:
        if len(vv) == len(w1) + len(w2):
            resul.append(False)
        resul.append(vv)
    return resul

words = []
c = int(input())
for line in sys.stdin:
    line = line[:-1]
    words.append(line)

possible = []
for perm in permutations(words):
    cur = perm[0]
    failed = False
    all_curs = [cur]
    for v in perm[1:]:
        nac = []
        for pc in all_curs:
            rr = comb(pc, v)
            nac += list(filter(None, comb(pc, v)))
        all_curs = nac
    possible += all_curs

p = set(possible)

mn = float('inf')
vs = []
for pn in p:
    if len(pn) < mn:
        mn = len(pn)
        vs = [pn]
    elif len(pn) == mn:
        vs.append(pn)

vs.sort()
if len(vs) == 0:
    print('-1')
else:
    print(vs[0])
