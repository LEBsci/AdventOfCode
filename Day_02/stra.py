'''Strategy guide for the game Rock, Paper, Scissors'''

import pandas as pd

# Read the data
data = pd.read_csv('input.txt', sep=' ', header=None)

data.iloc[:,1] = data.iloc[:,1].str.replace('X', 'A').str.replace('Y', 'B').str.replace('Z', 'C')

# Score the data

rounds = pd.DataFrame(columns=['Result'])

for i in range(len(data)):
    # Draw rounds rules
    if data.iloc[i,0] == data.iloc[i,1]:
        if data.iloc[i,1] == 'A':
            rounds.loc[i] = 1 + 3
        elif data.iloc[i,1] == 'B':
            rounds.loc[i] = 2 + 3
        elif data.iloc[i,1] == 'C':
            rounds.loc[i] = 3 + 3
    # Winning rounds rules
    elif data.iloc[i,0] == 'A' and data.iloc[i,1] == 'B':
        rounds.loc[i] = 2 + 6
    elif data.iloc[i,0] == 'B' and data.iloc[i,1] == 'C':
        rounds.loc[i] = 3 + 6
    elif data.iloc[i,0] == 'C' and data.iloc[i,1] == 'A':
        rounds.loc[i] = 1 + 6
    # Losing rounds rules
    elif data.iloc[i,0] == 'A' and data.iloc[i,1] == 'C':
        rounds.loc[i] = 3
    elif data.iloc[i,0] == 'B' and data.iloc[i,1] == 'A':
        rounds.loc[i] = 1
    elif data.iloc[i,0] == 'C' and data.iloc[i,1] == 'B':
        rounds.loc[i] = 2

# Write the output 
print('The total score would be ' + str(int(rounds.sum())))

'''Part 2 of the puzzle'''
# Read the data again
data2 = pd.read_csv('input.txt', sep=' ', header=None)

for i in range(len(data2)):
    # Draw rounds rules
    if data2.iloc[i,1] == 'Y':
        data2.iloc[i,1] = data2.iloc[i,0]
    # Lose rounds rules
    elif data2.iloc[i,1] == 'X':
        if data2.iloc[i,0] == 'A':
            data2.iloc[i,1] = 'C'
        elif data2.iloc[i,0] == 'B':
            data2.iloc[i,1] = 'A'
        elif data2.iloc[i,0] == 'C':
            data2.iloc[i,1] = 'B'
    # Win rounds rules
    elif data2.iloc[i,1] == 'Z':
        if data2.iloc[i,0] == 'A':
            data2.iloc[i,1] = 'B'
        elif data2.iloc[i,0] == 'B':
            data2.iloc[i,1] = 'C'
        elif data2.iloc[i,0] == 'C':
            data2.iloc[i,1] = 'A'

# Score the data

rounds2 = pd.DataFrame(columns=['Result'])

for i in range(len(data2)):
    # Draw rounds rules
    if data2.iloc[i,0] == data2.iloc[i,1]:
        if data2.iloc[i,1] == 'A':
            rounds2.loc[i] = 1 + 3
        elif data2.iloc[i,1] == 'B':
            rounds2.loc[i] = 2 + 3
        elif data2.iloc[i,1] == 'C':
            rounds2.loc[i] = 3 + 3
    # Winning rounds rules
    elif data2.iloc[i,0] == 'A' and data2.iloc[i,1] == 'B':
        rounds2.loc[i] = 2 + 6
    elif data2.iloc[i,0] == 'B' and data2.iloc[i,1] == 'C':
        rounds2.loc[i] = 3 + 6
    elif data2.iloc[i,0] == 'C' and data2.iloc[i,1] == 'A':
        rounds2.loc[i] = 1 + 6
    # Losing rounds rules
    elif data2.iloc[i,0] == 'A' and data2.iloc[i,1] == 'C':
        rounds2.loc[i] = 3
    elif data2.iloc[i,0] == 'B' and data2.iloc[i,1] == 'A':
        rounds2.loc[i] = 1
    elif data2.iloc[i,0] == 'C' and data2.iloc[i,1] == 'B':
        rounds2.loc[i] = 2

# Write the output 
print('The total score with strategy 2 would be ' + str(int(rounds2.sum())))        