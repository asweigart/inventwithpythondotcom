def rot13(text):
    # Create an encryptedText variable to store the encrypted string:
    encryptedText = ____
    # Loop over each character in the text:
    for character in text:
        # If the character is not a letter, add it as-is to encryptedText:
        if not character.____():
            encryptedText += ____
        # Otherwise calculate the letter's "rotated 13" letter:
        else:
            rotatedLetterOrdinal = ____(character) + 13
            # If adding 13 pushes the letter past Z, subtract 26:
            if ____.islower() and rotatedLetterOrdinal > ____:
                rotatedLetterOrdinal -= ____
            if ____.isupper() and rotatedLetterOrdinal > ____:
                rotatedLetterOrdinal -= ____

            # Add the encrypted letter to encryptedText:
            encryptedText += ____(rotatedLetterOrdinal)

    # Return the encrypted text:
    return encryptedText
