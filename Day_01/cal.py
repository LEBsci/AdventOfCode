'''Calorie counting for elves'''

import pandas as pd

f = open('input.txt', 'r+') # open the input file for reading and writing
lines = [int('0'+line) for line in f.read().splitlines()] # read the lines and convert to integers, add a zero to the beginning of each line to avoid errors from newline characters
f.close() # close the file

data = pd.DataFrame(lines) # create a dataframe from the list of integers
indexes = data.loc[data.iloc[:,0] == 0].index.insert(0,0) # find the indexes of the 0s and insert a 0 at the beginning

indexes = indexes.insert(len(indexes),len(data)) # add the last index of data to the list of indexes

result = pd.DataFrame(columns=['calories']) # create a new dataframe to hold the results

for i in range(len(indexes)-1): # iterate through the indexes
    result.loc[i] = data.iloc[indexes[i]:indexes[i+1],0].sum() # sum the values between the indexes and add them to the result dataframe

print('The Elf carrying the most calories has: ' + str(int(result.max())) + ' calories\n') # print the maximum value in the result dataframe

# Part 2 of the puzzle


print('The top three elves are carrying a total of: '+ str(int(result.sort_values(by=['calories'], ascending=False).iloc[0:3].sum())) + ' calories') # print the sum of the top three values in the result dataframe

'''elliotwutingfeng solutions'''

# Open the file, read the lines and split them by newline characters
with open("input.txt", "r") as f:
    lines = f.read().split("\n")


x = 0
largest = 0
for d in lines:
    if d == "": # check each line for a separator or empty line and check if the current sum is larger than the largest sum
        largest = max(x, largest)
        x = 0
    else: # sum the value of each line when there is no separator
        x += int(d)
print(largest)

# Part 2 of the puzzle

with open("input.txt", "r") as f:
    lines = f.read().split("\n")

numbers = [] # create a list to hold the numbers
x = 0
for d in lines:
    if d == "": # check each line for a separator or empty line and save the sum to the list
        numbers.append(x)
        x = 0
    else: # sum the value of each line when there is no separator
        x += int(d) 
top_3 = sum(sorted(numbers)[-3:]) # sort the list and sum the top 3 values
print(top_3)