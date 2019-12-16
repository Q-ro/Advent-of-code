"""
Author: Andres Mrad (Q-ro)
Date: Wednesday 04/December/2019 @ 11:02:44
Description: Solution to day 3's puzzle (Part A)
"""

# Reads the file and returns the wire paths
def fileReader():
    with open(r'Day 3\input.txt', 'r') as f:
        paths = [line.strip().split(',') for line in f]
    return paths

# Fills in the points in between the diferent end points of the wire
def xyWirePointPlotter(wirePositions):
    wirePointPlot = []
    xy = [0, 0]  # used to create the sequence between each collection of points
    for position in wirePositions:
        for _ in range(int(position[1:])):
            wirePointPlot.append(tuple(xy[:]))
            if position[0] == 'U':
                xy[1] += 1
            elif position[0] == 'D':
                xy[1] -= 1
            elif position[0] == 'L':
                xy[0] -= 1
            elif position[0] == 'R':
                xy[0] += 1
            else:
                print('Incorrect Command %s, only U, D, R, L, are valid', position[0])
                break

    return wirePointPlot

# Main App
def main():
    paths = fileReader()
    wire1Plot = xyWirePointPlotter(paths[0])
    wire2Plot = xyWirePointPlotter(paths[1])
    interceptions = list(set(wire1Plot).intersection(set(wire2Plot)))
    print(interceptions)
    absInterceptionPoints = [(abs(i[0]), abs(i[1])) for i in interceptions]
    print(absInterceptionPoints)

    # print the value for the smallest distance between the starting point and the interception point
    print(min([sum(i) for i in absInterceptionPoints if sum(i) > 0]))
    pass


# Entry point for the program
if __name__ == "__main__":
    main()
    pass
