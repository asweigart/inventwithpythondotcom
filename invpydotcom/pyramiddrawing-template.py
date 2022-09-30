def drawPyramid(height):
    # Loop over each row from 0 up to height:
    for rowNumber in range(____):
        # Create a string of spaces for the left side of the pyramid:
        leftSideSpaces = ' ' * (____ - (rowNumber + ____))
        # Create the string of hashtags for this row of the pyramid:
        pyramidRow = '#' * (____ * 2 + ____)
        # Print the left side spaces and the row of the pyramid:
        ____(leftSideSpaces + pyramidRow)
