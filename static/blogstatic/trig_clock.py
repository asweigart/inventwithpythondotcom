# Examples of the math.sin() and math.cos() trig functions in making a clock
# Al Sweigart al@inventwithpython.com

# You can learn more about Pygame with the
# free book "Making Games with Python & Pygame"
#
# http://inventwithpython.com/pygame
#

import sys, pygame, time, math
from pygame.locals import *

# set up a bunch of constants
BRIGHTBLUE = (  0,  50, 255)
WHITE      = (255, 255, 255)
DARKRED    = (128,   0,   0)
RED        = (255,   0,   0)
YELLOW     = (255, 255,   0)
BLACK      = (  0,   0,   0)

HOURHANDCOLOR = DARKRED
MINUTEHANDCOLOR = RED
SECONDHANDCOLOR = YELLOW
NUMBERBOXCOLOR = BRIGHTBLUE
BGCOLOR = WHITE

WINDOWWIDTH = 640 # width of the program's window, in pixels
WINDOWHEIGHT = 480 # height in pixels
WIN_CENTERX = int(WINDOWWIDTH / 2)
WIN_CENTERY = int(WINDOWHEIGHT / 2)


CLOCKNUMSIZE = 40 # size of the clock number's boxes
CLOCKSIZE = 200 # general size of the clock


# This function retrieves the x, y coordinates based on a "tick" mark, which ranges between 0 and 60
# A "tick" of 0 is at the top of the circle, 30 is at the bottom, 45 is at the "9 o'clock" position, etc.
# The "stretch" is how far from the origin the x, y return values will be
# "originx" and "originy" will be where the center of the circle is (almost always the center of the window)
def getTickPosition(tick, stretch=1.0, originx=WIN_CENTERX, originy=WIN_CENTERY):
    # uncomment to have a "rotating clock" feature.
    # This works by pushing the "tick" amount forward
    #tick += (time.time() % 15) * 4

    # The cos() and sin()
    tick -= 15

    # ensure that tick is between 0 and 60
    tick = tick % 60

    tick = 60 - tick

    # the argument to sin() or cos() needs to range between 0 and 2 * math.pi
    # Since tick is always between 0 and 60, (tick / 60.0) will always be between 0.0 and 1.0
    # The (tick / 60.0) lets us break up the range between 0 and 2 * math.pi into 60 increments.
    x =      math.cos(2 * math.pi * (tick / 60.0))
    y = -1 * math.sin(2 * math.pi * (tick / 60.0)) # "-1 *" because in Pygame, the y coordinates increase going down (the opposite of how they normally go in mathematics)

    # sin() and cos() return a number between -1.0 and 1.0, so multiply to stretch it out.
    x *= stretch
    y *= stretch

    # Then do the translation (i.e. sliding) of the x and y points.
    # NOTE: Always do the translation addition AFTER doing the stretch.
    x += originx
    y += originy

    return x, y


# these next 2 lines are used by the "pulsing clock" feature (see below)
originalClockSize = CLOCKSIZE
PULSESIZE = 20

# standard pygame setup code
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Trig Clock')
fontObj = pygame.font.Font('freesansbold.ttf', 26)

# render the Surface objects that have the clock numbers written on them
clockNumSurfs = [fontObj.render('%s' % (i), True, BGCOLOR, NUMBERBOXCOLOR)
                 for i in [12] + list(range(1, 12))] # Put 12 at the front of the list since clocks start at 12, not 1.


while True: # main application loop
    # event handling loop for quit events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    # fill the screen to draw from a blank state
    DISPLAYSURF.fill(BGCOLOR)

    # draw the numbers and number boxes of the clock
    for i in range(12):
        # set up the Rect objects for the numbers and the number boxes
        clockNumRect = clockNumSurfs[i].get_rect()
        clockNumRect.center = getTickPosition(i * 5, CLOCKSIZE)

        clockNumBoxRect = clockNumSurfs[i].get_rect()
        clockNumBoxRect.size = (CLOCKNUMSIZE, CLOCKNUMSIZE)
        clockNumBoxRect.center = getTickPosition(i * 5, CLOCKSIZE)

        # draw the numbers and the number boxes
        pygame.draw.rect(DISPLAYSURF, NUMBERBOXCOLOR, clockNumBoxRect)
        DISPLAYSURF.blit(clockNumSurfs[i], clockNumRect)

    # get the current time
    now = time.localtime()
    now_hour = now[3] % 12 # now[3] ranges from 0 to 23, so we mod 12.
    now_minute = now[4]
    now_second = now[5] + (time.time() % 1) # add the fraction of a second we get from time.time() to make a smooth-moving seconds hand

    # Uncomment this if you don't want the second hand to move smoothly:
    #now_second = now[5]

    # draw the hour hand
    x, y = getTickPosition(now_hour * 5 + (now_minute * 5 / 60.0), CLOCKSIZE * 0.6)
    pygame.draw.line(DISPLAYSURF, HOURHANDCOLOR, (WIN_CENTERX, WIN_CENTERY), (x, y), 8)

    # draw the minute hand
    x, y = getTickPosition(now_minute + (now_second / 60.0), CLOCKSIZE * 0.8)
    pygame.draw.line(DISPLAYSURF, MINUTEHANDCOLOR, (WIN_CENTERX, WIN_CENTERY), (x, y), 6)

    # draw the second hand
    x, y = getTickPosition(now_second, CLOCKSIZE * 0.8)
    pygame.draw.line(DISPLAYSURF, SECONDHANDCOLOR, (WIN_CENTERX, WIN_CENTERY), (x, y), 2)

    # draw the second hand's part that sticks out behind
    x, y = getTickPosition(now_second, CLOCKSIZE * -0.2) # negative stretch makes it go in the opposite direction
    pygame.draw.line(DISPLAYSURF, SECONDHANDCOLOR, (WIN_CENTERX, WIN_CENTERY), (x, y), 2)

    # draw border
    pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, WINDOWWIDTH, WINDOWHEIGHT), 1)

    pygame.display.update()

    # Uncomment this if you want the "pulsing clock" feature:
    #CLOCKSIZE = originalClockSize + math.sin(2 * math.pi * (time.time() % 1)) * PULSESIZE

