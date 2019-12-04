"""
Author: Andres Mrad (Q-ro)
Date: Tuesday 03/December/2019 @ 15:02:41
Description:  Solution to day 2 puzzle
"""

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

        print("Current instruction %a" % currentInstruction)

        # Kill the program
        if (currentOperation == 99):
            break

        # if(currentPosition+4 < len(tape)):

        # if(currentInstruction[3] < len(tape)):

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

    noun = -1
    verb = 0

    while True:
        noun += 1

        # read the input file, remove special characters and store them into a a list
        programTape = customMap(int,  fileReader(
            "Day 2\input.txt").rstrip().split(","))

        # replace the given positions of the tape with the given numbers
        programTape[1] = noun
        programTape[2] = verb

        endTape = tapeReader(programTape)
        print("Verb :")
        print(verb)
        print("Noun :")
        print(noun)
        print("EndTape :")
        print(endTape[0])

        if endTape[0] == 19690720:
            break

        if noun == 99:
            verb += 1
            noun = 0
            pass

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
