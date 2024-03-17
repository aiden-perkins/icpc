import sys
from collections import defaultdict


def parse_key_word(instruction):
    if instruction == 'halt':
        return ('halt',)
    if instruction.startswith('show'):
        return tuple(instruction.split())
    instruction = instruction.split()
    return instruction[0], instruction[1], ' '.join(instruction[2:])


labels = {}
instructions = []
idx = 0
for line in sys.stdin:
    line = line[:-2].strip()
    if len(line) == 0 or line.startswith('*'):
        continue
    if ': ' in line:
        line = line.split(': ')
        prsed = parse_key_word(line[1])
        labels[line[0]] = (prsed, idx)
        instructions.append(prsed)
    else:
        instructions.append(parse_key_word(line))
    idx += 1

keyword_exec = {
    'set': 'varis[x[1]] = int(eval(x[2], {}, varis))',
    'show': 'print(varis[x[1]])',
}
keyword_eval = {
    'gotoifz': lambda i: int(eval(i[0][2], {}, i[1])) == 0,
    'gotoifm': lambda i: int(eval(i[0][2], {}, i[1])) < 0,
    'gotoifp': lambda i: int(eval(i[0][2], {}, i[1])) > 0,
}


def perform_instruction(instrs, c_i, varis):
    x = instrs[c_i]
    if x[0] == 'halt':
        return
    if x[0].startswith('gotoif'):
        if keyword_eval[x[0]]((x, varis)):
            perform_instruction(instrs, labels[x[1]][1], varis)
        else:
            perform_instruction(instrs, c_i + 1, varis)
    else:
        exec(keyword_exec[x[0]])
        perform_instruction(instrs, c_i + 1, varis)


perform_instruction(instructions, 0, defaultdict(int))
