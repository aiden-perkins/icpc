import sys

for line in sys.stdin:
    bc = int(line)
    if bc == 0:
        break
        
    cache = {}
    
    for i in range(1, bc + 2):
        s = 0
        if i-1 in cache:
            s += cache[i-1]
        if i-2 in cache:
            s += cache[i-2]
        
        if i == 0:
            s = 0
        if i == 1:
            s = 1
        
        cache[i] = s
        
    print(cache[bc + 1])
