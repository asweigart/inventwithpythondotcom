# Import the leapyear module for its isLeapYear() function:
____ leapyear

def isValidDate(year, month, day):
    # If month is outside the bounds of 1 to 12, return False:
    if not (1 ____ month ____ 12):
        return ____
    # After this point, you can assume the month is valid.

    # If the year is a leap year and the date is Feb 29th, it is valid:
    if leapyear.isLeapYear(____) and ____ == 2 and ____ == 29:
        return ____
    # After this point, you can assume the year is not a leap year.

    # Check for invalid dates in 31-day months:
    if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= ____ <= 31):
        return ____
    # Check for invalid dates in 30-day months:
    elif ____ in (4, 6, 9, 11) and not (1 <= day <= 30):
        return ____
    # Check for invalid dates in February:
    elif month == ____ and not (1 <= ____ <= 28):
        return ____

    # Date passes all checks and is valid, so return True:
    return ____
