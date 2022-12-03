with open("input.txt", "r") as f:
    lines = [line for line in f.read().split('\n') if line != '']

hand = {'X': 1, 'Y': 2, 'Z': 3}
win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
tie = {'X': 'A', 'Y': 'B', 'Z': 'C'}

# Checks for what the opponent played and compares. If it's the winning or tieing move it increases the score accordingly

score = 0
for line in lines:
    opp, me = line.split(" ")
    score += hand[me]
    if tie[me] == opp:
        score += 3
    if win[me] == opp:
        score += 6

print('The total score would be ' + str(score))

'''Part two of the problem'''

with open("input.txt", "r") as f:
    lines = [line for line in f.read().split('\n') if line != '']

# If the opponent plays the first one, I played the second and score accordingly

tie = {'A': 1, 'B': 2, 'C': 3}
lose = {'A': 3, 'B': 1, 'C': 2}
win = {'A': 2, 'B': 3, 'C': 1}

score = 0
for line in lines:
    opp, goal = line.split(" ")
    # Lose goal
    if goal == 'X':
        hand_score = lose
    # Tie goal
    if goal == 'Y':
        hand_score = tie
        score += 3
    # Win goal
    if goal == 'Z':
        hand_score = win
        score += 6
    score += hand_score[opp]

print('The total score with the second strategy would be ' + str(score))