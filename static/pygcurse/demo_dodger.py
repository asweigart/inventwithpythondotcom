# Pygcurse Dodger
# By Al Sweigart al@inventwithpython.com

# This program is a demo for the Pygcurse module.
# Simplified BSD License, Copyright 2011 Al Sweigart

import pygame, random, sys, time, pygcurse
from pygame.locals import *

GREEN = (0, 255, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

WINWIDTH = 40
WINHEIGHT = 50
TEXTCOLOR = WHITE
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
BADDIEMINSIZE = 1
BADDIEMAXSIZE = 5
BADDIEMINSPEED = 4
BADDIEMAXSPEED = 1
ADDNEWBADDIERATE = 3

win = pygcurse.PygcurseWindow(WINWIDTH, WINHEIGHT, fullscreen=False)
pygame.display.set_caption('Pygcurse Dodger')
win.autoupdate = False

def main():
    showStartScreen()
    pygame.mouse.set_visible(False)
    mainClock = pygame.time.Clock()
    gameOver = False

    newGame = True
    while True:
        if gameOver and time.time() - 4 > gameOverTime:
            newGame = True
        if newGame:
            newGame = False
            pygame.mouse.set_pos(win.centerx * win.cellwidth, (win.bottom - 4) * win.cellheight)
            mousex, mousey = pygame.mouse.get_pos()
            cellx, celly = win.getcoordinatesatpixel(mousex, mousey)
            baddies = []
            baddieAddCounter = 0
            gameOver = False
            score = 0

        win.fill(bgcolor=BLACK)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                terminate()
            if event.type == MOUSEMOTION and not gameOver:
                mousex, mousey = event.pos
                cellx, celly = win.getcoordinatesatpixel(mousex, mousey)

        # add new baddies if needed
        if baddieAddCounter == ADDNEWBADDIERATE:
            speed = random.randint(BADDIEMAXSPEED, BADDIEMINSPEED)
            baddies.append({'size': random.randint(BADDIEMINSIZE, BADDIEMAXSIZE),
                            'speed': speed,
                            'x': random.randint(0, win.width),
                            'y': -BADDIEMAXSIZE,
                            'movecounter': speed})
            baddieAddCounter = 0
        else:
            baddieAddCounter += 1


        # move baddies down, remove if needed
        for i in range(len(baddies)-1, -1, -1):
            if baddies[i]['movecounter'] == 0:
                baddies[i]['y'] += 1
                baddies[i]['movecounter'] = baddies[i]['speed']
            else:
                baddies[i]['movecounter'] -= 1

            if baddies[i]['y'] > win.height:
                del baddies[i]


        # check if hit
        if not gameOver:
            for baddie in baddies:
                if cellx >= baddie['x'] and celly >= baddie['y'] and cellx < baddie['x']+baddie['size'] and celly < baddie['y']+baddie['size']:
                    gameOver = True
                    gameOverTime = time.time()
                    break
            score += 1

        # draw baddies to screen
        for baddie in baddies:
            win.fill('#', GREEN, BLACK, (baddie['x'], baddie['y'], baddie['size'], baddie['size']))

        if not gameOver:
            playercolor = WHITE
        else:
            playercolor = RED
            win.putchars('GAME OVER', win.centerx-4, win.centery, fgcolor=RED, bgcolor=BLACK)

        win.putchar('@', cellx, celly, playercolor)
        win.putchars('Score: %s' % (score), win.width - 14, 1, fgcolor=WHITE)
        win.update()
        mainClock.tick(FPS)


def showStartScreen():
    while checkForKeyPress() is None:
        win.fill(bgcolor=BLACK)
        win.putchars('Pygcurse Dodger', win.centerx-8, win.centery, fgcolor=TEXTCOLOR)
        if int(time.time() * 2) % 2 == 0: # flashing
            win.putchars('Press a key to start!', win.centerx-11, win.centery+1, fgcolor=TEXTCOLOR)
        win.update()


def checkForKeyPress():
    # Go through event queue looking for a KEYUP event.
    # Grab KEYDOWN events to remove them from the event queue.
    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        if event.key == K_ESCAPE:
            terminate()
        return event.key
    return None


def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()