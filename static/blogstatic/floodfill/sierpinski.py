"""
A Simple Demonstration of Recursive Functions with Sierpinkski Triangles
By Al Sweigart
http://inventwithpython.com

This script requires Pygame to be installed along with Python.
    http://pygame.com/download.shtml

You can modify this program by setting different values for some of the variables:
    WINWIDTH
    WINHEIGHT
    WINDOW_BG
    TRIANGLE_FG
    TRIANGLE_BG
    DELAY
    DEBUG
    MAXLEVEL

If you set DEBUG to True, then you will see red rectangles drawn around each of the sub-triangles that are drawn.
"""
import pygame, time, sys
from pygame.locals import *

# pygame setup stuff
pygame.init()
WINWIDTH = 640
WINHEIGHT = 480
windowSurface = pygame.display.set_mode((WINWIDTH, WINHEIGHT), 0, 32)
pygame.display.set_caption('Sierpinski Triangles')


# define a bunch of constants:
DELAY = 1.5 # seconds between showing the next level
DEBUG = False # if True, show red rectangle outlines
MAXLEVEL = 8 # the largest number of levels for the animation to show

# The red, green, blue values can be anywhere from 0 to 255:
#                 R    G    B
RED           = (255,   0,   0)
WHITE         = (255, 255, 255)
DARKTURQUOISE = (  3,  54,  73)
TURQUOISE     = (103, 154, 173)
GREEN         = (  0, 204,   0)

WINDOW_BG = TURQUOISE
TRIANGLE_FG = GREEN
TRIANGLE_BG = DARKTURQUOISE

SAVEIMAGES = False
if SAVEIMAGES:
    DELAY = 0.0


def drawSierpinkski(surf, rect, fgcolor, bgcolor, level=6):
    # Draws sierpinkski triangles inside the given rect object on the surf surface.

    if level == 0: # base case
        return

    # calculate the point one quarter and three quarters in the rect
    quarterWidth = (rect.width / 4) + rect.left
    threeQuarterWidth = (rect.width / 4 * 3) + rect.left

    # draw the outer triangle:
    pygame.draw.polygon(surf, fgcolor, ((rect.centerx, rect.top), (rect.left, rect.bottom), (rect.right, rect.bottom)))
    # draw the upside down inner triangle:
    pygame.draw.polygon(surf, bgcolor, ((quarterWidth, rect.centery), (rect.centerx, rect.bottom), (threeQuarterWidth, rect.centery)))

    # calculate the rectangular outlines
    topRect   = pygame.Rect(quarterWidth, rect.top,     (rect.width / 2), (rect.height / 2))
    leftRect  = pygame.Rect(rect.left,    rect.centery, (rect.width / 2), (rect.height / 2))
    rightRect = pygame.Rect(rect.centerx, rect.centery, (rect.width / 2), (rect.height / 2))

    if DEBUG:
        # in debug mode, we draw red outlines around each of the smaller inner triangles
        pygame.draw.rect(surf, RED, topRect, 1)
        pygame.draw.rect(surf, RED, leftRect, 1)
        pygame.draw.rect(surf, RED, rightRect, 1)

    # do the recursive calls, note that we pass "level-1" for the level.
    # (eventually level will become 0, and we'll stop making recursive calls)
    drawSierpinkski(surf, topRect, fgcolor, bgcolor, level-1)
    drawSierpinkski(surf, leftRect, fgcolor, bgcolor, level-1)
    drawSierpinkski(surf, rightRect, fgcolor, bgcolor, level-1)


def main():
    global SAVEIMAGES
    levelCounter = 0
    startTime = time.time() - DELAY
    saveCounter = 0
    saveTimestamp = int(time.time())

    # run the game loop
    while True:
        if time.time() > startTime + DELAY:
            # after DELAY seconds have passed, increment the level and draw it
            levelCounter += 1
            if levelCounter >= MAXLEVEL:
                # once we reach level 8, reset it back to 1.
                levelCounter = 1
                SAVEIMAGES = False

            # start with a fresh background:
            windowSurface.fill(WINDOW_BG)
            # draw the sierpinkski triangles
            drawSierpinkski(windowSurface, pygame.Rect(0, 0, WINWIDTH, WINHEIGHT), TRIANGLE_FG, TRIANGLE_BG, levelCounter)

            if SAVEIMAGES:
                pygame.image.save(windowSurface, 'sierpinkski_%s_%s.png' % (saveTimestamp, str(saveCounter).rjust(4, '0')))
                saveCounter += 1

            startTime = time.time() # reset the timer
        pygame.display.update()

        # check for any quit events
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()