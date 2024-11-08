import sys

count = None
names = None

apbt = list(' abcdefghijklmnopqrstuvwxyz'.upper())

for line in sys.stdin:
    line = line.replace('\n', '').replace('\r', '')
    if line.isnumeric():
        count = int(line)
        names = []
    else:
        names.append(line)

    if len(names) == count and count != 0:
        names.sort()
        half = (count // 2) - 1
        
        on1 = len(names[half])
        on2 = len(names[half + 1])
        
        result = ''
        
        for i, (c1, c2) in enumerate(zip(names[half].ljust(max(on1, on2)), names[half + 1].ljust(max(on1, on2)))):
            c1i = apbt.index(c1)
            c2i = apbt.index(c2)
            
            if c1i == c2i:
                result += c1
            elif c1 == ' ':
                break
            elif c2 == ' ':
                if c1 == 'Z':
                    result += 'Z'
                elif i + 1 == on1:
                    result += c1
                    break
                else:
                    result += apbt[c1i + 1]
                    break
            elif c2i - c1i > 1 and not (i + 1 == on1 and i + 1 == on2):
                if i + 1 == on1:
                    result += apbt[c1i]
                else:
                    result += apbt[c1i + 1]
                break
            elif i + 1 == on2:
                result += c1
            elif i + 1 == on1:
                result += c1
                break
            else:
                result += c2
                break
        print(result)
