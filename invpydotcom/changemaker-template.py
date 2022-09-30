def makeChange(amount):
    # Create a dictionary to keep track of how many of each coin:
    change = ____

    # If the amount is enough to add quarters, add them:
    if amount >= ____:
        change['quarters'] = amount // ____
        # Reduce the amount by the value of the quarters added:
        amount = amount % ____
    # If the amount is enough to add dimes, add them:
    if amount >= ____:
        change['dimes'] = ____ // ____
        # Reduce the amount by the value of the dimes added:
        amount = ____ % ____
    # If the amount is enough to add nickels, add them:
    if amount >= ____:
        change['nickels'] = ____ // ____
        # Reduce the amount by the value of the nickels added:
        amount = ____ % ____
    # If the amount is enough to add pennies, add them:
    if amount >= 1:
        change[____] = amount

    return change
