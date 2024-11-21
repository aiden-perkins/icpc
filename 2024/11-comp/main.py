c = int(input())
for i in range(c):
    word = set(list(input().lower()))
    abb = set(list(input().lower()))
    ans = len(word.intersection(abb))
    if ans != len(abb):
        print('NO')
    else:
        print('YES')
