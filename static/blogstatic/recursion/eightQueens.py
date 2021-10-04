SIZE = 8

def getPermutations(items):
    if len(items) == 0:
        # BASE CASE
        return [[]]
    else:
        # RECURSIVE CASE
        permutations = []
        head = [items[0]]
        tail = items[1:]
        tailPermutations = getPermutations(tail)
        for tailPerm in tailPermutations:
            for i in range(len(tailPerm) + 1):
                newPermutation = tailPerm[0:i] + head + tailPerm[i:]
                permutations.append(newPermutation)
        return permutations

def printBoard(board):
    for row in range(SIZE):
        for column in range(SIZE):
            if board[row] == column:
                print('Q ', end='')  # Print queen.
            else:
                print('. ', end='')  # Print blank space.
        print()  # Print newline.
    print()

numSolutions = 0
# Go through all possible boards with one queen per column, and
# filter out the ones with queens that can attack each other diagonally:
for board in getPermutations(list(range(SIZE))):
    # check if any queens can diagonally attack each other
    isValidBoard = True
    for row in range(SIZE):
        column = board[row]
        for diagOffset in range(1, SIZE):
            if row + diagOffset < SIZE:  # Bounds check.
                if (board[row + diagOffset] == column + diagOffset) or \
                   (board[row + diagOffset] == column - diagOffset):
                    isValidBoard = False
                    break

            if row - diagOffset >= 0:  # Bounds check.
                if (board[row - diagOffset] == column - diagOffset) or \
                   (board[row - diagOffset] == column + diagOffset):
                    isValidBoard = False
                    break

    if isValidBoard:
        printBoard(board)
        numSolutions += 1
print('Number of solutions:', numSolutions)
