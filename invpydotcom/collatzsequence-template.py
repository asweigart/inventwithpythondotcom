def collatz(startingNumber):
    # If the starting number is 0 or negative, return an empty list:
    if ____ < 1:
        return ____

    # Create a list to hold the sequence, beginning with the starting number:
    sequence = [____]
    num = ____
    # Keep looping until the current number is 1:
    while num ____ 1:
        # If odd, the next number is 3 times the current number plus 1:
        if num % 2 == ____:
            num = 3 * num + 1
        # If even, the next number is half the current number:
        else:
            num = num // ____
        # Record the number in the sequence list:
        sequence.append(____)

    # Return the sequence of numbers:
    return ____
