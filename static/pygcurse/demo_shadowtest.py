# Simplified BSD License, Copyright 2011 Al Sweigart

import pygcurse, pygame, sys
from pygame.locals import *
win = pygcurse.PygcurseWindow(40, 25)
win.autoblit = False

xoffset = 1
yoffset = 1
mousex = mousey = 0
while True:
    for event in pygame.event.get(): # the event loop
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                yoffset -= 1
            elif event.key == K_DOWN:
                yoffset += 1
            elif event.key == K_LEFT:
                xoffset -= 1
            elif event.key == K_RIGHT:
                xoffset += 1
            elif event.key == K_p:
                win.fullscreen = not win.fullscreen
            elif event.key == K_d:
                win._debugchars()
        elif event.type == MOUSEMOTION:
            mousex, mousey = win.getcoordinatesatpixel(event.pos, onscreen=False)

    win.setscreencolors('white', 'blue', clear=True)
    win.fill(bgcolor='red', region=(15, 10, 5, 5))
    win.addshadow(51, (15, 10, 5, 5), xoffset=xoffset, yoffset=yoffset)

    #win.drawline((6,6), (mousex, mousey), bgcolor='red')
    win.drawline((6,6), (mousex, mousey), char='+', fgcolor='yellow', bgcolor='green')

    win.cursor = 0, win.height-3
    win.write('Use mouse to move line, arrow keys to move shadow, p to switch to fullscreen.')
    win.cursor = 0, win.height-1
    win.putchars('xoffset=%s, yoffset=%s    ' % (xoffset, yoffset))
    win.blittowindow()
