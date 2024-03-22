import sys

k1 = int(input())
k2 = int(input())
adj_matrix = []
for line in sys.stdin:
    adj_matrix.append([int(a) for a in line[:-1]])
print(len(adj_matrix))
to_remove = []
for i, p in enumerate(adj_matrix):
    if p.count(0) - 1 < k2 or p.count(1) < k1:
        to_remove.append(i)
for i in to_remove:
    del adj_matrix[i]
[print(a) for a in adj_matrix]
