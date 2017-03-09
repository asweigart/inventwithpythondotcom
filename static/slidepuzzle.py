# Slide Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license
# Original "slidepuzzle.py" has been updated (commented) by Kun Lee T03
import pygame, sys, random  #The program uses pygame module to design slide puzzle game
from pygame.locals import *

# Create the constants for game display 
BOARDWIDTH = 4  
BOARDHEIGHT = 4 
TILESIZE = 80
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30
BLANK = None

#                 R    G    B   :Assign color codes to variables for ease of use
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
BRIGHTBLUE =    (  0,  50, 255)
DARKTURQUOISE = (  3,  54,  73)
GREEN =         (  0, 204,   0)

BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE
#Calculate horizontal and vertical margins
XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
#Assign variables for user's keyboard input
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main(): #this function implements all other functions defined below to handle game events and create repsonses based on user's actions
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT
#Set initial settings of the game(timer, display, text, font)
    pygame.init() # Initialize all pygame modules imported
    FPSCLOCK = pygame.time.Clock() # FPSCLOCK will be used to track time
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # Initialize a window for display
    pygame.display.set_caption('Slide Puzzle') # Set the name of a window tile
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE) # Set the font of texts

    # Store the option buttons and their rectangles in OPTIONS (will be displayed at lower right corner of the game by drawBoard function)
    RESET_SURF, RESET_RECT = makeText('Reset',    TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 90)
    NEW_SURF,   NEW_RECT   = makeText('New Game', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 60)
    SOLVE_SURF, SOLVE_RECT = makeText('Solve',    TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 30)

    mainBoard, solutionSeq = generateNewPuzzle(80)
    SOLVEDBOARD = getStartingBoard() # a solved board is the same as the board in a start state.
    allMoves = [] # list of moves made from the solved configuration

    while True: # main game loop
        slideTo = None # the direction, if any, a tile should slide
        msg = 'Click tile or press arrow keys to slide.' # contains the message (will be shown in the upper left corner)
        if mainBoard == SOLVEDBOARD: #Change message state when the user accomplishes the game
            msg = 'Solved!'

        drawBoard(mainBoard, msg) # Display the entire game on a window

        checkForQuit() # If user requests to terminate the game, this function will quit the program from Python
        for event in pygame.event.get(): # event handling loop (while loop + for loop -> for all events by user) 
            if event.type == MOUSEBUTTONUP: # For the case where mouse is used
                spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1]) # Locate where the mouse is clicked

                if (spotx, spoty) == (None, None):
                    # check if the user clicked on an option button (none of the tiles are clicked)
                    if RESET_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, allMoves) # clicked on Reset button
                        allMoves = []
                    elif NEW_RECT.collidepoint(event.pos):
                        mainBoard, solutionSeq = generateNewPuzzle(80) # clicked on New Game button
                        allMoves = []
                    elif SOLVE_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, solutionSeq + allMoves) # clicked on Solve button
                        allMoves = []
                else:
                    # check if the clicked tile was next to the blank spot

                    blankx, blanky = getBlankPosition(mainBoard) # Locate where the blank tile is 
                    if spotx == blankx + 1 and spoty == blanky: # Depending on which tile (next to the blank tile) is clicked, the tile will be moved to blank tile's location
                        slideTo = LEFT
                    elif spotx == blankx - 1 and spoty == blanky:
                        slideTo = RIGHT
                    elif spotx == blankx and spoty == blanky + 1:
                        slideTo = UP
                    elif spotx == blankx and spoty == blanky - 1:
                        slideTo = DOWN 

            elif event.type == KEYUP:
                # check if the user pressed a key to slide a tile (perform same as from line 85 to 96 but keyboard input is used)
                if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT):
                    slideTo = LEFT
                elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
                    slideTo = RIGHT
                elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
                    slideTo = UP
                elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
                    slideTo = DOWN

        if slideTo: # If a tile moves (slideTo value is changed) slideAnimation function will demonstrate the animation for moving the selected tile on the board 
            slideAnimation(mainBoard, slideTo, 'Click tile or press arrow keys to slide.', 8) # show sliding of a tile on screen
            makeMove(mainBoard, slideTo)
            allMoves.append(slideTo) # record the slide
        pygame.display.update() # Performs as pygame.display.flip() (entire displayment will be updated)
        FPSCLOCK.tick(FPS) # From line 15, FPS = 30 -> the game will run 30 frames per second


def terminate():
    pygame.quit() # Uninitialize all pygame modules that have previously been initialized (does not exit the program)
    sys.exit() # Raise the SystemExit exception -> Exit from Python


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


