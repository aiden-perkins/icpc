import sys

k1 = int(input())
k2 = int(input())
adj_matrix = []
for line in sys.stdin:
    adj_matrix.append([int(a) for a in line[:-1]])
for i in range(len(adj_matrix)):
    adj_matrix[i][i] = -1
people = list(range(len(adj_matrix)))
while True:
    for i, person in enumerate(adj_matrix):
        if (person.count(0) < k2 or person.count(1) < k1) and i in people:
            adj_matrix[i] = [-1 for _ in person]
            people.remove(i)
            for j in range(len(adj_matrix)):
                adj_matrix[j][i] = -1
            break
    else:
        break
for left in people:
    print(left + 1)
