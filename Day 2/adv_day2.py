"""
Author: Andres Mrad (Q-ro)
Date: Tuesday 03/December/2019 @ 15:02:41
Description:  Solution to day 2 puzzle 
"""

# Reads the file and returns it contents


def fileReader(path):
    with open(path, "r") as filehandle:
        filecontent = filehandle.read()
    return filecontent

# Takes a list and runs the program as the instructions come in


def tapeReader(tape):
    currentOperation = 0
    position1 = 0
    position2 = 0
    outputPosition = 0

    while currentOperation != 99:

        # Add
        if(currentOperation == 1):
            pass
        # Multiply
        if (currentOperation == 2):
            pass
        pass
    pass

# Main App


def main():
    # read the input file, remove special characters and store them into a a list
    programTape = fileReader(
        "d:/Gatos/Projects/Python/Advent of Code/Day 2/input.txt").rstrip().split(",")
    # replace the given positions of the tape qith the given numbers
    programTape[1] = 1
    programTape[2] = 12
    tapeReader(programTape)
    pass


# Start the main program
if __name__ == "__main__":
    main()
