
runs = int(input())

for i in range(runs):
    
    cc = {
        'TTT': 0,
        'TTH': 0,
        'THT': 0,
        'THH': 0,
        'HTT': 0,
        'HTH': 0,
        'HHT': 0,
        'HHH': 0,
    }
    first = int(input())
    combos = input()
    
    for j in range(38):
        cc[combos[j:j+3]] += 1
    
    print(f'{i + 1} ' + ' '.join([str(a) for a in cc.values()]))
    
    
