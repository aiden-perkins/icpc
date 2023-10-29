import sys
import math

for line in sys.stdin:
    nums = [float(a) for a in line.split(' ')]
    lengths = [
        50 - (2.54 * 4),
        100 - (2.54 * 8),
        200 - (2.54 * 8),
        300 - (2.54 * 8),
        500 - (2.54 * 8)
    ]
    m = ['0.5', '1', '2', '3', '5']
    side_distance = 1.75 * abs(nums[0] - nums[2])
    right = (19 - nums[1]) + (19 - nums[3])
    left = nums[1] + nums[3]
    length_side = (side_distance + min(right, left)) * 2.54
    length_no_side = (math.sqrt((side_distance ** 2) + (abs(nums[1] - nums[3]) ** 2))) * 2.54
    if length_no_side < lengths[0]:
        print(m[0])
    else:
        for i, l in enumerate(lengths[1:]):
            if length_side < l:
                print(m[i + 1])
                break
