import numpy as np

with open("input.txt", "r") as f:
    lines = [line for line in f.read().split('\n') if line != ''] # Read the input file and remove empty lines

operations = [line for line in lines if 'move' in line] # List of operations, they contain the word 'move'

f_stack = [line for line in lines if 'move' not in line] # List of stacks

s_stack = np.array([[f_stack[i][1+4*j] for j in range(len(f_stack[i])//4+1)] for i in range(len(f_stack))]).T # Stacks as a 2D array for transposing

grid = [''.join(s_stack[i]).replace(' ', '') for i in range(len(s_stack))] # For Part One

grid2 = [''.join(s_stack[i]).replace(' ', '') for i in range(len(s_stack))] # For Part Two

for i in operations: # For each operation
    sep = ''.join(x for x in i if x.isdigit()) # Find the numbers in the operation
    crates, from_, to_ = int(sep[:-2]), int(sep[-2])-1, int(sep[-1])-1 # Split the numbers into how many crates, from_ what stack and to_ what stack
    '''Section for part Two'''
    grid2[to_] = grid2[from_][0:int(crates)] + grid2[to_]
    grid2[from_] = grid2[from_][int(crates):]
    '''End of section for part Two'''
    for j in range(crates): # For each crate
        grid[to_] = grid[from_][0] + grid[to_] # Move the crate to the top of the stack
        grid[from_] = grid[from_][1:] # Remove the crate from the stack

print('The crates that end up on top of each stack are: '+''.join([grid[i][0] for i in range(len(grid))]) + '\n')

'''Part Two'''

print('The crates that end up on top of each stack with the CrateMover 9001 are : '+''.join([grid2[i][0] for i in range(len(grid))]) + '\n')