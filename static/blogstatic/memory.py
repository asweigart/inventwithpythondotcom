# Memory
# http://inventwithpython.com
# By Al Sweigart al@inventwithpython.com

"""
Welcome to the Code Comments for Memory. Code Comments is a series of simple games with detailed comments in the source code, so you can see how the game works.

The text in between the triple-double-quotes are comments. The Python interpreter ignores any text in between them, so we can add any comments about the source code without affecting the program. In general for Code Comments, the comments will describe the lines of code above the comment. It helps to view this file either on the Code Comments site or with a text editor that does "syntax highlighting", so that the comments appear in a separate color and are easier to distinguish from the code.

This Code Comments assumes you know some basic Python programming. If you are a beginner and would like to learn computer programming, there is a free book online called "Invent Your Own Computer Games with Python" at http://inventwithpython.com

The Code Comments programs make references to sections of this book throughout the program. This Code Comments can also teach you how to use the Pygame library to make your own games with graphics, animation, and sound. You can download Pygame from http://pygame.org and view its documentation at http://pygame.org/docs/

HOW TO PLAY MEMORY:
Click on one of the boxes to reveal the icon (that is, the colored shape) underneth. Click on another box where you think its matching twin is.

A QUICK WORD ABOUT THE DATA STRUCTURES USED IN MEMORY:
Variables can hold values of different types, such as integers (1, 2, 42, -5), floating point numbers (3.14, 5.0, -3.77) or strings ('Hello', 'SPAM', '42'). Some data types such as lists, tuples, and dictionaries can hold multiple other values. For example, [1, 2, 'Hello'] is a list value that holds three values (two integers and a string). Lists can also contain other lists as well.

We have a data structure that represents which boxes on the board contain what icons. It will be a list of lists of two-string tuples. Here is an example:
    mainBoard = [[(DONUT, RED), (DIAMOND, BLUE)], [(DIAMOND, BLUE'), (DONUT, RED)]]
This would be the data structure for a 2x2 board. Because it is a list of lists, the indexes we use can map to X Y coordinates, e.g. we can use mainBoard[0][0] for the top leftmost box, mainBoard[1][0] is the box to the right and mainBoard[0][1] is the box below the top leftmost one.

Remember, our XY coordinate system increases the X coordinate as we go to the right and increase the Y coordinate as we go down. It looks like this:

0,0    1,0    2,0    3,0    4,0
0,1    1,1    2,1    3,1    4,1
0,2    1,2    2,2    3,2    4,2
0,3    1,3    2,3    3,3    4,3
0,4    1,4    2,4    3,4    4,4

So the information for the icon for the box that is third from the left, second from the top would be at mainBoard[2][1]:

mainBoard[0][0]    mainBoard[1][0]    mainBoard[2][0]    mainBoard[3][0]    mainBoard[4][0]
mainBoard[0][1]    mainBoard[1][1]    mainBoard[2][1]    mainBoard[3][1]    mainBoard[4][1]
mainBoard[0][2]    mainBoard[1][2]    mainBoard[2][2]    mainBoard[3][2]    mainBoard[4][2]
mainBoard[0][3]    mainBoard[1][3]    mainBoard[2][3]    mainBoard[3][3]    mainBoard[4][3]
mainBoard[0][4]    mainBoard[1][4]    mainBoard[2][4]    mainBoard[3][4]    mainBoard[4][4]

Inside the list of lists, we store a tuple to denote the shape and color of the icon. The first item will be the color (which technically is itself a tuple of three integers, see the color constant variables below) and the second item is a string that describes the shape (either DONUT, SQUARE, DIAMOND, LINES, or OVAL).

This is the complete data structure for which boxes have which icons.

The data structure to keep track of which boxes have already been matched and revealed is also a list of lists, but it just contains True if the box should be revealed when drawn on the screen and False if it should be covered up. See the revealedBoxes variable for details.
"""

