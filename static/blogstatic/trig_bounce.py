# Examples of the math.sin() and math.cos() trig functions
# Al Sweigart al@inventwithpython.com

# You can learn more about Pygame with the
# free book "Making Games with Python & Pygame"
#
# http://inventwithpython.com/pygame
#

import sys, pygame, math
from pygame.locals import *

# set up a bunch of constants
BRIGHTBLUE = (  0,  50, 255)
RED        = (255,   0,   0)
WHITE      = (255, 255, 255)
BLACK      = (  0,   0,   0)

BGCOLOR = WHITE

WINDOWWIDTH = 640 # width of the program's window, in pixels
WINDOWHEIGHT = 480 # height in pixels
WIN_CENTERX = int(WINDOWWIDTH / 2)
WIN_CENTERY = int(WINDOWHEIGHT / 2)

FPS = 60

PERIOD_INCREMENTS = 500.0
AMPLITUDE = 100

# standard pygame setup code
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Trig Bounce')

step = 0

# main application loop
while True:
    # event handling loop for quit events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    # fill the screen to draw from a blank state
    DISPLAYSURF.fill(BGCOLOR)

    # draw waving ball
    yPos = -1 * math.sin(step) * AMPLITUDE
    pygame.draw.circle(DISPLAYSURF, BRIGHTBLUE, (int(WINDOWWIDTH * 0.333), int(yPos) + WIN_CENTERY), 40)

    # draw waving ball
    yPos = -1 * abs(math.sin(step)) * AMPLITUDE
    pygame.draw.circle(DISPLAYSURF, RED, (int(WINDOWWIDTH * 0.666), int(yPos) + WIN_CENTERY), 40)


    # draw the border
    pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, WINDOWWIDTH, WINDOWHEIGHT), 1)

    pygame.display.update()
    FPSCLOCK.tick(FPS)

    step += 0.02
    step %= 2 * math.pi