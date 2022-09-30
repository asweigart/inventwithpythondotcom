def bubbleSort(numbers):
    # The outer loop loops i over all but the last number:
    for i in range(len(____) - ____):
        # The inner loop loops j starting at i to the last number:
        for j in range(____, len(____)):
            # If the number at i is greater than the number at j, swap them:
            if numbers[i] ____ numbers[j]:
                numbers[i], numbers[j] = numbers[____], numbers[____]
    # Return the now-sorted list:
    return numbers
