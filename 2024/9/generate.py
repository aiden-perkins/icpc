import random

abcs = 'abcdefghijklmnopqrstuvwxyz'.upper()

s = ''

for i in range(10 ** 6):
    # s += abcs[random.randint(0, 25)]
    s += 'Z'

f = open('6.in', 'w')
f.write(s + '\n')
f.close()
