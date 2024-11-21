import sys

def is_on_line(x11, y11, sl, yint):
    py = (x11 * sl) + yint
    return round(py, 6) == round(y11, 6)

amount = int(input())

for line in sys.stdin:
    line = line[:-1]
    xs = []
    ll = line.replace('\t', ' ').split(' ')
    for ii in ll:
        if ii.isnumeric() or ii[1:].isnumeric():
            xs.append(int(ii))
    x1, y1, x2, y2, x3, y3, x4, y4 = xs
    n = y1 - y2
    d = x1 - x2
    if d == 0:
        if x1 == x2 and x3 == x4 and x2 == x3:
            print('No')
        else:
            print('Yes')
        continue
    m = n / d
    yint_cept = y1 - (m * x1)
    c3 = is_on_line(x3, y3, m, yint_cept)
    c4 = is_on_line(x4, y4, m, yint_cept)
    if c3 == True and c4 == True:
        print('No')
    else:
        print('Yes')
