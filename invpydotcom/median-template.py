def median(numbers):
    # Special case: If the numbers list is empty, return None:
    if len(numbers) == ____:
        return ____

    # Sort the numbers list:
    ____.sort()

    # Get the index of the middle number:
    middleIndex = len(____) // ____

    # If the numbers list has an even length, return the average of the
    # middle two numbers:
    if len(numbers) % ____ == 0:
        return (numbers[____] + numbers[middleIndex - ____]) / ____
    # If the numbers list has an odd length, return the middlemost number:
    else:
        return numbers[____]
