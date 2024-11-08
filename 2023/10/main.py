from fractions import Fraction
import sys

parcel_count = 0
bookings = {}
for i in range(1, 37):
    bookings[i] = []
for line in sys.stdin:
    info = line.replace('  ', ' ').split(' SECTION ')
    s_n = int(info[1])
    parts = info[0].split(' OF ')
    nests = 1024
    const = 640 / (nests ** 2)
    s = [0, 0, nests, nests]
    parts.reverse()
    for part in parts:
        delta_x = (s[2] - s[0]) // 2
        delta_y = (s[3] - s[1]) // 2
        if 'N' in part:
            s[1] += delta_y
        elif 'S' in part:
            s[3] -= delta_y
        if 'E' in part:
            s[0] += delta_x
        elif 'W' in part:
            s[2] -= delta_x
    for book in bookings[s_n]:
        s_x_r = range(s[0], s[2] + 1)
        book_x_r = range(book[0], book[2] + 1)
        s_y_r = range(s[1], s[3] + 1)
        book_y_r = range(book[1], book[3] + 1)
        if len(list(set(s_x_r) & set(book_x_r))) > 1 and len(list(set(s_y_r) & set(book_y_r))) > 1:
            print(f'OVERLAPS {book[4]}')
            break
    else:
        acres = (s[2] - s[0]) * (s[3] - s[1]) * const
        fraction_s = ''
        if acres / int(acres) != 1:
            fraction_s = ' ' + str(Fraction(acres % int(acres)))
        word = 'ACRES'
        if acres <= 1:
            word = 'ACRE'
        parcel_count += 1
        print(f'{parcel_count} {int(acres)}{fraction_s} {word}')
        s.append(parcel_count)
        bookings[s_n].append(s)

