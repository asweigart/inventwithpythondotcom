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
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)
BROWN    = (139,  69,  19)
DARKGRAY = (128, 128, 128)

BGCOLOR = WHITE

WINDOWWIDTH = 640 # width of the program's window, in pixels
WINDOWHEIGHT = 480 # height in pixels

FPS = 30


# standard pygame setup code
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Trig Eyes')


def getAngle(x1, y1, x2, y2):
    # Return value is 0 for right, 90 for up, 180 for left, and 270 for down (and all values between 0 and 360)
    angle = math.atan2(x1 - x2, y1 - y2) # get the angle in radians
    angle = angle * (180 / math.pi) # convert to degrees
    angle = (angle + 90) % 360 # adjust for a right-facing sprite
    return angle


# main application loop
while True:
    # event handling loop for quit events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    # fill the screen to draw from a blank state
    DISPLAYSURF.fill(BGCOLOR)

    # draw the cannons pointed at the mouse cursor
    mousex, mousey = pygame.mouse.get_pos()

    for eyex, eyey in ((100, 100), (140, 100), (400, 400), (440, 400), (500, 250), (540, 250)):
        degrees = getAngle(eyex, eyey, mousex, mousey)

        # draw the outline of the eye
        pygame.draw.circle(DISPLAYSURF, BLACK, (eyex, eyey), 15, 1)

        # draw the black part of the eye
        xPos = math.cos(degrees * (math.pi / 180)) * 5
        yPos = math.sin(degrees * (math.pi / 180)) * 5
        pygame.draw.circle(DISPLAYSURF, BLACK, (int(xPos) + eyex, -1 * int(yPos) + eyey), 10)

    # draw the cross hairs over the mouse
    pygame.draw.line(DISPLAYSURF, BLACK, (mousex - 10, mousey), (mousex + 10, mousey))
    pygame.draw.line(DISPLAYSURF, BLACK, (mousex, mousey - 10), (mousex, mousey + 10))

    # draw the border
    pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, WINDOWWIDTH, WINDOWHEIGHT), 1)

    pygame.display.update()
    FPSCLOCK.tick(FPS)
