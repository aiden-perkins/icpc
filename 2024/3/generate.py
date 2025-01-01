n = 2000
queries = 4000
denominations = list(range(1, n + 1))
print(f"{n} {queries}")
print(" ".join(map(str, denominations)))
for i in range(queries // 2):
    query_value = (i + 1) * 50 + 20000
    print(f"Q {query_value}")
    if i < len(denominations):
        print(f"X {denominations[n - i - 1]}")
