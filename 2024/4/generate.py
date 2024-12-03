
import random
import string

def random_unit_name():
    length = random.randint(1, 20)
    chars = string.ascii_letters + string.digits + '_'
    return ''.join(random.choice(chars) for _ in range(length))

def random_float():
    return round(random.uniform(0, 1000), 3)

# Generate 200,000 lines
n = 199900

# Create a list of unit names to reuse (to ensure conversions are possible)
unit_names = [random_unit_name() for _ in range(100)]

with open('2.in', 'w') as f:
    # Generate n-1 lines (leaving space for the final 'G')
    for i in range(n-1):
        if random.random() < 0.1:  # 60% chance for knowledge lines
            unit1 = random.choice(unit_names)
            unit2 = random.choice(unit_names)
            while unit1 == unit2:  # ensure different units
                unit2 = random.choice(unit_names)

            a = random_float()
            # 50% chance to add offset
            if random.random() < 0.5:
                o = random_float()
                f.write(f'K {unit1} = {a} {unit2} + {o}\n')
            else:
                f.write(f'K {unit1} = {a} {unit2}\n')
        else:  # 40% chance for homework lines
            unit1 = random.choice(unit_names)
            unit2 = random.choice(unit_names)
            x = random_float()
            f.write(f'H {x} {unit1} = ? {unit2}\n')

    # Add the final 'G' line
    f.write('G\n')
