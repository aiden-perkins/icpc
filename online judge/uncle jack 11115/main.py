import sys

for line in sys.stdin:
    line = line.replace('\n', '').replace('   ', ' ').split(' ')
    if line != ['0', '0']:
        print(int(line[0]) ** int(line[1]))

