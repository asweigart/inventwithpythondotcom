def mode(numbers):
    # Special case: If the numbers list is empty, return None:
    if len(numbers) == ____:
        return ____

    # Dictionary with keys of numbers and values of how often they appear:
    numberCount = {}

    # Track the most frequent number and how often it appears:
    mostFreqNumber = None
    mostFreqNumberCount = ____

    # Loop through all the numbers, counting how often they appear:
    for number in ____:
        # If the number hasn't appeared before, set it's count to 0.
        if ____ not in numberCount:
            numberCount[____] = ____
        # Increment the number's count:
        numberCount[____] += ____
        # If this is more frequent than the most frequent number, it
        # becomes the new most frequent number:
        if numberCount[number] > ____:
            mostFreqNumber = ____
            mostFreqNumberCount = ____[____]
    # The function returns the most frequent number:
    return mostFreqNumber