def getStartingBoard():
    # Return a board data structure with tiles in the solved state.
    # All tile numbers will be in order where the numbers increase from left to right by rows (blank tile at botton right of the board)
    
    counter = 1 # "counter" tracks the tile number 
    board = []
    for x in range(BOARDWIDTH): 
        column = []
        for y in range(BOARDHEIGHT): # "counter" will be incremented verticallay (column -> y) by the width of the board 
            column.append(counter)
            counter += BOARDWIDTH
        board.append(column) 
        counter -= BOARDWIDTH * (BOARDHEIGHT - 1) + BOARDWIDTH - 1 # "counter" is set to first row number of next column
                                                                # "counter" will start incrementing at the start of the next column 
    board[BOARDWIDTH-1][BOARDHEIGHT-1] = BLANK # Blank tile is placed at botton right of the board
    return board


def getBlankPosition(board):
    # Return the x and y of board coordinates of the blank space.
    for x in range(BOARDWIDTH): # Check every single tile of the board (using double array concept) 
        for y in range(BOARDHEIGHT):
            if board[x][y] == BLANK: # Since there is only one blank tile on the board, no need to check every tiles
                return (x, y)       # If one blank tile is found, stop the searching


def makeMove(board, move):
    # This function does not check if the move is valid.
    blankx, blanky = getBlankPosition(board) # Locate the horizontal and vertical coordinate of a blank tile
    # Swap the coordinates(location) of blank tile and selected tile (no need for swap function <- Python supports multiple concurrent assignments)
    if move == UP:
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
    elif move == DOWN:
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
    elif move == LEFT:
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
    elif move == RIGHT:
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]


def isValidMove(board, move): # Return true if the movement is possible, false otherwise (line 173~176 checks if the location of blank tile allows the move)
    blankx, blanky = getBlankPosition(board) #Depending on the coordinate of blank tile, a tile cannot move to the following directions (will be stopped at the end of the board)
    return (move == UP and blanky != len(board[0]) - 1) or \
           (move == DOWN and blanky != 0) or \
           (move == LEFT and blankx != len(board) - 1) or \
           (move == RIGHT and blankx != 0)
            # Backslash '\' is used to seperate one line into multiple lines (for the purpose of nice formatting)

def getRandomMove(board, lastMove=None): # Function that creates randomly ordered tiles (will be used for generateNewPuzzle function)
    # start with a full list of all four moves
    validMoves = [UP, DOWN, LEFT, RIGHT]

    # remove moves from the list as they are disqualified (b/c if the tile moves to oppposite direction, the tile is back to the original location) 
    if lastMove == UP or not isValidMove(board, DOWN): # Need to prevent tile from going back -> remove the movement to opposite direction
        validMoves.remove(DOWN)
    if lastMove == DOWN or not isValidMove(board, UP):
        validMoves.remove(UP)
    if lastMove == LEFT or not isValidMove(board, RIGHT):
        validMoves.remove(RIGHT)
    if lastMove == RIGHT or not isValidMove(board, LEFT):
        validMoves.remove(LEFT)

    # return a random move from the list of remaining moves
    return random.choice(validMoves)


def getLeftTopOfTile(tileX, tileY): # Locate the pixel coordinate of left top of a tile (converts board coordinate to pixel coordinate)
    left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
    top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)
    return (left, top) # Will act as a reference point


def getSpotClicked(board, x, y):
    # from the x & y pixel coordinates, get the x & y board coordinates
    for tileX in range(len(board)): # Double for loops will go through every possible xy board coordinates
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX, tileY)
            tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE) # "tileRect" gets the coordinate of top left of a tile to represent space of a tile
            if tileRect.collidepoint(x, y): # Use collideoint method to check if (x,y) coordinate is inside the space of a tile
                return (tileX, tileY) # Returns the tile that is clicked
    return (None, None) # In the case when mouse clicked outside the board


def drawTile(tilex, tiley, number, adjx=0, adjy=0):
    # draw a tile at board coordinates tilex and tiley, optionally a few
    # pixels over (determined by adjx and adjy)
    left, top = getLeftTopOfTile(tilex, tiley)
    pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE)) #pygame.draw method only takes pixel coordinates
    textSurf = BASICFONT.render(str(number), True, TEXTCOLOR) # Create surfaces that have numbers written on tiles (at centre point)
    textRect = textSurf.get_rect()
    textRect.center = left + int(TILESIZE / 2) + adjx, top + int(TILESIZE / 2) + adjy 
    DISPLAYSURF.blit(textSurf, textRect) #Draw the tile (draw the surface on rectangle)


