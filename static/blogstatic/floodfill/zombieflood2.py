import pygame, time, sys
from pygame.locals import *


WORLD = """
hhhhhhh
hhchhhh
hchhchh
hchhchh
hhcchhh
hhhhhhh
"""
WORLD_WIDTH = len(WORLD.strip().split('\n')[0])
WORLD_HEIGHT = len(WORLD.strip().split('\n'))
assert ['bad width' for x in WORLD.strip().split('\n') if len(x) != WORLD_WIDTH] == [], "WORLD string needs to be rectangular."

# pygame setup stuff
pygame.init()
winWidth = 50 * WORLD_WIDTH
winHeight = 50 * WORLD_HEIGHT
windowSurface = pygame.display.set_mode((winWidth, winHeight), 0, 32)
pygame.display.set_caption('Zombie Flood 2')

# define a bunch of constants
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

WINDOW_BG = WHITE
TOBITECOLOR = (0,255,0)
HUMAN_IMG = pygame.image.load('human_transparent.png')
ZOMBIE_IMG = pygame.image.load('zombie_transparent.png')
CAT_IMG = pygame.image.load('cat_transparent.png')

DELAY = 0.5 # seconds between showing the next level
SAVEIMAGES = False # if True, save the images that this program produces
if SAVEIMAGES:
    DELAY = 0.0

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

SAVETIMESTAMP = int(time.time())
SAVECOUNTER = 0


def convertAsciiMapToWorld(ascii_map):
    ascii_map = ascii_map.strip().split('\n')
    width = len(ascii_map[0])
    height = len(ascii_map)

    world = []
    for i in range(width):
        world.append([HUMAN_IMG] * height)

    for x in range(width):
        for y in range(height):
            if ascii_map[y][x] == 'c':
                world[x][y] = CAT_IMG
            elif ascii_map[y][x] == 'z':
                world[x][y] = ZOMBIE_IMG

    biteMap = []
    for x in range(width):
        column = []
        for y in range(height):
            column.append( [UP, DOWN, LEFT, RIGHT] )
        biteMap.append(column)

    return world, biteMap

def drawWorld(surf, world, biteMap):
    global SAVECOUNTER

    surf.fill(WHITE)

    width = len(world)
    height = len(world[0])
    for x in range(width):
        for y in range(height):
            surf.blit(world[x][y], (x * 50, y * 50, 50, 50))

    for x in range(width):
        for y in range(height):
            if world[x][y] == ZOMBIE_IMG:
                # draw bitemap for this coordinate
                if UP in biteMap[x][y]:
                    pygame.draw.circle(surf, TOBITECOLOR, (x*50+25, y*50+10), 5)
                if DOWN in biteMap[x][y]:
                    pygame.draw.circle(surf, TOBITECOLOR, (x*50+25, y*50+40), 5)
                if LEFT in biteMap[x][y]:
                    pygame.draw.circle(surf, TOBITECOLOR, (x*50+10, y*50+25), 5)
                if RIGHT in biteMap[x][y]:
                    pygame.draw.circle(surf, TOBITECOLOR, (x*50+40, y*50+25), 5)

    if SAVEIMAGES:
        pygame.image.save(surf, 'zflood2_%s_%s.png' % (SAVETIMESTAMP, str(SAVECOUNTER).rjust(4, '0')))
        SAVECOUNTER += 1

    pygame.display.update()
    time.sleep(DELAY)


def zombieFloodFill(surf, world, biteMap, x, y):

    worldWidth = len(world)
    worldHeight = len(world[0])

    world[x][y] = ZOMBIE_IMG
    drawWorld(surf, world, biteMap)


    biteMap[x][y].remove(UP)
    if y-1 >= 0 and world[x][y-1] == HUMAN_IMG:
        zombieFloodFill(surf, world, biteMap, x, y-1)
    drawWorld(surf, world, biteMap)

    biteMap[x][y].remove(RIGHT)
    if x+1 < worldWidth and world[x+1][y] == HUMAN_IMG:
        zombieFloodFill(surf, world, biteMap, x+1, y)
    drawWorld(surf, world, biteMap)

    biteMap[x][y].remove(DOWN)
    if y+1 < worldHeight and world[x][y+1] == HUMAN_IMG:
        zombieFloodFill(surf, world, biteMap, x, y+1)
    drawWorld(surf, world, biteMap)

    biteMap[x][y].remove(LEFT)
    if x-1 >= 0 and world[x-1][y] == HUMAN_IMG:
        zombieFloodFill(surf, world, biteMap, x-1, y)
    drawWorld(surf, world, biteMap)


def main():
    startx = 5
    starty = 5

    world, biteMap = convertAsciiMapToWorld(WORLD)
    worldWidth = len(world)
    worldHeight = len(world[0])

    zombieFloodFill(windowSurface, world, biteMap, startx, starty)

    while True:
        # check for any quit events
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main()