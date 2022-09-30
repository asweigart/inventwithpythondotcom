def convertStrToInt(stringNum):
    # This dictionary maps string digits to single integer digits:
    DIGITS_STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    # Make a note whether the number is negative or not, and make
    # integerNum positive for the rest of the function's code:
    if stringNum[0] == '-':
        isNegative = True
        stringNum = stringNum[1:]  # Remove the negative sign.
    else:
        isNegative = False

    # integerNum holds the converted integer, and starts off at 0:
    integerNum = 0

    # Loop over the digits in the string from left to right:
    for i in range(len(stringNum)):
        # Get the integer digit from the string digit:
        digit = DIGITS_STR_TO_INT[stringNum[i]]
        # Add this to the integer number:
        integerNum = (integerNum * 10) + digit

    # If the number was originally negative, make the integer
    # negative before returning it:
    if isNegative:
        return -integerNum
    else:
        return integerNum
