with open("input.txt", "r") as f:
    lines = [line for line in f.read().split('\n') if line != '']

upper = [*range(65,91)] # ASCII characters for letters A-Z
lower = [*range(97,123)] # ASCII characters for letters a-z
chars = lower + upper # All ASCII characters

d = {} # Empty dictionary
count = 1 # Priority of the first item
sum = 0 # Sum of all priorities

for i in chars:
    d[chr(i)] = count # Add the character and its priority to the dictionary
    count += 1

for line in lines:
    first, second = line[len(line)//2:], line[:len(line)//2] # Split the line in half
    output = [x for x in first if x in second]  # Find the characters that are in both halves
    sum += d[output[0]] # Add the priority of the first character (some appear several times) to the sum

print('The sum of priorities for the item types that appear in both rucksacks is: ' + str(sum) + '\n')


'''Part two of the puzzle'''

sum2 = 0 # Sum of all priorities

for i in range(len(lines)//3):
    first, second, third = lines[i*3:i*3+3] # Split the lines into groups of three
    output = [x for x in first if x in second and x in third] # Find the characters that are in all three lines
    sum2 += d[output[0]] # Add the priority of the first character (some appear several times) to the sum

print('The sum of priorities for the item types that correspond to the badges of three-Elf groups is: ' + str(sum2))