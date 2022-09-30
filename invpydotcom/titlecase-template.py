def getTitleCase(text):
    # Create a titledText variable to store the titlecase text:
    titledText = ____
    # Loop over every index in text:
    for i in range(len(____)):
        # The character at the start of text should be uppercase:
        if i == ____:
            titledText += text[i].____()
        # If the character is a letter and the previous character is
        # not a letter, make it uppercase:
        elif text[____].isalpha() and not text[i - ____].isalpha():
            titledText += text[____].upper()
        # Otherwise, make it lowercase:
        else:
            titledText += text[i].____()
    # Return the titled cased string:
    return titledText
