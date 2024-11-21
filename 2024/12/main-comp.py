import sys

c = int(input())
for i in range(c):
    n, r = [int(a) for a in input().split(' ')]
    l2 = input().split(' ')
    prod = 1
    for gues in l2:
        if '?' in gues:
            for i in range(1, 10):
                nn = int(gues.replace('?', str(i)))

                print(nn)
