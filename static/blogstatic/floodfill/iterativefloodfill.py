"""
A really simple --iterative-- implementation of the Flood Fill algorithm.
by Al Sweigart
http://inventwithpython.com

This script can be run with either Python 2 or Python 3.
"""

import sys

textmap = """
....................
.......XXXXXXXXXX...
.......X........X...
.......X........X...
..XXXXXX........X...
..X.............X...
..X.............X...
..X........XXXXXX...
..X........X........
..XXXX..XXXX........
.....XXXX...........
....................
....................
"""

lines = textmap.strip().split('\n')
assert ['bad width' for x in lines if len(x) != len(lines[0])] == [], "WORLD string needs to be rectangular."

def getWorldFromTextMap(textmap):
    # Converts the programmer-friendly version of a world typed out as ascii
    # characters in a multiline string into a source code-friendly version
    # that lets us access the map as world[x][y].
    worldWidth = len(textmap.strip().split('\n')[0])
    worldHeight = len(textmap.strip().split('\n'))

    textmap = textmap.strip().split('\n')

    world = []
    for i in range(worldWidth):
        world.append([''] * worldHeight)
    for x in range(worldWidth):
        for y in range(worldHeight):
            world[x][y] = textmap[y][x]
    return world


def printWorld(world):
    worldWidth = len(world)
    worldHeight = len(world[0])

    for y in range(worldHeight):
        for x in range(worldWidth):
            sys.stdout.write(world[x][y])
        sys.stdout.write('\n')

def floodFill(world, x, y, oldChar, newChar):
    # Starting at x and y, changes any adjacent
    # characters that match oldChar to newChar.
    worldWidth = len(world)
    worldHeight = len(world[0])

    if oldChar == None:
        oldChar = world[x][y]

    theStack = [ (x, y) ]
    while len(theStack) > 0:
        x, y = theStack.pop()

        if world[x][y] != oldChar:
            # Base case. If the current x, y character is not the oldChar,
            # then do nothing.
            continue

        # Change the character at world[x][y] to newChar
        world[x][y] = newChar

        if x > 0: # left
            theStack.append( (x-1, y) )

        if y > 0: # up
            theStack.append( (x, y-1) )

        if x < worldWidth-1: # right
            theStack.append( (x+1, y) )

        if y < worldHeight-1: # down
            theStack.append( (x, y+1) )

def main():
    world = getWorldFromTextMap(textmap)
    printWorld(world)
    print()

    floodFill(world, 5, 8, None, '+')
    printWorld(world)
    print()

    floodFill(world, 0, 0, None, 's')
    printWorld(world)
    print()

if __name__ == '__main__':
    main()