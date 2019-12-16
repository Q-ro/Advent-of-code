"""
Author: Andres Mrad (Q-ro)
Date: Wednesday 04/December/2019 @ 11:02:44
Description: Solution to day 3's puzzle (Part B)
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
                print('Incorrect Command %s, only U, D, R, L, are valid',
                      position[0])
                break

    return wirePointPlot


def stepCounter(wire1Plot, wire2Plot, intersection):

    shortestStepCount = 0
    # remove the starting point from the intersections list
    intersection.remove((0, 0))

    for i, position in enumerate(intersection):

        # find the index for the intersection point on wire 1
        indexW1 = wire1Plot.index(position)
        # find the index for the intersection point on wire 2
        indexW2 = wire2Plot.index(position)
        # calculate the step counts
        stepCount = len(set(wire1Plot[0:indexW1])) + \
            len(set(wire2Plot[0:indexW2]))
        # store the shortest one
        if i == 0 or shortestStepCount > stepCount:
            shortestStepCount = stepCount
        pass

    return shortestStepCount

# Main App


def main():
    paths = fileReader()
    wire1Plot = xyWirePointPlotter(paths[0])
    wire2Plot = xyWirePointPlotter(paths[1])
    intersection = list(set(wire1Plot).intersection(set(wire2Plot)))

    print("Shortest step count is : ")
    print(stepCounter(wire1Plot, wire2Plot, intersection))
    pass


# Entry point for the program
if __name__ == "__main__":
    main()
    pass
