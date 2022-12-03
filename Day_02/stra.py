'''Strategy guide for the game Rock, Paper, Scissors'''

import pandas as pd

# Scoring function
def score(df):
    '''Score the game'''
    rounds = pd.DataFrame(columns=['Result'])

    for i in range(len(df)):
    # Draw rounds rules
       if df.iloc[i,0] == df.iloc[i,1]:
           if df.iloc[i,1] == 'A':
               rounds.loc[i] = 1 + 3
           elif df.iloc[i,1] == 'B':
               rounds.loc[i] = 2 + 3
           elif df.iloc[i,1] == 'C':
               rounds.loc[i] = 3 + 3
       # Winning rounds rules
       elif df.iloc[i,0] == 'A' and df.iloc[i,1] == 'B':
           rounds.loc[i] = 2 + 6
       elif df.iloc[i,0] == 'B' and df.iloc[i,1] == 'C':
           rounds.loc[i] = 3 + 6
       elif df.iloc[i,0] == 'C' and df.iloc[i,1] == 'A':
           rounds.loc[i] = 1 + 6
       # Losing rounds rules
       elif df.iloc[i,0] == 'A' and df.iloc[i,1] == 'C':
           rounds.loc[i] = 3
       elif df.iloc[i,0] == 'B' and df.iloc[i,1] == 'A':
           rounds.loc[i] = 1
       elif df.iloc[i,0] == 'C' and df.iloc[i,1] == 'B':
           rounds.loc[i] = 2
    return int(rounds.sum())

# Read the data
data = pd.read_csv('input.txt', sep=' ', header=None)
# Replace the values to match the opponent's notation
data.iloc[:,1] = data.iloc[:,1].str.replace('X', 'A').str.replace('Y', 'B').str.replace('Z', 'C')

# Score the data and write the output 

print('The total score would be ' + str(score(data)))

'''Part 2 of the puzzle'''
# Read the data again
data2 = pd.read_csv('input.txt', sep=' ', header=None)
# Replace the values to match the strategy guide and the opponent's notation
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

# Score the data and write the output 

print('The total score with strategy 2 would be ' + str(score(data2)))