with open("input.txt", "r") as f:
    lines = [line for line in f.read().split('\n') if line != '']

hand = {'X': 1, 'Y': 2, 'Z': 3}
win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
tie = {'X': 'A', 'Y': 'B', 'Z': 'C'}

score = 0
for line in lines:
    opp, me = line.split(" ")
    score += hand[me]
    if tie[me] == opp:
        score += 3
    if win[me] == opp:
        score += 6

print('The total score would be ' + str(score))
