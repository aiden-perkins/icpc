import sys

amount_of_commands = 0
commands = []
games = []
for line in sys.stdin:
    line = line.replace('\n', '')
    if amount_of_commands == 0:
        amount_of_commands = int(line)
    else:
        if line in ['north', 'south', 'east', 'west']:
            commands.append(line)
        else:
            games.append(commands)
            commands = []
            amount_of_commands = int(line)
for game in games:
    die = [1, 2, 3]  # top, north, and west
    for instruction in game:
        old_top = die[0]
        if instruction == 'north':
            # top becomes south
            die[0] = abs(die[1] - 7)
            # north becomes bottom
            die[1] = old_top
        if instruction == 'south':
            # top becomes north
            die[0] = die[1]
            # north becomes top
            die[1] = abs(old_top - 7)
        if instruction == 'west':
            # top becomes east
            die[0] = abs(die[2] - 7)
            # west becomes top
            die[2] = old_top
        if instruction == 'east':
            # top becomes west
            die[0] = die[2]
            # west becomes bottom
            die[2] = abs(old_top - 7)
    print(die[0])
