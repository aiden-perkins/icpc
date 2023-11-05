import math

p, m, b, s = [int(a) for a in input().split(' ')]
people = {}
while len(people) < p:
    line = [int(a) for a in input().split(' ')]
    for i in range(0, len(line), 2):
        people[len(people) + 1] = [s - line[i], line[i + 1]]
age_groups = {}
for p_id in people:
    person = people[p_id]
    group = ((person[0] - 50) // b) + 1
    if group not in age_groups:
        age_groups[group] = [
            person[1],  # This is the total shares that the investors have.
            0,  # This is the total shares that will be distributed to the other investors.
            [p_id]  # This list is the people alive in the tontine, so we know when to stop payouts.
        ]
    else:
        age_groups[group][0] += person[1]
        age_groups[group][2].append(p_id)
while True:
    pct, died, who = None, None, []
    try:
        line = [float(a) for a in input().split(' ')]
    except EOFError:
        break
    for idx in range(len(line) + 1):
        if pct is None:
            pct = line[idx]
        elif died is None:
            died = int(line[idx])
        elif len(who) < died:
            who.append(int(line[idx]))
        else:
            # This is when we actually calculate the percentage for the payout.
            for group_number in age_groups:
                for dead_person in who:
                    if dead_person in age_groups[group_number][2]:
                        if len(age_groups[group_number][2]) > m:
                            shares = people[dead_person][1]
                            age_groups[group_number][0] -= shares
                            age_groups[group_number][1] += shares
                        age_groups[group_number][2].remove(dead_person)
                if len(age_groups[group_number][2]) > 0:
                    raw = ((age_groups[group_number][1] * pct) / age_groups[group_number][0]) + pct
                    print(f'{s} {group_number} {math.trunc(int(raw * 1000) / 10) / 100:.2f}')
            s += 1
            pct, died, who = None, None, []
            if len(line) != idx:
                pct = line[idx]