import random
import time
import pygame
import sys
from pygame.locals import *
"""Here we import modules that our game needs. random has random number functions, time has the sleep() function, sys has the exit() function, and pygame contains all the pygame-related functions.

pygame.locals contains constants like MOUSEMOTION and MOUSEBUTTONUP and QUIT for the events. It's easier to type MOUSEBUTTONUP instead of pygame.locals.MOUSEBUTTONUP, so we use the "from pygame.locals import *" format to import these to the local namespace.
"""

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8
COLS = 10
ROWS = 6
BOXSIZE = 40
GAPSIZE = 10
"""These constant variables (the uppercase names means we shouldn't change the values stored in them) set some standard values for our game. You can play around with different values for them (though some values might cause bugs in the game.) By using constants instead of the values directly, it is easier to make changes since we only have to change them in one place.

For example, if we used 8 instead of REVEALSPEED, then if we wanted to change our code later we'd have to change every place in the code we find 8. This is trickier than just changing the one line where REVEALSPEED is originally set.

More information about constants is at http://inventwithpython.com/chapter9.html#ConstantVariables
"""

DARKGRAY = (60, 60, 60)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BGCOLOR = DARKGRAY
BOXCOLOR = WHITE

"""We also set up some constant values for different colors. Pygame uses tuples of three integers to represent color. The integers represent the amount of red, green, and blue in the color (this is commonly called a RGB). 0 means there is none of the primary color in the color, and 255 means there is the maximum amount. So (255, 0, 0) is red, since it has the maximum amount of red but no green or blue. But (255, 0, 255) adds the max amount of blue with the red, creating purple.

More information about colors is at http://inventwithpython.com/chapter17.html#ColorsinPygame
"""

DONUT = 1
SQUARE = 2
DIAMOND = 3
LINES = 4
OVAL = 5
"""We also set up constants for the shapes. The number 1 will represent the donut shaped icons. However, if we simply used the integer 1 in our code, it would be hard to remember what 1 stood for. And if we made a typo such as 11, this bug could go undetected for quite some time and be hard to track down. By using the DONUT constant, it is easy to remember what the shape is, and any typos (such as DOMUT) would immediately cause an error on the line with DOMUT. One look at DOMUT at it is obvious to see that this is an incorrectly typed name.
"""