def makeText(text, color, bgcolor, top, left):
    # create the Surface and Rect objects for some text and set the location where the text will be placed
    textSurf = BASICFONT.render(text, True, color, bgcolor) # Create the text surface(message) 
    textRect = textSurf.get_rect() # Create the text area (rectangular)
    textRect.topleft = (top, left) # Text Location
    return (textSurf, textRect)


def drawBoard(board, message): 
    DISPLAYSURF.fill(BGCOLOR) # Fill the surface with "BGCOLOR"
    if message: # If there is a message, display on the board
        textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
        DISPLAYSURF.blit(textSurf, textRect) # Draw textSurf on textRect

    for tilex in range(len(board)): # Find where tiles should be located and draw them on the board
        for tiley in range(len(board[0])):
            if board[tilex][tiley]: # There will be one empty spot where no tile will be displayed (b/c this game is a slide puzzle)
                drawTile(tilex, tiley, board[tilex][tiley])

    left, top = getLeftTopOfTile(0, 0) # Find the size of boarder that will wrap the tiles
    width = BOARDWIDTH * TILESIZE
    height = BOARDHEIGHT * TILESIZE
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)

    DISPLAYSURF.blit(RESET_SURF, RESET_RECT) # Display option menus 
    DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
    DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)


def slideAnimation(board, direction, message, animationSpeed):
    # Note: This function does not check if the move is valid.

    blankx, blanky = getBlankPosition(board)
    if direction == UP: # Based on the location of blank tile, the next location (after movement) of the blank tile is found
        movex = blankx  # Location is computed depending on the direction
        movey = blanky + 1
    elif direction == DOWN:
        movex = blankx
        movey = blanky - 1
    elif direction == LEFT:
        movex = blankx + 1
        movey = blanky
    elif direction == RIGHT:
        movex = blankx - 1
        movey = blanky

    # prepare the base surface
    drawBoard(board, message)
    baseSurf = DISPLAYSURF.copy() # baseSurf and DISPLAYSURF are two different surfaces
    # draw a blank space over the moving tile on the baseSurf Surface (so that when the tile moves, the baseSurf tile won't remain)
    moveLeft, moveTop = getLeftTopOfTile(movex, movey)
    pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, TILESIZE, TILESIZE))

    for i in range(0, TILESIZE, animationSpeed):# the tile will move close and closer to the destination (from 0 to the disance between two tiles at a speed of animatinoSpeed)
                                                # and animate the tile sliding over
        checkForQuit() # If user requests, terminate the game
        DISPLAYSURF.blit(baseSurf, (0, 0))
        if direction == UP: # tile movement depends on the dirction
            drawTile(movex, movey, board[movex][movey], 0, -i) # "i" represents frame per second (increments by animationSpeed)
        if direction == DOWN:
            drawTile(movex, movey, board[movex][movey], 0, i)
        if direction == LEFT:
            drawTile(movex, movey, board[movex][movey], -i, 0)
        if direction == RIGHT:
            drawTile(movex, movey, board[movex][movey], i, 0)

        pygame.display.update()# Update the displayment
        FPSCLOCK.tick(FPS)


def generateNewPuzzle(numSlides): # Create new board structure
    # From a starting configuration, make numSlides number of moves (and
    # animate these moves).
    sequence = []
    board = getStartingBoard()
    drawBoard(board, '')
    pygame.display.update()
    pygame.time.wait(500) # pause 500 milliseconds for effect (tiles are not moving for 0.5 sec)
    lastMove = None
    for i in range(numSlides):
        move = getRandomMove(board, lastMove) # Mix the tiles randomly (at the start of each new game) -> allows users to enjoy different trials
        slideAnimation(board, move, 'Generating new puzzle...', animationSpeed=int(TILESIZE / 3)) # Animate the movements first
        makeMove(board, move) # Then update the tiles
        sequence.append(move) # The random movements by tiles are saved -> When user clicks Solve button, this sequence will be used to undo all the movements
        lastMove = move # Prevents tiles from moving back to original places (b/c "move" is passed to line 305)
    return (board, sequence)


def resetAnimation(board, allMoves):
    # make all of the moves in allMoves in reverse.
    revAllMoves = allMoves[:] # gets a copy of the list ([:] -> creates entire list)
    revAllMoves.reverse()

    for move in revAllMoves:
        if move == UP: # B/c this function reverses the movements, direction of the move is set to opposite direction
            oppositeMove = DOWN
        elif move == DOWN:
            oppositeMove = UP
        elif move == RIGHT:
            oppositeMove = LEFT
        elif move == LEFT:
            oppositeMove = RIGHT
        slideAnimation(board, oppositeMove, '', animationSpeed=int(TILESIZE / 2))
        makeMove(board, oppositeMove)


if __name__ == '__main__': # Automatically calls main() function -> When this code gets executed, the game will begin right away
    main()
