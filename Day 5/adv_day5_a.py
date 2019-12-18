'''
Author: Andres Mrad (Q-ro)
Date: Tuesday 17/December/2019 @ 19:33:20
Description:  Solution to Day 5 puzzle (Part 1)
'''

# Imports
import random

# Reads the file and returns it contents
def fileReader(path):
    with open(path, "r") as filehandle:
        filecontent = filehandle.read()
    return filecontent

# Takes a list and runs the program as the instructions come in
def tapeReader(tape):
    currentPosition = 0
    currentOperation = []

    while True:
        currentOperation = tape[currentPosition]
        currentInstruction = tape[currentPosition: currentPosition+4]

        # Kill the program
        if (currentOperation == 99):
            break

        # Add
        if(currentOperation == 1):
            tape[currentInstruction[3]] = tape[currentInstruction[1]] + \
                tape[currentInstruction[2]]
            pass

        # Multiply
        if (currentOperation == 2):
            tape[currentInstruction[3]] = tape[currentInstruction[1]] * \
                tape[currentInstruction[2]]
            pass

        # Store value at a given position
        if (currentOperation == 3):
            
            pass

        # Outputs value at a given position
        if (currentOperation == 4):
            
            pass

        # Move to the next operation
        currentPosition += 4

    return tape


# custom Map implementation
def customMap(func, arr):
    tempArray = []
    for x in arr:
        tempArray.append(func(x))
        pass
    return tempArray


# Main App
def main():

    while True:

        # read the input file, remove special characters and store them into a a list
        programTape = customMap(int,  fileReader(
            r"Day 2\input.txt").rstrip().split(","))

        # replace the given positions of the tape with the given numbers
        noun  = random.randint(0, 99)
        verb  = random.randint(0, 99)
        programTape[1] = noun
        programTape[2] = verb

        endTape = tapeReader(programTape)
        # print("Verb :")
        # print(verb)
        # print("Noun :")
        # print(noun)
        # print("EndTape :")
        # print(endTape[0])

        if endTape[0] == 19690720:
            break

    print("End tape :")
    print(endTape)
    print("Verb :")
    print(verb)
    print("Noun :")
    print(noun)
    print("Solution :")
    print(100 * noun + verb)


# Start the main program
if __name__ == "__main__":
    main()