def main():
    global MAINCLOCK, MAINSURF
    """The main() function is where our program begins. (See the last two lines of code to see why.) Because we define MAINCLOCK and MAINSURF inside this function, these are local variables to the main() function and the names MAINCLOCK and MAINSURF won't exist outside of this function. By using a global statement, we can tell Python that we want these variables to be global variables.

    More information about global and local variables is at http://inventwithpython.com/chapter6.html#VariableScope
    """

    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    MAINSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    """pygame.init() needs to be called before any of the other Pygame functions.

    pygame.time.Clock() returns a pygame.Clock object. We will use this object's tick() method to ensure that the program runs at no faster than 30 frames per second (or whatever integer value we have in the FPS constant.)

    pygame.display.set_mode() creates the window on the screen and returns a pygame.Surface object. Any drawing done on this Surface object with the pygame.draw.* functions will be displayed on the screen when we call pygame.display.update().

    More information about pygame.display.set_mode() is at http://inventwithpython.com/chapter17.html#ThepygamedisplaysetmodeandpygamedisplaysetcaptionFunctions"""

    mousex = 0
    mousey = 0
    pygame.display.set_caption('Memory')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)
    """Here are some basic start-of-the-game settings we want to make. First we set the text of the window's caption. mousex and mousey will store the latest coordinates of the mouse cursor.

    mainBoard will contain the board data structure of what each box's icon is. It is a list of list of tuples of an integer and a tuple of three integers (whew!). The first list represents the rows, the second list represents the columns. The tuple has two values, an integer for the shape (one of the DONUT, OVAL, etc. constants) and an integer for the color.

    So mainBoard[0][0] contains an integer for the color of the topmost leftmost box. If this integer is, say, 2, then the color corresponds to COLORS[2] (which we have set up to be BLUE.) mainBoard[1][0] is the box to the right of mainBoard[0][0] and mainBoard[0][1] is the box below mainBoard[0][0].

    getRandomizedBoard() will return a board with randomly chosen icons, which is how the game starts off.

    revealedBoxes is a data structure that stores which matched pairs the player has found. This will be used to determine which boxes should be revealed and which should stay hidden. generateRevealedBoxesData returns a list of lists, with one value (False in the case above) for each box we have on the board."""

    firstStep = True
    firstSelection = None
    """These two variables keep track of which step it is. When the user clicks on a box for the first time, we will change firstStep from True to False, and save which box was clicked on to firstSelection. The next time the player clicks on a box, firstStep will be False (which is how we know this is the player's second step) and we can see if the box the player just clicked on matches the one in firstSelection.

    Afterwards, we reset firstStep back to True so that the next time the player clicks on a box it is seen as the first step of the two-step process."""

    MAINSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)
    """At the start of the game, we want to quickly flash through the contents of the board just to give the user a sneak peek at things. startGameAnimation() is the function that does this."""

    # Main game loop:
    while True:
        clicked = False

        # Draw the board.
        MAINSURF.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes)
        """This is the main game loop, which constantly loops while the program is playing. In this loop, we display the board on the screen and also handle any input events from the player. clicked will store the whether or not the player has clicked the mouse (the location is stored in mousex and mousey). We reset the value to False each time the game loop loops."""

        # Handle any events.
        for event in pygame.event.get():
            """The pygame.event.get() function returns a list of pygame.Event objects of events that have happened since the last call to pygame.event.get(). This loop uses the same code to handle each event in this list."""
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                """The QUIT event is created when the user tries to shut down the program by clicking the X in the top right corner, or by killing the program from the task manager or some other means."""
                pygame.quit()
                sys.exit()
                """In order to terminate the program, we must call both pygame.quit() (to shut down the Pygame engine) and sys.exit() (to shut down the program.)"""
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                """A MOUSEMOTION event is created whenever the user moves the mouse over the window. The Event object created has a pos attribute that is a tuple of the two xy integer coordinates for where the mouse is located. We will save these values off to mousex and mousey."""
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clicked = True
                """When the MOUSEBUTTONUP is created, we store the location of the mouse click (which is stored as the pos attribute of the Event object) and set clicked to True."""


        boxx, boxy = isOverBox(mousex, mousey)
        """If the latest mouse position that we received an Event object for was located over one of the boxes, then boxx and boxy will have the coordinates of that box (0, 0 will represent the top leftmost box). Otherwise, boxx and boxy will just contain the None value."""
        if boxx != None and boxy != None:
            # The mouse is over a box.

            if not revealedBoxes[boxx][boxy]:
                highlightBox(boxx, boxy)
            """To convey to the player that they can click on one of the covered up box, we add highlighting by drawing a blue rectangle around it. But we only want to add this highlighting to boxes that have not yet been revealed."""

            if clicked and not revealedBoxes[boxx][boxy]:
                # Player has clicked on an unrevealed box.
                revealBoxesAnimation(mainBoard, [(boxx, boxy)], REVEALSPEED)
                revealedBoxes[boxx][boxy] = True
                """Now we play the animation of the box revealing itself, and (for now anyway) mark the box as unrevealed."""

                if firstStep:
                    firstSelection = (boxx, boxy)
                    firstStep = False
                    """If this was the first of the two guesses, then we want to store this information and which box was clicked in firstStep and firstSelection."""
                else:
                    # Check if there is a match.
                    shape1, color1 = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    shape2, color2 = getShapeAndColor(mainBoard, boxx, boxy)

                    if shape1 != shape2 or color1 != color2:
                        # Icons don't match. Unreveal both selections.
                        time.sleep(0.8)
                        unrevealBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)], REVEALSPEED)
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes):
                        """Our hasWon() function will return True if all of the values in the revealedBoxes data structure are True, meaning that all of the shapes have been found. In this case, we display a special animation for winning, wait two seconds, and then reset the board for another game."""
                        gameWonAnimation(mainBoard)
                        time.sleep(2)

                        # Reset the board
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        # Show the fully unrevealed board for a second.
                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        time.sleep(1)

                        # Replay the start game animation.
                        startGameAnimation(mainBoard)
                    firstStep = True
                    """Since we are at the end of the second step, we want firstStep to be set to True again so that the next click from the player will be interpretted as the first of the two guesses."""

        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        MAINCLOCK.tick(FPS)
        """A call to pygame.display.update() causes any drawing functions done to the MAINSURF pygame.Surface object to be drawn to the screen. Unlike other pygame.Surface object, the object stored in MAINSURF was the one returned by the pygame.display.set_mode() call, which is why it is the Surface object that is drawn to the screen when pygame.display.update() is called.

        The call to MAINCLOCK.tick(FPS) will introduce a pause to the game so that the program doesn't run faster than 30 frames per second. (30 is the value we stored inside the FPS constant.) This is so that our program doesn't run too fast on very powerful computer."""

