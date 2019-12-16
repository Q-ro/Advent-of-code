'''
Author: Andres Mrad (Q-ro)
Date: Sunday 01/December/2019 @ 21:11:40
Description: Solution to "Advent of code" Day 1 puzzle (https://adventofcode.com/2019/day/1)
'''

# imports
import array
import math

# reads a file and returns it as an array of the file lines


def fileReader(path):
    f = open(path, "r")
    return f.readlines()

# return the amount of fuel needed for a given mass and it's fuel


def fuelCalculator(mass):
    fuel = (math.floor(mass/3) - 2)
    if(fuel <= 0):
        return 0
    else:
        return fuelCalculator(fuel) + fuel

# custom sumBy implementation


def sumBy(func, arr):
    tempSum = 0
    for x in arr:
        tempSum += func(x)
        pass
    return tempSum

# custom Map implementation


def customMap(func, arr):
    tempArray = []
    for x in arr:
        tempArray.append(func(x))
        pass
    return tempArray

# Main app


def main():
    # total sum of required fuel (for moduels 'n fuel)
    print("Total Required Fuel is : %d" %
          (sumBy(fuelCalculator,  customMap(int, fileReader(r"Day 1\input.txt")))))


# Start the main program
if __name__ == "__main__":
    main()
