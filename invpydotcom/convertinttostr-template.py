def convertIntToStr(integerNum):
    # Special case: Check if integerNum is 0, and return '0' if so:
    if integerNum == ____:
        return ____

    # This dictionary maps single integer digits to string digits:
    DIGITS_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
        5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    # Make a note whether the number is negative or not, and make
    # integerNum positive for the rest of the function's code:
    if integerNum < ____:
        isNegative = ____
        integerNum = ____
    else:
        isNegative = ____

    # stringNum holds the converted string, and starts off blank:
    stringNum = ____

    # Keeping looping while integerNum is greater than zero:
    while integerNum ____ 0:
        # Mod the integerNum by 10 to get the digit in the ones place:
        onesPlaceDigit = integerNum % ____
        # Put the corresponding string digit at the front of stringNum:
        stringNum = DIGITS_INT_TO_STR[onesPlaceDigit] + ____
        # Divide integerNum by ten to remove one entire digit place:
        integerNum //= ____

    # If the number was originally negative, add a minus sign:
    if isNegative:
        return ____ + stringNum
    else:
        return ____
