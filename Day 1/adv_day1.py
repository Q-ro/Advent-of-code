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

# Main app


def main():
    # total sum of required fuel
    totalFuelSum = 0

    # open and read file
    for x in fileReader("input.txt"):
        # turn the lines into integers and calculate the required fuel for each module, then add it to the sum
        fuelMass = fuelCalculator(int(x))
        totalFuelSum += fuelMass

        print("Component Mass:")
        print(x)
        print("Required Fuel:")
        print(fuelMass)

        print("Fuel required so far Fuel:")
        print(totalFuelSum)

    print("Total Required Fuel is : %d" % (totalFuelSum))


# Start the main program
if __name__ == "__main__":
    main()
