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
pygame.display.set_caption('Trig Pointer')

# create the base cannon image
cannonSurf = pygame.Surface((100, 100))
cannonSurf.fill(BGCOLOR)
pygame.draw.circle(cannonSurf, DARKGRAY, (20, 50), 20) # left end
pygame.draw.circle(cannonSurf, DARKGRAY, (80, 50), 20) # right end
pygame.draw.rect(cannonSurf, DARKGRAY, (20, 30, 60, 40)) # body
pygame.draw.circle(cannonSurf, BLACK, (80, 50), 15) # hole
pygame.draw.circle(cannonSurf, BLACK, (80, 50), 20, 1) # right end outline
pygame.draw.circle(cannonSurf, BROWN, (30, 70), 20) # wheel
pygame.draw.circle(cannonSurf, BLACK, (30, 70), 20, 1) # wheel outline


def getAngle(x1, y1, x2, y2):
    # Return value is 0 for right, 90 for up, 180 for left, and 270 for down (and all values between 0 and 360)

    # calculate the slope between the two points
    rise = y2 - y1
    run = x2 - x1
    if run != 0: # avoid "divide by zero" error
        slope = (rise) / float(run)
    else:
        slope = 0.0

    # get the angle between the two points (and "* (180 / math.pi)" to convert from radians to degrees)
    angle = math.atan( slope ) * (180 / math.pi)

    # make adjustments for which quadrant the event is in.
    if run < 0:
        angle += 180
    angle = 360 - angle # reverse the angle since on the screen, y increase as it goes _down_

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
    for cannonx, cannony in ((200, 150), (50, 300), (50, 50), (200, 400)):

        degrees = getAngle(cannonx, cannony, mousex, mousey)

        # rotate a copy of the cannon image and draw it
        rotatedSurf = pygame.transform.rotate(cannonSurf, degrees)
        rotatedRect = rotatedSurf.get_rect()
        rotatedRect.center = (cannonx, cannony)
        DISPLAYSURF.blit(rotatedSurf, rotatedRect)

    # draw the cross hairs over the mouse
    pygame.draw.line(DISPLAYSURF, BLACK, (mousex - 10, mousey), (mousex + 10, mousey))
    pygame.draw.line(DISPLAYSURF, BLACK, (mousex, mousey - 10), (mousex, mousey + 10))

    # draw the border
    pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, WINDOWWIDTH, WINDOWHEIGHT), 1)

    pygame.display.update()
    FPSCLOCK.tick(FPS)