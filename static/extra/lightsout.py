# Lights Out!

import random # for the randint() function
import string # for the ascii_uppercase string
import math # for the sqrt() function
import sys # for the exit() function

def enterBoardSize():
    # Lets player type in board size.
    # Returns a two-item list of ints: [width, height]
    print('What board size do you want to play? Enter size as WIDTHxHEIGHT.')
    print('For example, type 3x3 or 5x7. Min is 3x3, max is 10x10.')
    while True:
        size = input()
        size = size.split('x')
        if len(size) == 2 and isValidSize(size[0]) and isValidSize(size[1]):
            return [int(size[0]), int(size[1])]
        print('Enter size as WIDTHxHEIGHT. Min size is 3, max size is 10.')


def isValidSize(n):
    # Returns True if n is a number and between 3 and 10. Otherwise returns False.
    return n.isdigit() and int(n) >= 3 and int(n) <= 10


def enterDifficulty():
    while True:
        print('Enter the difficulty: (1-9)')
        diff = input()
        if diff.isdigit() and int(diff) >= 1 and int(diff) <= 9:
            return int(diff)

def getWidthHeight(board):
    return [len(board), len(board[0])]


def drawBoard(board):
    width, height = getWidthHeight(board)

    print('    ' + '   '.join(string.ascii_uppercase[:width]))
    print('  +' + ('---+' * (width)))
    for y in range(height):
        print('  |' + '|'.join(getRow(board, y)) + '|')
        print(string.ascii_uppercase[y] + ' |' + '|'.join(getRow(board, y)) + '|')
        print('  |' + '|'.join(getRow(board, y)) + '|')
        print('  +' + ('---+' * (width)))


def getBoardSymbol(boardValue):
    # Returns 'O' if boardValue is True, otherwise '.'
    if boardValue:
        return 'O'
    else:
        return '.'

def getRow(board, row):
    # Returns a list of the board spaces for the row number given.
    width, height = getWidthHeight(board) # height isn't used in this function
    boardRow = []
    row = int(row)
    for i in range(width):
        boardRow.append(getBoardSymbol(board[i][row]) * 3) # * 3 because each space is 3x3 characters
    return boardRow

def getNewBoard(width, height):
    # Creates a brand new, blank board data structure.
    board = []
    for i in range(width):
        board.append([False] * height)
    return board

def getBoardCopy(board):
    width, height = getWidthHeight(board)
    dupeBoard = getNewBoard(width, height)
    for x in range(width):
        for y in range(height):
            dupeBoard[x][y] = board[x][y]
    return dupeBoard

def randomMoves(board, numMoves):
    width, height = getWidthHeight(board)
    for i in range(numMoves):
        makeMove(board, random.randint(0, width-1), random.randint(0, height-1))

def letterToIndex(letter):
    return string.ascii_uppercase.find(letter)

def isOnBoard(board, x, y):
    width, height = getWidthHeight(board)
    return x >= 0 and x < width and y >= 0 and y < height

def makeMove(board, x, y):
    if isOnBoard(board, x, y): # flip space
        board[x][y] = not board[x][y]
    if isOnBoard(board, x, y-1): # flip space above
        board[x][y-1] = not board[x][y-1]
    if isOnBoard(board, x, y+1): # flip space below
        board[x][y+1] = not board[x][y+1]
    if isOnBoard(board, x-1, y): # flip space to the left
        board[x-1][y] = not board[x-1][y]
    if isOnBoard(board, x+1, y): # flip space to the right
        board[x+1][y] = not board[x+1][y]

def enterMove(board):
    width, height = getWidthHeight(board)
    while True:
        print('Enter (A-%s)(A-%s), or quit, reset, or new:' % (string.ascii_uppercase[width-1], string.ascii_uppercase[height-1]))
        move = input().upper()

        if move == 'QUIT' or move == 'RESET' or move == 'NEW':
            return move
        elif len(move) == 2 and move.isalpha() and isOnBoard(board, letterToIndex(move[0]), letterToIndex(move[1])):
            return [letterToIndex(move[0]), letterToIndex(move[1])]

def playAgain():
    print('Do you want to reset this board, play a new game, or quit? (new/reset/quit)')
    while True:
        action = input().lower()
        if action.startswith('r'):
            return 'reset'
        elif action.startswith('n'):
            return 'new'
        elif action.startswith('q'):
            return 'quit'

        print('Please type in new, reset, or quit.')
                

def isBoardOff(board):
    width, height = getWidthHeight(board)
    for x in range(width):
        for y in range(height):
            if board[x][y]:
                return False
    return True

def showInstructions():
    print('''Instructions:
The Lights Out board is a made up of on (O) and off (.) lights.
Pushing down a light will reverse its state, and also the states of
the lights above, below, and to the left and right of it. (On lights
will turn off, off lights will turn on.)
The goal of the game is to turn off all the lights on the board in
as few moves as possible.

To enter a move, type the letter of the column followed by the letter
of the row you wish to push.
You can also type quit to exit the game, or type reset to start the
current puzzle over.
You can also type new to start a new game.''')
    print()


print('Welcome to Lights Out!')
print('Do you want instructions? (yes/no)')
if input().lower().startswith('y'):
    showInstructions()

while True:
    width, height = enterBoardSize()
    diff = enterDifficulty()

    theBoard = getNewBoard(width, height)
    # Make several random moves on the board depending on board size and difficulty.
    # round() returns a float, so call int() to cut off the trailing .0
    fewestMoves = diff * int(round(math.sqrt(width * height)))
    randomMoves(theBoard, fewestMoves)
    print('You should be able to solve this in at least %s moves.' % (fewestMoves))

    originalBoard = getBoardCopy(theBoard) # for when the player wants to reset the board
    movesTaken = 0
    while True:
        drawBoard(theBoard)
        if isBoardOff(theBoard):
            # Player has won the game
            print()
            print('*' * 50)
            print('Good job! You solved the puzzle in %s moves.' % (movesTaken))
            print('This puzzle can be solved in at least %s moves.' % (fewestMoves))
            print('*' * 50)
            print()
            action = playAgain()
            if action == 'reset':
                movesTaken = 0
                theBoard = getBoardCopy(originalBoard)
                continue
            elif action == 'new':
                break
            else: # default of quit
                print('Thanks for playing!')
                sys.exit()

        print('Turns taken: %s (Goal: %s)' % (movesTaken, fewestMoves))

        move = enterMove(theBoard)
        movesTaken += 1
        if move == 'RESET':
            movesTaken = 0
            theBoard = getBoardCopy(originalBoard)
        elif move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif move == 'NEW':
            break
        else:
            makeMove(theBoard, move[0], move[1])

