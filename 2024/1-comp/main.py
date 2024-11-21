import sys

an2 = []
for line in sys.stdin:
    line = line[:-1]
    ll = line.replace('\t', ' ').split(' ')
    for ii in ll:
        if ii.isnumeric():
            an2.append(int(ii))
# lines = (''.join(sys.stdin.readlines())).replace('\n', ' ').split(' ')
# c = int(lines[0])
# an = [int(a) for a in lines[1:-1]]
an = an2[1:]
ans = set()
for a in range(len(an)):
    for b in range(a + 1, len(an)):
        ans.add(an[a] + an[b])
print((len(an) * (len(an) - 1)) // 2, len(ans))

