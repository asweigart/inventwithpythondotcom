"""
Room Counter program
by Al Sweigart
http://inventwithpython.com

This program demonstrates how the flood fill algorithm can be used to determine
how many enclosed rooms are in a map.

Draw the map in the textworld multiline string (make sure the first and last lines
are blank) using . for empty spaces and # for walls. The program will display
the map you've configured and then also shows how many enclosed rooms there are.
(Walls that do not completely close off rooms are not counted.)

This program is made for Python 3, but works in Python 2 as well.

"""

import sys

# This map contains four rooms.
textmap = """
........................#.....
........................#.....
........................#.....
.....######.............######
.....#....#....######.........
.....#....#....#....#.....#...
.....######....##.###.....#...
................#.#.......####
................#.#...........
######.....######.#######.....
#....#.....#............#.....
###..#.....#............#.....
###..#.....##############.....
#....#........................
######........................
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
    # The recursive algorithm. Starting at x and y, changes any adjacent
    # characters that match oldChar to newChar.
    worldWidth = len(world)
    worldHeight = len(world[0])

    if oldChar == None:
        oldChar = world[x][y]

    if world[x][y] != oldChar:
        # Base case. If the current x, y character is not the oldChar,
        # then do nothing.
        return

    # Change the character at world[x][y] to newChar
    world[x][y] = newChar

    # Recursive calls. Make a recursive call as long as we are not on the
    # boundary (which would cause an Index Error.)
    if x > 0: # left
        floodFill(world, x-1, y, oldChar, newChar)

    if y > 0: # up
        floodFill(world, x, y-1, oldChar, newChar)

    if x < worldWidth-1: # right
        floodFill(world, x+1, y, oldChar, newChar)

    if y < worldHeight-1: # down
        floodFill(world, x, y+1, oldChar, newChar)


def getNumOfRooms(world):
    worldWidth = len(world)
    worldHeight = len(world[0])

    roomCount = -1 # because the outside area counts as room, so let's start
                   # off at -1.
    for x in range(worldWidth):
        for y in range(worldHeight):
            # on each possible x, y empty space in the map, call floodfill.
            if world[x][y] == '.':
                floodFill(world, x, y, '.', 'x')

                # comment out the next two lines if you don't want
                # getNumOfRooms() to display output when called.
                printWorld(world)
                print()

                roomCount += 1
    return roomCount


world = getWorldFromTextMap(textmap)
printWorld(world)
print()
print('Number of rooms:', getNumOfRooms(world))
