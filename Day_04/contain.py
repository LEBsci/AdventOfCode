with open("input.txt", "r") as f:
    lines = [line for line in f.read().split('\n') if line != '']
    
count = 0
count2 = 0

for line in lines:
    elf1, elf2 = line.split(",") # Split the data separating by comma
    min_elf1, max_elf1 = [int(i) for i in elf1.split("-")] # Split values and convert to integer
    min_elf2, max_elf2 = [int(i) for i in elf2.split("-")]
    if (min_elf1 <= min_elf2 and max_elf2 <= max_elf1) or (min_elf2 <= min_elf1 and max_elf1 <= max_elf2): # Check if the ranges are contained within each other and increasing the count if that is the case
        count += 1
    if (min_elf1 <= min_elf2 <= max_elf1) or (min_elf2 <= min_elf1 <= max_elf2): # Range overlap checker for part 2 of the puzzle (cases duplicate so minimum is two)
        count2 += 1

print("The amount of assignments in which one range fully contains the other is: " + str(count)+"\n")
print("The amount of assignments in which ranges overlap is: " + str(count2))