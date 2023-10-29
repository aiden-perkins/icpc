from collections import Counter
import sys

total = -1
for line in sys.stdin:
    if total == -1:
        total = int(line)
    else:
        t = line.split(' ')
        t = [i.replace('\n', '') for i in t]
        c = Counter(t).most_common()
        s_2 = 0
        for i in c[1:]:
            s_2 += i[1]
        who = {
            '1': 'Future One',
            '2': 'Two-gether',
            '3': 'Triple Harmony'
        }
        if s_2 < c[0][1]:
            print(f'{who[c[0][0]]} Dominates')
        else:
            print('Power Balanced')

