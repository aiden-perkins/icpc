import heapq
import math
from itertools import combinations


def get_point_at_distance(p1, p2):
    vector_x = p2[0] - p1[0]
    vector_y = p2[1] - p1[1]
    distance = (vector_x**2 + vector_y**2)**0.5
    if distance == 0:
        return p1
    unit_x = vector_x / distance
    unit_y = vector_y / distance
    result_x = p2[0] - unit_x
    result_y = p2[1] - unit_y
    return result_x, result_y


def check_overlap(h, nh):
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    for point in h:
        distt = distance(point, nh)
        if distt > 2:
            return False

    epsilon = 1e-10
    for point in h:
        if distance(point, nh) < epsilon:
            return True
    return True


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def get_new_holds(holds_with_hand, holds_already_used, all_holds):
    untouched_holds = set(all_holds).difference(holds_already_used)
    new_holds = []
    for untouched_hold in untouched_holds:
        if check_overlap(holds_with_hand, untouched_hold):
            new_holds.append(untouched_hold)
    return new_holds


N = int(input())
start_holds = [(-0.2, 0), (0, 0), (0.2, 0)]
holds = []
for _ in range(N):
    holds.append(tuple(map(float, input().strip().split())))
th = holds[-1]
holds += start_holds

queue = [(0, (0, 0), set(start_holds), set(start_holds))]
final_cost = []
while queue:
    cost, current_position, current_holds, holds_used = heapq.heappop(queue)

    if th in holds_used:
        final_cost.append(cost)
        # break

    for new_current_holds in combinations(current_holds, 3):
        pnhs = get_new_holds(new_current_holds, holds_used, holds)
        for pnh in combinations(pnhs + list(new_current_holds), 3):
            print(pnh)
        # for possible_new_hold in get_new_holds(new_current_holds, holds_used, holds):
        #     pnc = dist(possible_new_hold, current_position)
        #     new_cost = cost
        #     new_pos = current_position
        #     if pnc > 1:
        #         new_cost += pnc - 1
        #         new_pos = get_point_at_distance(current_position, possible_new_hold)
        #     print(new_pos, new_cost)
        #     heapq.heappush(queue, (new_cost, new_pos, set(pnh), holds_used.union(set(pnh))))

if final_cost:
    print(min(final_cost))
else:
    print(-1)
