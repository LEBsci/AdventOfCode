with open("input.txt", "r") as f:
    lines = [line for line in f.read().split('\n') if line != '']
operations = [line for line in lines if 'move' in line]
f_stack = [line for line in lines if 'move' not in line]
for i in f_stack[-2].split(' '):
    print(i)