def generateRevealedBoxesData(val):
    dataStruct = []
    """Our "revealed boxes" data structure is a simple list of lists of boolean values. For example, if dataStruct[0][0] is set to False, that means the top leftmost box is not revealed. Like screen coordinates, 0, 0 represents the top left and the x coordinate increases going to the right and the y coordinate increases going down. So dataStruct[0][1] is the box below the top leftmost box and dataStruct[1][0] is the box to the right of the top leftmost box."""
    for c in range(COLS):
        dataStruct.append([val] * ROWS)
    return dataStruct


def splitIntoGroupsOf(groupSize, theList):
    """This is a function that is used by our "start game" animation. No matter how many boxes there are (which can vary with different values for COLS and ROWS), we only want to reveal a certain number of the boxes at a time. This function generically takes a list and an integer size, and returns a list of lists. Each of the lists inside the list is of size groupSize or less.

    For example, splitIntoGroupsOf(3, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) will return [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j']]"""
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i+groupSize])
    return result


def startGameAnimation(board):
    """At the start of the game, we will reveal all the boxes 8 at a time. To do this, we create a temporary "revealed boxes" data structure. Next we create a list (called boxes) of all the boxes on the board and randomly shuffle that list. This shuffled boxes is passed to splitIntoGroupsOf() and we get a list of lists of 8 (except the last list may have less than 8 if it just has the leftovers). We reveal these groups of boxes one group at a time."""

    tempRevealedBoxes = generateRevealedBoxesData(False)
    """tempRevealedBoxes stores a "revealed boxes" data structure with all the values set to False (meaning they are all covered up.)"""
    boxes = []
    for x in range(COLS):
        for y in range(ROWS):
            boxes.append( (x, y) )
    """At the end of these nested for loops, boxes will be a list containing a tuple for each of the boxes. So if our board was a 3x2 board (because COLS is 3 and ROWS is 2), then boxes would end up as [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]"""

    random.shuffle(boxes)
    """Next we shuffle the order of these tuples in boxes so that they will appear in random order."""

    groups = splitIntoGroupsOf(8, boxes)
    """Then we split up this list of tuples into lists of lists of 8 (or less for the last list) tuples."""

    for g in groups:
        drawBoard(board, tempRevealedBoxes)
        revealBoxesAnimation(board, g, REVEALSPEED)
        """Each list of 8 boxes stored is passed to revealBoxesAnimation(), which will uncover the boxes on the screen."""
        unrevealBoxesAnimation(board, g, REVEALSPEED)
        """After uncovering the boxes, we then want to re-cover them before revealing the next group of 8 boxes."""

def gameWonAnimation(board):
    global BGCOLOR, BOXCOLOR
    tempRevealedBoxes = generateRevealedBoxesData(True)
    """tempRevealedBoxes stores a "revealed boxes" data structure with all the values set to True (meaning they are all revealed.)"""

    for i in range(14):
        BGCOLOR, BOXCOLOR = BOXCOLOR, BGCOLOR
        """To add a flashing effect, we will reverse the background and box colors."""

        MAINSURF.fill(BGCOLOR)
        drawBoard(board, tempRevealedBoxes)
        pygame.display.update()
        time.sleep(0.3)
        """We redraw the board then display it on the screen by calling pygame.display.update(). Then we wait for a third of a second, and then iterate through the loop again."""


def hasWon(revealed):
    """We can check if the player has won by ensuring that every value in the "revealed boxes" data structure is set to True. The first time we find a False value, we go ahead and return False."""
    for i in revealed:
        if False in i:
            return False
    return True


def getShapeAndColor(board, boxx, boxy):
    """This function is only one line long, but it can be hard to remember that the shape and color are stored in board[boxx][boxy][0] and board[boxx][boxy][1]. Typing "getShapeAndColor()" with the parameters is much easier, so this function is more of a shortcut than anything."""
    return board[boxx][boxy][0], board[boxx][boxy][1]


