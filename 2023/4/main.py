import sys
import math

p = False
participants = []
tt = []
for line in sys.stdin:
    line = line.replace('\n', '').split(' ')
    if not p:
        p, m, b, s = [int(a) for a in line]
    elif len(participants) < p:
        line = [int(a) for a in line]
        for i in range(0, len(line), 2):
            # Index 0 is ID, 1 is their age, 2 is shares, 3 is if their shares should count towards the dead pool,
            # and 4 is if they are alive or not. This would be so much easier to read if I used OOP.
            participants.append([len(participants) + 1, s - line[i], line[i + 1], True, True])
        if len(participants) == p:  # Making the tontines
            participants.sort(key=lambda a: a[1])
            c_a = 50
            t = []
            for person in participants:
                if person[1] in range(c_a, c_a + b):
                    t.append(person)
                else:
                    # This extra append is to keep track of the dead shares & how many people are alive.
                    t.append([0, len(t)])
                    tt.append(t)
                    t = [person]
                    c_a += b
            t.append([0, len(t)])
            tt.append(t)
    else:
        pct, died, who = None, None, []
        line = [float(a) for a in line]
        for idx in range(len(line) + 1):
            if pct is None:
                pct = line[idx]
            elif died is None:
                died = int(line[idx])
            elif len(who) < died:
                who.append(int(line[idx]))
            else:  # If we get here then we can calculate the next year payouts.
                for i, age_group in enumerate(tt):
                    alive_shares = 0
                    alive_c = 0
                    for j, person in enumerate(age_group):
                        if len(person) == 2:  # Ignore our tracker at the end of the age_group list.
                            continue
                        if person[0] in who:
                            if tt[i][len(age_group) - 1][1] > m:
                                # Decrease the amount of alive people.
                                tt[i][len(age_group) - 1][1] -= 1
                                # Increase the dead shares tracker.
                                tt[i][len(age_group) - 1][0] += person[2]
                                # Set if their shares should count to false.
                                tt[i][j][3] = False
                            # Set them from alive to dead.
                            tt[i][j][4] = False
                        if person[3]:
                            # We only want people whose shares should count to be added.
                            alive_shares += person[2]
                        if person[4]:
                            # This is so we know if everyone is dead in the age_group.
                            alive_c += 1
                    if alive_c != 0:
                        raw = ((age_group[len(age_group) - 1][0] * pct) / alive_shares) + pct
                        print(f'{s} {i + 1} {math.trunc(int(raw * 1000) / 10) / 100:.2f}')
                s += 1
                pct, died, who = None, None, []
                if len(line) != idx:
                    pct = line[idx]
