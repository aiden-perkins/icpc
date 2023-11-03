import sys
import math

tests = 0
for line in sys.stdin:
    line = line.replace('\n', '')
    if tests == 0:
        tests = int(line)
    else:
        n = int(line)
        print(math.ceil((n/2 - 1) * n/2))
