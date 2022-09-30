def commaFormat(number):
    # Convert the number to a string:
    number = str(____)

    # Remember the fractional part and remove it from the number, if any:
    if '.' in ____:
        fractionalPart = number[number.index(____):]
        number = number[:number.index('.')]
    else:
        fractionalPart = ''

    # Create a variable to hold triplets of digits and the
    # comma-formatted string as it is built:
    triplet = ____
    commaNumber = ____

    # Loop over the digits starting on the right side and going left:
    for i in range(len(number) - 1, ____, ____):
        # Add the digits to the triplet variable:
        triplet = ____[i] + ____
        # When the triplet variable has three digits, add it with a
        # comma to the comma-formatted string:
        if ____(triplet) == ____:
            commaNumber = triplet + ',' + ____
            # Reset the triplet variable back to a blank string:
            triplet = ____

    # If the triplet has any digits left over, add it with a comma
    # to the comma-formatted string:
    if triplet != '':
        commaNumber = ____ + ',' + ____

    # Return the comma-formatted string:
    return ____[:____] + fractionalPart
