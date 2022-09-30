def drawBorder(width, height):
    # Special case: If the width or height is less than two, draw nothing:
    if width < ____ or height < ____:
        return

    # Print the top row:
    print('+' + ('-' * (width - ____)) + ____)

    # Loop for each row (except the top and bottom):
    for i in range(height - 2):
        # Print the sides:
        print(____ + (____ * (width - 2)) + ____)

    # Print the bottom row:
    print(___________________________________)
