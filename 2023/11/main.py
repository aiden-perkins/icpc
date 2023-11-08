import sys
import math

"""
player_count = 0
excitement_scores = []
for line in sys.stdin:
    line = line.replace('\n', '')
    if player_count == 0:
        player_count = int(line)
    else:
        excitement_scores.append([int(a) for a in line.split(' ')])
"""
player_count = 4
excitement_scores = [
    [0, 15, 4, -2],
    [15, 0, 10, 1],
    [4, 10, 0, 8],
    [-2, 1, 8, 0],
]
players_to_rounds = {
    2: 1,
    4: 2,
    8: 3,
    16: 4,
    32: 5,
    64: 6,
}
rounds_in_tourney = players_to_rounds[player_count]
total_games_left = (player_count - 1) ** 2
possible_different_brackets = player_count - 1
p1_games_played = rounds_in_tourney * possible_different_brackets

p1_ex = 0
for i in range(possible_different_brackets, 0, -1):
    p1_ex += (player_count - i) * excitement_scores[0][i]
total_games_left -= p1_games_played
print(total_games_left)

# Player 2

