# Pygcurse Maze
# By Al Sweigart al@inventwithpython.com
# Maze Generation code by Joe Wingbermuehle

# This program is a demo for the Pygcurse module.
# Simplified BSD License, Copyright 2011 Al Sweigart

import pygcurse, pygame, sys, random, time
from pygame.locals import *

BLUE = (0, 0, 128)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
RED = (255,0,0)

MAZE_WIDTH  = 41
MAZE_HEIGHT = 41
FPS = 40

win = pygcurse.PygcurseWindow(MAZE_WIDTH, MAZE_HEIGHT, fullscreen=False)
pygame.display.set_caption('Pygcurse Maze')
win.autowindowupdate = False
win.autoupdate = False


class JoeWingMaze():
    # Maze generator in Python
    # Joe Wingbermuehle
    # 2010-10-06
    # http://joewing.net/programs/games/python/maze.py

    def __init__(self, width=21, height=21):
        if width % 2 == 0:
            width += 1
        if height % 2 == 0:
            height += 1

        # The size of the maze (must be odd).
        self.width  = width
        self.height = height

        # The maze.
        self.maze = dict()

        # Generate and display a random maze.
        self.init_maze()
        self.generate_maze()
        #self.display_maze() # prints out the maze to stdout

    # Display the maze.
    def display_maze(self):
       for y in range(0, self.height):
          for x in range(0, self.width):
             if self.maze[x][y] == 0:
                sys.stdout.write(" ")
             else:
                sys.stdout.write("#")
          sys.stdout.write("\n")

    # Initialize the maze.
    def init_maze(self):
       for x in range(0, self.width):
          self.maze[x] = dict()
          for y in range(0, self.height):
             self.maze[x][y] = 1

    # Carve the maze starting at x, y.
    def carve_maze(self, x, y):
       dir = random.randint(0, 3)
       count = 0
       while count < 4:
          dx = 0
          dy = 0
          if   dir == 0:
             dx = 1
          elif dir == 1:
             dy = 1
          elif dir == 2:
             dx = -1
          else:
             dy = -1
          x1 = x + dx
          y1 = y + dy
          x2 = x1 + dx
          y2 = y1 + dy
          if x2 > 0 and x2 < self.width and y2 > 0 and y2 < self.height:
             if self.maze[x1][y1] == 1 and self.maze[x2][y2] == 1:
                self.maze[x1][y1] = 0
                self.maze[x2][y2] = 0
                self.carve_maze(x2, y2)
          count = count + 1
          dir = (dir + 1) % 4

    # Generate the maze.
    def generate_maze(self):
       random.seed()
       #self.maze[1][1] = 0
       self.carve_maze(1, 1)
       #self.maze[1][0] = 0
       #self.maze[self.width - 2][self.height - 1] = 0

       # maze generator modified to have randomly placed entrance/exit.
       startx = starty = endx = endy = 0
       while self.maze[startx][starty]:
           startx = random.randint(1, self.width-2)
           starty = random.randint(1, self.height-2)
       while self.maze[endx][endy] or endx == 0 or abs(startx - endx) < int(self.width / 3) or abs(starty - endy) < int(self.height / 3):
           endx = random.randint(1, self.width-2)
           endy = random.randint(1, self.height-2)

       self.maze[startx][starty] = 0
       self.maze[endx][endy] = 0

       self.startx = startx
       self.starty = starty
       self.endx = endx
       self.endy = endy





def main():
    newGame = True
    solved = False
    moveLeft = moveRight = moveUp = moveDown = False
    lastmovetime = sys.maxsize
    mainClock = pygame.time.Clock()
    while True:
        if newGame:
            newGame = False # if you want to see something cool, change the False to True
            jwmaze = JoeWingMaze(MAZE_WIDTH, MAZE_HEIGHT)
            maze = jwmaze.maze
            solved = False
            playerx, playery = jwmaze.startx, jwmaze.starty
            endx, endy = jwmaze.endx, jwmaze.endy
            breadcrumbs = {}

        if (playerx, playery) not in breadcrumbs:
            breadcrumbs[(playerx, playery)] = True

        # handle input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if solved or event.key == K_BACKSPACE:
                    newGame = True
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_UP:
                    moveUp = True
                    moveDown = False
                elif event.key == K_DOWN:
                    moveDown = True
                    moveUp = False
                elif event.key == K_LEFT:
                    moveLeft = True
                    moveRight = False
                elif event.key == K_RIGHT:
                    moveRight = True
                    moveLeft = False
                lastmovetime = time.time() - 1

            elif event.type == KEYUP:
                if event.key == K_UP:
                    moveUp = False
                elif event.key == K_DOWN:
                    moveDown = False
                elif event.key == K_LEFT:
                    moveLeft = False
                elif event.key == K_RIGHT:
                    moveRight = False

        # move the player (if allowed)
        if time.time() - 0.05 > lastmovetime:
            if moveUp and isOnBoard(playerx, playery-1) and maze[playerx][playery-1] == 0:
                playery -= 1
            elif moveDown and isOnBoard(playerx, playery+1) and maze[playerx][playery+1] == 0:
                playery += 1
            elif moveLeft and isOnBoard(playerx-1, playery) and maze[playerx-1][playery] == 0:
                playerx -= 1
            elif moveRight and isOnBoard(playerx+1, playery) and maze[playerx+1][playery] == 0:
                playerx += 1

            lastmovetime = time.time()
            if playerx == endx and playery == endy:
                solved = True

        # display maze
        drawMaze(win, maze, breadcrumbs)
        if solved:
            win.cursor = (win.centerx - 4, win.centery)
            win.write('Solved!', fgcolor=YELLOW, bgcolor=RED)
            moveLeft = moveRight = moveUp = moveDown = False
        win.putchar('@', playerx, playery, RED, BLACK)
        win.putchar('O', jwmaze.endx, jwmaze.endy, GREEN, BLACK)
        win.update()
        pygame.display.update()
        mainClock.tick(FPS)


def isOnBoard(x, y):
    return x >= 0 and y >= 0 and x < MAZE_WIDTH and y < MAZE_HEIGHT


def drawMaze(win, maze, breadcrumbs):
    for x in range(MAZE_WIDTH):
        for y in range(MAZE_HEIGHT):
            if maze[x][y] != 0:
                win.paint(x, y, BLUE)
            else:
                win.paint(x, y, BLACK)
            if (x, y) in breadcrumbs:
                win.putchar('.', x, y, RED, BLACK)

if __name__ == '__main__':
    main()