def revealBoxesAnimation(board, boxes, speed):
    # Do the "box reveal" animation.
    """The sliding back animation that happens when we reveal a box is simple to explain. First, we'll always draw the background color over the entire area of the box, and then draw the icon on top of that. Then we draw varying amounts of the box color on top of that. Say that BOXSIZE is set to 40. First we'll want to draw the entire 40x40 box to fully cover the icon. Then on the next frame we only draw a 32x40 box, which means 8 columns of pixels of the icon can be seen. Then next we only draw a 24x40, so almost half of the icon can be seen. This keeps going until the box is fully revealed and we aren't drawing any of the covering box."""
    for i in range(BOXSIZE, -speed - 1, -speed):
        for b in boxes:
            """We add this nested for loop because we'll want to reveal multiple boxes at the same time (for example, in the starting animation). Of course, if the boxes list just has one box in it, then only one box is revealed and this for loop is moot. But having this for loop gives us the option for multiple boxes being revealed so we add it in."""
            drawBoxCover(board, b, i)
        pygame.display.update()
        MAINCLOCK.tick(FPS)

def unrevealBoxesAnimation(board, boxes, speed):
    # Do the "box cover" animation.
    """This function is pretty much the same as revealBoxesAnimation(), except the for loop is different."""
    for i in range(0, BOXSIZE, speed):
        for b in boxes:
            drawBoxCover(board, b, i)
        pygame.display.update()
        MAINCLOCK.tick(FPS)

def drawBoxCover(board, b, coverage):
    """Both the revealBoxesAnimation() and unrevealBoxesAnimation() do the exact same thing inside their nested for loops, so instead of copying and pasting that code twice, we just put the code in its own function and call that function twice. Getting rid of duplicated code this way is often a good idea, because if we want to change the code later (say, if we find a bug in it), then we only have to change it in one place instead of multiple places. It also makes our program shorter and easier to read."""
    left, top = leftTopOfBox(b[0], b[1])
    pygame.draw.rect(MAINSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
    shape, color = getShapeAndColor(board, b[0], b[1])
    drawShape(shape, color, b[0], b[1])
    if coverage > 0:
        pygame.draw.rect(MAINSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))

def getRandomizedBoard():
    # Get a list of every possible shape in every possible color.

    """The getRandomizedBoard() is called when we are starting a new game, and want the board to have randomly placed icons. But it can't be completely random, for each and every icon on the board, there has to be one (and only one) matching icon. This function makes sure that the board is formed correctly."""

    icons = []
    for c in (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN):
        for s in (DONUT, SQUARE, DIAMOND, LINES, OVAL):
            icons.append( (s, c) )
    """These nested for loops will ensure that the icons list will have a tuple representing every possible color and shape combination. We probably won't use all of these combinations, but for this function we want to start off with a complete list."""

    # To decide how many icons to use, shuffle the list and then truncate it.
    random.shuffle(icons)
    numIconsUsed = int(COLS * ROWS / 2)
    icons = icons[:numIconsUsed] * 2 # going to need pairs of icons
    """The above three lines shuffles the complete list of icons into random order. Then, we calculate how many icons we will use. There will be COLS x ROWS number of boxes on the board, however we need pairs of icons, so we divide that number by two. Note that if COLS and ROWS are both odd numbers, we will end up trying to divide an odd number by 2. This would create a bug in our program. Just be sure to set at least one of COLS or ROWS to an even number to prevent this.

    icons[:numIconsUsed] would be a slice with half of the icons we need. We double the content by multiplying this slice by 2. (Multiplying a list by an integer is called list replication.)"""

    # Create the board data structure.
    board = []
    """To create the board data structure, first we need to make a blank list. We will then add lists of icons to this list. (Remember that icons are just tuples of two integers for the shape and color.)"""
    for x in range(COLS):
        column = []
        """For each row, we start a new list for the column in that row."""
        for y in range(ROWS):
            randomIndex = random.randint(0, len(icons) - 1)
            column.append(icons[randomIndex])
            del icons[randomIndex]
            """First we randomly select an index from the list of icons we previously made. We then add the icon at that index to the column we are constructing. To ensure we don't use that particular icon again, we delete it from the list with a del statement. (Don't worry about the icon's twin. Remember we have two of each icon in the icons list.)

            More information about the del statement is at http://inventwithpython.com/chapter9.html#RemovingItemsfromListswithdelStatements
            """
        board.append(column)
        """After this loop has created the list of icons for this column, we add that list to the board list. On the next iteration of the outer loop, we create the next column."""
    return board


