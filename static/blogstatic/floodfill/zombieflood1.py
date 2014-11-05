import pygame, time, sys
from pygame.locals import *


WORLD = """
hhhhhhh
hhchhhh
hchhchh
hchhchh
hhcchhh
hhhhhhz
"""
WORLD_WIDTH = len(WORLD.strip().split('\n')[0])
WORLD_HEIGHT = len(WORLD.strip().split('\n'))
assert ['bad width' for x in WORLD.strip().split('\n') if len(x) != WORLD_WIDTH] == [], "WORLD string needs to be rectangular."

# pygame setup stuff
pygame.init()
winWidth = 50 * WORLD_WIDTH
winHeight = 50 * WORLD_HEIGHT
windowSurface = pygame.display.set_mode((winWidth, winHeight), 0, 32)
pygame.display.set_caption('Zombie Flood 1')

# define a bunch of constants
WHITE = (255, 255, 255)

WINDOW_BG = WHITE
HUMAN_IMG = pygame.image.load('human_transparent.png')
ZOMBIE_IMG = pygame.image.load('zombie_transparent.png')
CAT_IMG = pygame.image.load('cat_transparent.png')

DELAY = 0.3 # seconds between showing the next level
SAVEIMAGES = False # if True, save the images that this program produces (this creates a ton of .png files in the script's directory)
if SAVEIMAGES:
    DELAY = 0.0


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
    return world

def drawWorld(surf, world):
    width = len(world)
    height = len(world[0])
    for x in range(width):
        for y in range(height):
            surf.blit(world[x][y], (x * 50, y * 50, 50, 50))


def zombieBite(world, x, y):
    worldWidth = len(world)
    worldHeight = len(world[0])
    atLeastOneBite = False
    for ix, iy in ( (1,0), (-1,0), (0,1), (0,-1) ):
        if x+ix >= 0 and y+iy >= 0 and x+ix < worldWidth and y+iy < worldHeight and world[x+ix][y+iy] == HUMAN_IMG:
            world[x+ix][y+iy] = ZOMBIE_IMG
            atLeastOneBite = True
    return atLeastOneBite

def main():
    saveTimestamp = int(time.time())
    saveCounter = 0
    world = convertAsciiMapToWorld(WORLD)
    worldWidth = len(world)
    worldHeight = len(world[0])

    windowSurface.fill(WHITE)
    drawWorld(windowSurface, world)
    if SAVEIMAGES:
        pygame.image.save(windowSurface, 'zflood1_%s_%s.png' % (saveTimestamp, str(saveCounter).rjust(4, '0')))
        saveCounter += 1

    startTime = time.time()

    # run the game loop
    while True:
        if time.time() > startTime + DELAY:
            atLeastOneBite = False
            originalZombies = []
            for x in range(worldWidth):
                for y in range(worldHeight):
                    if world[x][y] == ZOMBIE_IMG:
                        originalZombies.append((x, y))

            for x, y in originalZombies:
                if zombieBite(world, x, y):
                    atLeastOneBite = True

            if atLeastOneBite:
                # redraw the world since there has been a change
                windowSurface.fill(WHITE)
                drawWorld(windowSurface, world)
                if SAVEIMAGES:
                    pygame.image.save(windowSurface, 'zflood1_%s_%s.png' % (saveTimestamp, str(saveCounter).rjust(4, '0')))
                    saveCounter += 1

            startTime = time.time()

        # check for any quit events
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main()