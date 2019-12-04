"""
Author: Andres Mrad (Q-ro)
Date: Wednesday 04/December/2019 @ 11:02:44
Description: Solution to day 3's puzzle 
"""

#Imports

# Reads the file and returns the wire paths
def fileReader(path):
    f = open(path, "r")
    return f.readlines()

# Main App
def main():
    wiresPaths = fileReader("Day 3\input.txt")
    wire1Path = wiresPaths[0].rstrip().split(",")
    wire2Path = wiresPaths[1].rstrip().split(",")
    # print(wiresPaths)
    print(wire1Path)
    print(wire2Path)
    pass

#Entry point for the program
if __name__ == "__main__":
    main()
    pass