#10.	Create a list of lists to represent the scores of different games played in a tournament, 
# and find the winner based on the highest average score
# Create a list of lists where each sublist contains scores of a player in different games
scores = [
    [150, 200, 250],  # Player 1 scores
    [300, 400, 350],  # Player 2 scores
    [200, 250, 300],  # Player 3 scores
    [400, 450, 500]   # Player 4 scores
]

# Manually calculate the average score for each player
# Player 1 average
player_1_total = scores[0][0] + scores[0][1] + scores[0][2]
player_1_avg = player_1_total / 3

# Player 2 average
player_2_total = scores[1][0] + scores[1][1] + scores[1][2]
player_2_avg = player_2_total / 3

# Player 3 average
player_3_total = scores[2][0] + scores[2][1] + scores[2][2]
player_3_avg = player_3_total / 3

# Player 4 average
player_4_total = scores[3][0] + scores[3][1] + scores[3][2]
player_4_avg = player_4_total / 3

# Manually find the highest average score and the corresponding player
# Assume Player 1 is the initial winner
winner_index = 0
highest_avg = player_1_avg

# Compare Player 2
if player_2_avg > highest_avg:
    winner_index = 1
    highest_avg = player_2_avg

# Compare Player 3
if player_3_avg > highest_avg:
    winner_index = 2
    highest_avg = player_3_avg

# Compare Player 4
if player_4_avg > highest_avg:
    winner_index = 3
    highest_avg = player_4_avg

# Print the winner and their average score
print("Winner: Player", winner_index + 1)
print("Highest Average Score:", highest_avg)
