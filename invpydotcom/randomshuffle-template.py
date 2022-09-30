# Import the random module for its randint() function.
import random

def shuffle(values):
    # Loop over the range of indexes from 0 up to the length of the list:
    for i in range(____(values)):
        # Randomly pick an index to swap with:
        swapIndex = random.randint(0, len(____) - ____)
        # Swap the values between the two indexes:
        values[i], values[swapIndex] = values[____], values[____]
