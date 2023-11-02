import numpy as np
import sys
import time as tm

start_time = tm.time()
"""
for line in ['5 3 -3 3 -3 -5', '15 4 20']:  # 1.in
for line in ['10 0 0 5 -7 -7', '30 1 50']:  # 3.in
for line in ['10 0 0 5 -7 -7', '30 20 50']:  # 2.in
"""
first = False
for line in sys.stdin:
    if not first:
        x1, y1, x2, y2, x3, y3 = [int(a) for a in line.split(' ')]
        r1 = np.sqrt(x1 ** 2 + y1 ** 2)
        r2 = np.sqrt(x2 ** 2 + y2 ** 2)
        r3 = np.sqrt(x3 ** 2 + y3 ** 2)
        first = True
    else:
        v, t, earth_distance = [int(a) for a in line.split(' ')]

        def rotate(x, y, radius, new_angle):
            # This rotates the given coordinate by the given angle.
            if x < 0:
                new_angle += 180
            if x == 0:
                old_angle = (np.pi / 2) * (y / np.abs(y))
            else:
                old_angle = np.arctan((y / x))
            new_angle = ((new_angle * np.pi) / 180) + old_angle
            return [(radius * np.cos(new_angle)), radius * np.sin(new_angle), radius]

        p1 = [x1, y1, r1]
        p2 = [x2, y2, r2]
        p3 = [x3, y3, r3]

        # find the max radius
        max_radius = max(r1, r2, r3)
        # calculate the fastest time it reaches earth_distance
        units_to_move = earth_distance - max_radius
        fastest_time_to_earth_distance = units_to_move / v
        # use that time to find how much it has rotated
        degrees_to_move = ((fastest_time_to_earth_distance / t) * 360) % 360
        # calculate new 3 points from this spot
        p1 = rotate(*p1, degrees_to_move)
        p2 = rotate(*p2, degrees_to_move)
        p3 = rotate(*p3, degrees_to_move)
        # update w
        earth_distance = earth_distance - units_to_move
        # now run the accuracy code

        def check_distance(sign, distance, px1, px2, px3):
            if sign == -1:
                return px1 >= distance or px2 >= distance or px3 >= distance
            return px1 <= distance and px2 <= distance and px3 <= distance

        delta_degrees_time = 360 / t  # this is the amount of degrees it goes for every t
        current_time = 0
        last_sign = -1
        accuracy = 10  # Cannot be > 14
        for exponent in range(accuracy + 1):
            delta_time = 0.01 * (10 ** (-exponent)) * last_sign
            last_sign *= -1
            delta_angle = delta_degrees_time * delta_time
            delta_x = delta_time * v
            current_sign = delta_time / np.abs(delta_time)
            while check_distance(current_sign, earth_distance, p1[0], p2[0], p3[0]):
                p1 = rotate(*p1, delta_angle)
                p2 = rotate(*p2, delta_angle)
                p3 = rotate(*p3, delta_angle)
                earth_distance -= delta_x
                current_time += delta_time
        raw_time = current_time + fastest_time_to_earth_distance
        total_time = format(round(raw_time, accuracy), "." + str(accuracy) + "f")
        print(total_time)
        # print(f'Took {tm.time() - start_time} seconds')
