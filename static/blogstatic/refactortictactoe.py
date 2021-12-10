def checkLETTER1(PlayerOne):
    #This is a function that checks whether the input of player one is either lower case x or lower case o
    if PlayerOne == 'x' or PlayerOne =='o':
        print('''PlayerOne has selected ''' + str(PlayerOne)+
        ''' PlayerTwo please select a letter''')

    elif PlayerOne != 'x' and PlayerOne !='o':
        print('''PlayerOne please select what letter you are going to be. Either LOWERCASE x or LOWERCASE o''')

def checkLETTER2(PlayerTwo):
    #This is a function that checks whether the input of player two is either lower case x or lower case o
    if (PlayerTwo == 'x' or PlayerTwo =='o') and (PlayerTwo != PlayerOne):
        print('''PlayerTwo has selected ''' + str(PlayerTwo)+
        ''' PlayerOne please make a move''')

    elif (PlayerTwo != 'x' or PlayerTwo !='o') and(PlayerTwo != PlayerOne) :
        print('''PlayerTwo please select what letter you are going to be. Either LOWERCASE x or LOWERCASE o''')
    elif (PlayerTwo != 'x' or PlayerTwo !='o') and(PlayerTwo == PlayerOne):
        print('''PlayerOne already picked that letter''')
def checkPlayerOneMove(PlayerOneMove):
    #this function checks whether player ones move was valid and if so places his letter on the location they specfied
    if PlayerOneMove in moves:
        indexPlayerOneMove = moves.index(PlayerOneMove)
        if board[PlayerOneMove]==' ':
            board[PlayerOneMove]=PlayerOne
            validMOVE1 = 1
            return validMOVE1, board
        else:
            print('''That spot has been taken up''')
            validMOVE = 0
            return validMOVE
    elif PlayerOneMove not in moves:
        print('''This not one of the moves you can make have a look at the instuctions again''')
        print('''
        top-L = placing letter in the top left space
        top-M = placing letter in the top middle space
        top-R = placing letter in the top right space
        mid-L = placing letter in the center left space
        mid-M = placing letter in the center middle space
        mid-R = placing letter in the center right space
        low-L = placing letter in the bottom left space
        low-M = placing letter in the bottom middle space
        low-R = placing letter in the bottom right space''')
        validMOVE1 = 0
        return validMOVE1
def checkPlayerTwoMove(PlayerTwoMove):
    #this function checks whether player ones move was valid and if so places his letter on the location they specfied
    if PlayerTwoMove in moves:
        indexPlayerTwoMove = moves.index(PlayerTwoMove)
        if board[PlayerTwoMove]==' ':
            board[PlayerTwoMove]=PlayerTwo
            validMOVE2 = 1
            return validMOVE2, board
        else:
            print('''That spot has been taken up''')
            validMOVE2 = 0
            return validMOVE2
    elif PlayerTwoMove not in moves:
        print('''This not one of the moves you can make have a look at the instuctions again''')
        print('''
        top-L = placing letter in the top left space
        top-M = placing letter in the top middle space
        top-R = placing letter in the top right space
        mid-L = placing letter in the center left space
        mid-M = placing letter in the center middle space
        mid-R = placing letter in the center right space
        low-L = placing letter in the bottom left space
        low-M = placing letter in the bottom middle space
        low-R = placing letter in the bottom right space''')
        validMOVE2 = 0
        return validMOVE2
