def reverseString(text):
    # Convert the text string into a list of character strings:
    text = ____(text)
    # Loop over the first half of indexes in the list:
    for i in range(len(____) // ____):
        # Swap the values of i and it's mirror index in the second
        # half of the list:
        mirrorIndex = len(text) - ____ - ____
        text[i], text[mirrorIndex] = text[____], text[____]
    # Join the list of strings into a single string and return it:
    return ''.join(text)
