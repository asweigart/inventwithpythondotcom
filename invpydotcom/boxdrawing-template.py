def drawBox(size):
    # Special case: Draw nothing if size is less than 1:
    if size < ____:
        return

    # Draw back line on top surface:
    print(' ' * (____ + 1) + '+' + '-' * (____ * 2) + '+')

    # Draw top surface:
    for i in range(____):
        print(' ' * (____ - i) + '/' + ' ' * (____ * 2) + '/' + ' ' * i + '|')

    # Draw top line on top surface:
    print(____ + ____ * (size * 2) + ____ + ' ' * size + '+')

    # Draw front surface:
    for i in range(size - 1, ____, ____):
        print(____ + ' ' * (size * ____) + ____ + ' ' * i + ____)

    # Draw bottom lie on front surface:
    print(____ + ____ * (size * 2) + ____)

# In a loop, call drawBox() with arguments 1 to 5:
for i in range(1, 6):
    drawBox(i)