def print_board(board):
    #This function prints the board
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
def check_winner(board):
    #this function checks who won the game
    if board['top-L']== board['top-M']== board['top-R']:
        if PlayerOne == board['top-L']:
            print('PlayerOne has won')
            return 1
        elif PlayerTwo == board['top-L']:
            print('PlayerTwo has won')
            return 1
        elif board['top-L']==' ':
            print('Nobody has won yet')
    if board['top-L']== board['mid-L']== board['low-L']:
        if PlayerOne == board['top-L']:
            print('PlayerOne has won')
            return 1
        elif PlayerTwo == board['top-L']:
            print('PlayerTwo has won')
            return 1
        elif board['top-L']== ' ':
            print('Nobody has won yet')
    if board['top-L']== board['mid-M']== board['low-R']:
        if PlayerOne == board['top-L']:
            print('PlayerOne has won')
            return 1
        elif PlayerTwo == board['top-L']:
            print('PlayerTwo has won')
            return 1
        elif board['top-L']==' ':
            print('Nobody has won yet')
    if board['top-R']== board['mid-M']== board['low-L']:
        if PlayerOne == board['top-R']:
            print('PlayerOne has won')
            return 1
        elif PlayerTwo == board['top-R']:
            print('PlayerTwo has won')
            return 1
        elif board['top-R']==' ':
            print('Nobody has won yet')
    if board['top-R']== board['mid-R']== board['low-R']:
        if PlayerOne == board['top-R']:
            print('PlayerOne has won')
            return 1
        elif PlayerTwo == board['top-R']:
            print('PlayerTwo has won')
            return 1
        elif board['top-R']== ' ':
            print('Nobody has won yet')
    if board['mid-R']== board['mid-L']== board['mid-M']:
        if PlayerOne == board['mid-R']:
            print('PlayerOne has won')
            return 1
        elif PlayerTwo == board['mid-R']:
            print('PlayerTwo has won')
            return 1
        elif board['mid-R']== ' ':
            print('Nobody has won yet')
    if board['mid-M']== board['top-M']== board['low-M']:
        if PlayerOne == board['mid-M']:
            print('PlayerOne has won')
            return 1
        elif PlayerTwo == board['mid-M']:
            print('PlayerTwo has won')
            return 1
        elif board['mid-M'] == ' ':
            print('Nobody has won yet')
    if board['low-M']== board['low-L']== board['low-R']:
        if PlayerOne == board['low-M']:
            print('PlayerOne has won')
            return 1
        elif PlayerTwo == board['low-M']:
            print('PlayerTwo has won')
            return 1
        elif board['low-M'] == ' ':
            print('Nobody has won yet')

print('''Welcome to this game of tic-tac-toe.
PlayerOne please select what letter you are going to be. Either LOWERCASE x or LOWERCASE o''')
PlayerOne = input()
checkLETTER1(PlayerOne)

while PlayerOne != 'x' and PlayerOne !='o':
    #this is a while loop that keeps asking for a input and then checks the input until player one is either x or o
    PlayerOne = input()
    checkLETTER1(PlayerOne)

PlayerTwo = input()
checkLETTER2(PlayerTwo)

while (PlayerTwo != 'x' and PlayerTwo !='o') or (PlayerTwo == PlayerOne) :
    #this is a while loop that keeps asking for a input and then checks the input until player two is either x or o
    PlayerTwo = input()
    checkLETTER2(PlayerTwo)
#the nex following code prints the instructions
print('''
        top-L = placing letter in the top left space
        top-M = placing letter in the top middle space
        top-R = placing letter in the top right space
        mid-L = placing letter in the center left space
        mid-M = placing letter in the center middle space
        mid-R = placing letter in the center right space
        low-L = placing letter in the bottom left space
        low-M = placing letter in the bottom middle space
        low-R = placing letter in the bottom right space''')

#the nex code is a dictionary of the board and list of possible moves
moves = ['top-L','top-M','top-R','mid-L','mid-M','mid-R','low-L','low-M','low-R']

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

num_move = 0
while num_move < 2:
    #this while loop continues for 2 moves
    validMOVE1 = 0
    validMOVE2 = 0
    while validMOVE1 == 0:
        PlayerOneMove = input()
        validMOVE1= checkPlayerOneMove(PlayerOneMove)
    print_board(board)


    while validMOVE2 == 0:
        PlayerTwoMove = input()
        validMOVE2 = checkPlayerTwoMove(PlayerTwoMove)
    print_board(board)

    num_move = num_move + 1
while num_move < 4:
    validMOVE1 = 0
    validMOVE2 = 0
    winner1 = 0
    winner2=0
    #this while loop checks if someone has won up to 4 moves
    while validMOVE1 == 0:
        PlayerOneMove = input()
        validMOVE1= checkPlayerOneMove(PlayerOneMove)
    print_board(board)
    winner1 = check_winner(board)
    if winner1 ==1 :
        break

    while validMOVE2 == 0:
        PlayerTwoMove = input()
        validMOVE2 = checkPlayerTwoMove(PlayerTwoMove)
    print_board(board)
    num_move = num_move + 1
    winner2 = check_winner(board)
    if winner2 == 1:
        break
    print(num_move)
validMOVE1 = 0
while validMOVE1 == 0:
        PlayerOneMove = input()
        validMOVE1= checkPlayerOneMove(PlayerOneMove)
        print_board(board)
        winner1 = check_winner(board)
        if winner1 ==1 :
            break
if (winner1 != 1) and (winner2 != 1):
    print('Stalemate')