def leftTopOfBox(boxx, boxy):
    """Remember that we are using two different sets of cartesian coordinates in this program. The first is for the pixels in the window. The x axis of this cartesian coordinate system goes from 0 to WINDOWWIDTH and the y axis goes from 0 to WINDOWHEIGHT.

    The second set is used when we talk about the boxes on the board. The upper left box is at 0,0 (much like the upper left pixel is a 0,0). The x axis of this cartesian coordinate system goes from 0 to ROWS and the y axis goes from 0 to COLS.

    When we want to draw the box at, say, the board's cartesian coordinates of 2, 4, then this has to be translated to coordinates for the window's cartesian coordinate system. The leftTopOfBox() function will do this, and return a tuple of integers for the x, y position of the box in the window's coordinate system."""

    # See how big the margins are for each side.
    xmargin = int((WINDOWWIDTH - (COLS * (BOXSIZE + GAPSIZE))) / 2)
    ymargin = int((WINDOWHEIGHT - (ROWS * (BOXSIZE + GAPSIZE))) / 2)
    """First we need to calculate how big the margins on either side of the board are. For the x axis margin, start with the window's total width, and then subtract the box size and size of the gap in between boxes by the total number of boxes. Since we have two margins, we will want to divide this amount in half so that both margins are equally sized.

    Do the same for the y axis's margin, except use the window's height and the number of rows instead of columns."""
    left = boxx * (BOXSIZE + GAPSIZE) + xmargin
    top = boxy * (BOXSIZE + GAPSIZE) + ymargin
    """We can calculate the top left location of the box based on the box coordinates. Say this is the box 2, 3 (which is third from the left, and fourth down from the top because the first row and column of boxes are at 0.) To get the "left" value, we need to add the size of a box to the size of the gap in between boxes, and multiple it by 2. Then add the length of xmargin. Do the same to find the top, except use the y axis values.

    It may help to draw our the coordinates here. Let's say that BOXSIZE is 40 and GAPSIZE is 10. Also let's pretend the xmargin was calculated to 70 and ymargin to 90. Here are the box coordinates and window coordinates of the boxes:

                  ^                 ^                 ^                 ^                 ^
                  |                 |                 |                 |                 |
                 90                90                90                90                90
                  |                 |                 |                 |                 |
            +----------+      +----------+      +----------+      +----------+      +----------+
            |0,0       |      |1,0       |      |2,0       |      |3,0       |      |4,0       |
    <--70-->|70,90     |<-10->|120,90    |<-10->|170,90    |<-10->|220,90    |<-10->|270,90    |
            |<---40--->|      |<---40--->|      |<---40--->|      |<---40--->|      |<---40--->|
            +----------+      +----------+      +----------+      +----------+      +----------+
                  ^                 ^                 ^                 ^                 ^
                  |                 |                 |                 |                 |
                 10                10                10                10                10
                  |                 |                 |                 |                 |
            +----------+      +----------+      +----------+      +----------+      +----------+
            |0,1       |      |1,1       |      |2,1       |      |3,1       |      |4,1       |
    <--70-->|70,140    |<-10->|120,140   |<-10->|170,140   |<-10->|220,140   |<-10->|270,140   |
            |<---40--->|      |<---40--->|      |<---40--->|      |<---40--->|      |<---40--->|
            +----------+      +----------+      +----------+      +----------+      +----------+
                  ^                 ^                 ^                 ^                 ^
                  |                 |                 |                 |                 |
                 10                10                10                10                10
                  |                 |                 |                 |                 |
            +----------+      +----------+      +----------+      +----------+      +----------+
            |0,2       |      |1,2       |      |2,2       |      |3,2       |      |4,2       |
    <--70-->|70,190    |<-10->|120,190   |<-10->|170,190   |<-10->|220,190   |<-10->|270,190   |
            |<---40--->|      |<---40--->|      |<---40--->|      |<---40--->|      |<---40--->|
            +----------+      +----------+      +----------+      +----------+      +----------+
    """
    return (left, top)


