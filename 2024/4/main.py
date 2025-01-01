import sys
from collections import defaultdict
from fractions import Fraction

set_groups = defaultdict(dict)
known_units = {}

for line in sys.stdin:
    line = line.strip().split(' ')
    action, *line = line
    if action == 'K':
        name1, _eq, a, name2, *line = line
        a = Fraction(a)
        o = Fraction(0)
        if line:
            sign, o = line
            o = Fraction(o)
            if sign == '-':
                o *= -1

        if name1 not in known_units and name2 not in known_units:
            set_groups[name1][name2] = (a, o)
            set_groups[name1][name1] = (Fraction(1), Fraction(0))
            known_units[name1] = name1
            known_units[name2] = name1

        elif name1 in known_units and name2 not in known_units:
            name1_base = known_units[name1]
            name1_a, name1_o = set_groups[name1_base][name1]
            set_groups[name1_base][name2] = (name1_a * a, (name1_a * o) + name1_o)
            known_units[name2] = name1_base

        elif name1 not in known_units and name2 in known_units:
            name2_base = known_units[name2]
            name2_a, name2_o = set_groups[name2_base][name2]
            if name2 in set_groups:
                set_groups[name2_base][name1] = (Fraction(1, a), ((o * -1) * Fraction(1, a)))
            else:
                set_groups[name2_base][name1] = (name2_a * Fraction(1, a), (-1 * (o * name2_a)) + name2_o)
            known_units[name1] = name2_base

        else:
            new_name = name1
            new_base = known_units[name1]
            old_name = name2
            old_base = known_units[name2]
            old_to_new_ratio = a
            old_to_new_extra = o

            if len(set_groups[new_base]) < len(set_groups[old_base]):
                new_base, old_base = old_base, new_base
                new_name, old_name = old_name, new_name
                old_to_new_ratio = Fraction(1, a)
                old_to_new_extra = (o * -1) * Fraction(1, a)

            if new_name == new_base and old_name == old_base:
                for unit, (a, o) in set_groups[old_base].items():
                    new_a = a * old_to_new_ratio
                    new_o = (a * old_to_new_extra) + o
                    set_groups[new_base][unit] = (new_a, new_o)
                    known_units[unit] = new_base

            elif new_name == new_base and old_name != old_base:
                old_base_to_old_name_a, old_base_to_old_name_o = set_groups[old_base][old_name]
                old_base_to_old_name_a = Fraction(1, old_base_to_old_name_a)
                old_base_to_old_name_o = (old_base_to_old_name_o * -1) * Fraction(1, old_base_to_old_name_a)

                for unit, (a, o) in set_groups[old_base].items():
                    if unit != old_name:
                        intermediate_a = a * old_base_to_old_name_a
                        intermediate_o = (a * old_base_to_old_name_o) + o
                        new_a = intermediate_a * old_to_new_ratio
                        new_o = (intermediate_a * old_to_new_extra) + intermediate_o
                        set_groups[new_base][unit] = (new_a, new_o)
                        known_units[unit] = new_base
                    else:
                        set_groups[new_base][unit] = (old_to_new_ratio, old_to_new_extra)
                        known_units[unit] = new_base

            elif new_name != new_base and old_name == old_base:
                new_name_to_new_base_a, new_name_to_new_base_o = set_groups[new_base][new_name]

                for unit, (a, o) in set_groups[old_base].items():
                    intermediate_a = a * old_to_new_ratio
                    intermediate_o = (a * old_to_new_extra) + o
                    new_a = intermediate_a * new_name_to_new_base_a
                    new_o = (intermediate_a * new_name_to_new_base_o) + intermediate_o
                    set_groups[new_base][unit] = (new_a, new_o)
                    known_units[unit] = new_base

            else:
                old_base_to_old_name_a, old_base_to_old_name_o = set_groups[old_base][old_name]
                old_base_to_old_name_a = Fraction(1, old_base_to_old_name_a)
                old_base_to_old_name_o = (old_base_to_old_name_o * -1) * Fraction(1, old_base_to_old_name_a)
                new_name_to_new_base_a, new_name_to_new_base_o = set_groups[new_base][new_name]

                for unit, (a, o) in set_groups[old_base].items():
                    if old_name != unit:
                        intermediate_a1 = a * old_base_to_old_name_a
                        intermediate_o1 = (a * old_base_to_old_name_o) + o
                        intermediate_a2 = intermediate_a1 * old_to_new_ratio
                        intermediate_o2 = (intermediate_a1 * old_to_new_extra) + intermediate_o1
                        new_a = intermediate_a2 * new_name_to_new_base_a
                        new_o = (intermediate_a2 * new_name_to_new_base_o) + intermediate_o2
                        set_groups[new_base][unit] = (new_a, new_o)
                        known_units[unit] = new_base
                    else:
                        new_a = old_to_new_ratio * new_name_to_new_base_a
                        new_o = (old_to_new_ratio * new_name_to_new_base_o) + old_to_new_extra
                        set_groups[new_base][unit] = (new_a, new_o)
                        known_units[unit] = new_base

            set_groups.pop(old_base)

    elif action == 'H':
        x, name1, _eq, _qm, name2 = line
        x = Fraction(x)

        ans = None
        if name1 in known_units and name2 in known_units:
            name1_base = known_units[name1]
            name2_base = known_units[name2]
            name1_a, name1_o = set_groups[name1_base][name1]
            name2_a, name2_o = set_groups[name2_base][name2]

            if name1_base == name2_base:
                if name1 in set_groups:
                    r1 = Fraction(1, name2_a)
                    r2 = ((name2_o * -1) * Fraction(1, name2_a))
                    ans = r1 * x + r2
                elif name2 in set_groups:
                    ans = name1_a * x + name1_o
                else:
                    r1 = Fraction(1, name2_a)
                    r2 = ((name2_o * -1) * Fraction(1, name2_a))
                    ans = r1 * (name1_a * x + name1_o) + r2
        if ans is not None:
            print(float(ans))
        else:
            print('Too hard!')
    else:
        exit(0)
