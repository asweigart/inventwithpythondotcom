# Simplified BSD License, Copyright 2011 Al Sweigart

import pygcurse, pygame, sys
from pygame.locals import *
win = pygcurse.PygcurseWindow(40, 25)
win.autoblit = False


box = pygcurse.PygcurseTextbox(win, (4, 4, 20, 14), fgcolor='red', bgcolor='black', border='basic', wrap=True, marginleft=3, caption='Hello world!')
box.text = 'The Ojibway aboriginal people in North America used cowry shells which they called sacred Miigis Shells or whiteshells in Midewiwin ceremonies, and the Whiteshell Provincial Park in Manitoba, Canada is named after this type of shell. There is some debate about how the Ojibway traded for or found these shells, so far inland and so far north, very distant from the natural habitat. Oral stories and birch bark scrolls seem to indicate that the shells were found in the ground, or washed up on the shores of lakes or rivers. Finding the cowry shells so far inland could indicate the previous use of them by an earlier tribe or group in the area, who may have obtained them through an extensive trade network in the ancient past. Petroforms in the Whiteshell Provincial Park may be as old as 8,000 years.'
eraseBox = False
while True:
    for event in pygame.event.get(): # the event loop
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                box.height -= 1
            elif event.key == K_DOWN:
                box.height += 1
            elif event.key == K_LEFT:
                box.width -= 1
            elif event.key == K_RIGHT:
                box.width += 1
            elif event.key == K_w:
                box.y -= 1
            elif event.key == K_s:
                box.y += 1
            elif event.key == K_a:
                box.x -= 1
            elif event.key == K_d:
                box.x += 1
            elif event.key == K_r:
                box.x = 4
                box.y = 4
                box.width = 20
                box.height = 14
            elif event.key == K_p:
                win.fullscreen = not win.fullscreen
            elif event.key == K_d:
                win._debugchars()
            elif event.key == K_m:
                eraseBox = not eraseBox
            elif event.key == K_f:
                #win.font = pygame.sysfont.SysFont('freesansbold', 24, (255,0,0))
                win.height = 30
    win.setscreencolors('white', 'blue', clear=True)
    box.update()
    if eraseBox:
        box.erase()
    win.cursor = 0, win.height-3
    win.pygprint('WASD to move, arrow keys for height, p to switch to fullscreen.')
    win.cursor = 0, win.height-1
    win.putchars('x=%s, y=%s, width=%s, height=%s    ' % (box.x, box.y, box.width, box.height))
    win.blittowindow()

