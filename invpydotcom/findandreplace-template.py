def findAndReplace(text, oldText, newText):
    replacedText = ____
    i = ____
    while i < len(____):
        # If index i in text is the start of the oldText pattern, add
        # the replacement text:
        if text[i:i + len(____)] == oldText:
            # Add the replacement text:
            replacedText += ____
            # Increment i by the length of oldText:
            i += len(____)
        # Otherwise, add the characters at text[i] and increment i by 1:
        else:
            replacedText += ____[i]
            i += ____
    return replacedText