def drawBoard(board, revealed):
    """Two data structures are passed to this function. "board" contains the information of which icons are where. "revealed" contains the information of which icons on the board are revealed and which are still hidden. We will use both of these data structures to determine if we should draw a hiding box or an icon, and if an icon then which icon."""
    for boxx in range(COLS):
        for boxy in range(ROWS):
            left, top = leftTopOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box.
                pygame.draw.rect(MAINSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                # Draw the icon.
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawShape(shape, color, boxx, boxy)


def isOverBox(x, y):
    """The isOverBox() function takes window coordinates and checks if they are over one of the boxes on the board. This function will be used so we know if the mouse is over a box (in which case, we draw the blue highlight around that box. It returns the box coordinates of the box it is over. If it is not over any boxes, it returns the tuple (None, None) instead."""
    for boxx in range(COLS):
        for boxy in range(ROWS):
            left, top = leftTopOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                """First we get the window coordinates of the top left corner of the box by calling our leftTopOfBox() function. We use this information to create a pygame.Rect object, because pygame.Rect objects have a collidepoint() method which will tell us if the coordinates we provide are inside of the rectangle the pygame.Rect object represents. If so, then collidepoint() returns True and we know we should return the current box's box coordinates."""
                return (boxx, boxy)
    return (None, None)


def highlightBox(boxx, boxy):
    left, top = leftTopOfBox(boxx, boxy)
    pygame.draw.rect(MAINSURF, BLUE, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)
    """The 4 argument we pass to pygame.draw.rect() function tells the function that we want the rectangle we are drawing to have an outline width of 4 pixels. To make the rectangle fatter, increase this number. If the number is set to 0 (or not passed at all, like in other calls to pygame.draw.rect(), then a filled rectangle will be drawn."""


def drawShape(shape, color, boxx, boxy):
    quarter = int(BOXSIZE * 0.25)
    half = int(BOXSIZE * 0.5)

    left, top = leftTopOfBox(boxx, boxy)
    """Each of the shapes has its own custom bit of code that draws it. We have this code in one of the if or elif blocks in this function. To find where in the window we should draw the shape, we get the top left corner of the box's position. To keep things proportional, we also get the size of 1/4 and 1/2 of the box stored in quarter and half, respectively."""
    if shape == DONUT:
        pygame.draw.circle(MAINSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(MAINSURF, BGCOLOR, (left + half, top + half), quarter - 5)
        """To draw the donut shape, first we draw a large circle (with a radius of half of the box size minus 5 pixels), and then draw the "hole" by drawing a smaller circle of the background color (with a radius of a quarter of the box size minus 5 pixels)."""
    elif shape == SQUARE:
        pygame.draw.rect(MAINSURF, color, (left + 10, top + 10, BOXSIZE - 20, BOXSIZE - 20))
    elif shape == DIAMOND:
        pygame.draw.polygon(MAINSURF, color, ((left + half, top), (left + BOXSIZE, top + half), (left + half, top + BOXSIZE), (left, top + half)))
        """We can draw the diamond shape by drawing a polygon with points in the middle of the top, right, bottom, and then left sides of the box in order."""
    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(MAINSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(MAINSURF, color, (left + i, top + BOXSIZE), (left + BOXSIZE, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(MAINSURF, color, (left, top + quarter, BOXSIZE, half))


if __name__ == '__main__':
    main()
    """This if statement is actually the first line of code that is run in our program (aside from the import statements and the constant variable assignments. __name__ is a special variable that is created for all Python programs implicitly. The value stored in this variable is the string '__main__', but only when the script is run by itself. If this script is imported by another script's import statement, then the value of __name__ will be the name of the file (if this script still has the name memory.py, then the __name__ variable will contain 'memory').

    This is really handy if we ever want to use the functions that are in this program in another program. By having this if statement here, which then runs the main() function, we could have another program use "import memory" and make use of any of the functions we've already written. Or if you want to test individual functions by calling them from the interactive shell, you could call them without running the game program. This trick is really handy for code reuse."""