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
BLUE       = (  0,   0, 255)
WHITE      = (255, 255, 255)
DARKRED    = (128,   0,   0)
DARKBLUE   = (  0,   0, 128)
RED        = (255,   0,   0)
GREEN      = (  0, 255,   0)
DARKGREEN  = (  0, 128,   0)
YELLOW     = (255, 255,   0)
DARKYELLOW = (128, 128,   0)
BLACK      = (  0,   0,   0)

BGCOLOR = WHITE

WINDOWWIDTH = 640 # width of the program's window, in pixels
WINDOWHEIGHT = 480 # height in pixels
WIN_CENTERX = int(WINDOWWIDTH / 2) # the midpoint for the width of the window
WIN_CENTERY = int(WINDOWHEIGHT / 2) # the midpoint for the height of the window

FPS = 160 # frames per second to run at

AMPLITUDE = 100 # how many pixels tall the waves with rise/fall.

# standard pygame setup code
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Trig Waves')
fontObj = pygame.font.Font('freesansbold.ttf', 16)

# variables that track visibility modes
showSine = True
showCosine = True
showHighAmpSine = True
showHighFreqSine = True
pause = False

xPos = 0
step = 0 # the current input f
posRecord = {'sin': [], 'cos': [], 'hiampsin': [], 'hifreqsin': []} # keeps track of the ball positions for drawing the waves

# making text Surface and Rect objects for various labels
sinLabelSurf         = fontObj.render('sine', True, RED, BGCOLOR)
cosLabelSurf         = fontObj.render('cosine', True, BLUE, BGCOLOR)
highAmpSinLabelSurf  = fontObj.render('hi amp sin', True, GREEN, BGCOLOR)
highFreqSinLabelSurf = fontObj.render('hi freq sin', True, YELLOW, BGCOLOR)

sinLabelRect         = sinLabelSurf.get_rect()
cosLabelRect         = cosLabelSurf.get_rect()
highAmpSinLabelRect  = highAmpSinLabelSurf.get_rect()
highFreqSinLabelRect = highFreqSinLabelSurf.get_rect()

instructionsSurf = fontObj.render('Press Q, W, E, R to toggle waves. P to pause.', True, BLACK, BGCOLOR)
instructionsRect = instructionsSurf.get_rect()
instructionsRect.left = 10
instructionsRect.bottom = WINDOWHEIGHT - 10

# main application loop
while True:
    # event handling loop for quit events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        # check for key presses that toggle pausing and wave visibility
        if event.type == KEYUP:
            if event.key == K_q:
                showSine = not showSine
            elif event.key == K_w:
                showCosine = not showCosine
            elif event.key == K_e:
                showHighAmpSine = not showHighAmpSine
            elif event.key == K_r:
                showHighFreqSine = not showHighFreqSine
            elif event.key == K_p:
                pause = not pause

    # fill the screen to draw from a blank state
    DISPLAYSURF.fill(BGCOLOR)

    # draw instructions
    DISPLAYSURF.blit(instructionsSurf, instructionsRect)

    # draw the horizontal middle line and the amplitude lines
    pygame.draw.line(DISPLAYSURF, BLACK, (0, WIN_CENTERY), (WINDOWWIDTH, WIN_CENTERY))
    pygame.draw.line(DISPLAYSURF, BLACK, (0, WIN_CENTERY + AMPLITUDE), (WINDOWWIDTH, WIN_CENTERY + AMPLITUDE))
    pygame.draw.line(DISPLAYSURF, BLACK, (0, WIN_CENTERY - AMPLITUDE), (WINDOWWIDTH, WIN_CENTERY - AMPLITUDE))


    # sine wave
    yPos = -1 * math.sin(step) * AMPLITUDE
    posRecord['sin'].append((int(xPos), int(yPos) + WIN_CENTERY))
    if showSine:
        # draw the sine ball and label
        pygame.draw.circle(DISPLAYSURF, RED, (int(xPos), int(yPos) + WIN_CENTERY), 10)
        sinLabelRect.center = (int(xPos), int(yPos) + WIN_CENTERY + 20)
        DISPLAYSURF.blit(sinLabelSurf, sinLabelRect)


    # cosine wave
    yPos = -1 * math.cos(step) * AMPLITUDE
    posRecord['cos'].append((int(xPos), int(yPos) + WIN_CENTERY))
    if showCosine:
        # draw the cosine ball and label
        pygame.draw.circle(DISPLAYSURF, BLUE, (int(xPos), int(yPos) + WIN_CENTERY), 10)
        cosLabelRect.center = (int(xPos), int(yPos) + WIN_CENTERY + 20)
        DISPLAYSURF.blit(cosLabelSurf, cosLabelRect)


    # high amplitude sine wave
    yPos = -1 * math.sin(step) * (AMPLITUDE + 100) # Note the "+ 100" to the amplitude!
    posRecord['hiampsin'].append((int(xPos), int(yPos) + WIN_CENTERY))
    if showHighAmpSine:
        # draw the high amplitude sine ball and label
        pygame.draw.circle(DISPLAYSURF, GREEN, (int(xPos), int(yPos) + WIN_CENTERY), 10)
        highAmpSinLabelRect.center = (int(xPos), int(yPos) + WIN_CENTERY + 20)
        DISPLAYSURF.blit(highAmpSinLabelSurf, highAmpSinLabelRect)


    # high frequency sine wave
    yPos = -1 * math.sin(step * 4) * AMPLITUDE # Note the "* 4" to the frequency
    posRecord['hifreqsin'].append((int(xPos), int(yPos) + WIN_CENTERY))
    if showHighFreqSine:
        # draw the high frequency sine ball and label
        pygame.draw.circle(DISPLAYSURF, YELLOW, (int(xPos), int(yPos) + WIN_CENTERY), 10)
        highFreqSinLabelRect.center = (int(xPos), int(yPos) + WIN_CENTERY + 20)
        DISPLAYSURF.blit(highFreqSinLabelSurf, highFreqSinLabelRect)



    # draw the waves from the previously recorded ball positions
    if showSine:
        for x, y in posRecord['sin']:
            pygame.draw.circle(DISPLAYSURF, DARKRED, (x, y), 4)
    if showCosine:
        for x, y in posRecord['cos']:
            pygame.draw.circle(DISPLAYSURF, DARKBLUE, (x, y), 4)
    if showHighAmpSine:
        for x, y in posRecord['hiampsin']:
            pygame.draw.circle(DISPLAYSURF, DARKGREEN, (x, y), 4)
    if showHighFreqSine:
        for x, y in posRecord['hifreqsin']:
            pygame.draw.circle(DISPLAYSURF, DARKYELLOW, (x, y), 4)

    # draw the border
    pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, WINDOWWIDTH, WINDOWHEIGHT), 1)

    pygame.display.update()
    FPSCLOCK.tick(FPS)

    if not pause:
        xPos += 0.5
        if xPos > WINDOWWIDTH:
            xPos = 0
            posRecord = {'sin': [], 'cos': [], 'hiampsin': [], 'hifreqsin': []}
            step = 0
        else:
            step += 0.008
            step %= 2 * math.pi
