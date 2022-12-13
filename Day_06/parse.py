with open("input.txt", "r") as f:
    stream = f.read() # Read the input file
    
for i in range(len(stream)-3): # Iterate over every character in packs of four
    if len(set(stream[i:i+4])) == 4: # Check for a set in which there are four different symbols
        print('A total of ' + str(i+4) + ' characters need to be processed before the first start-of-packet marker is detected')
        break # Stop checking after the first packet appears