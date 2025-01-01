import random

max_knowledge = 190000
for i in range(max_knowledge):
    unit1 = f"unit_{i}"
    unit2 = f"unit_{(i + 1) % max_knowledge}"
    if random.random() < 0.1:
        multiplier = random.uniform(0.5, 2.0)
        if random.random() < 0.3:
            offset = random.uniform(0, 10)
            print(f"K {unit1} = {multiplier:.3f} {unit2} + {offset:.3f}")
        else:
            print(f"K {unit1} = {multiplier:.3f} {unit2}")
    else:
        print(f"K {unit1} = 1.000 {unit2}")
for _ in range(100):
    start_idx = random.randint(0, max_knowledge-1)
    distance = random.randint(max_knowledge//4, max_knowledge//2)
    value = 32.0
    print(f"H {value:.3f} {unit1} = ? {unit2}")
print("G")
