n, m = list(map(int, input().strip().split()))
color_counts = []
for _ in range(m):
    cic = int(input())
    color_counts.append(cic)
color_counts.sort()
ccmn = color_counts[0]
ccmx = color_counts[-1]

if ccmn in [1, 2]:
    print(1)
elif ccmx == n:
    print(1)
elif ccmx + ccmn - 1 <= n:
    print(1)
else:
    print(2)
