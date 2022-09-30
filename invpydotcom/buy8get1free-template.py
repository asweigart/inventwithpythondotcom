def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    # Track the total price:
    totalPrice = ____
    # Track how many coffees we have until we get a free one:
    cupsUntilFreeCoffee = 8

    # Loop until the number of coffees to buy reaches 0:
    while numberOfCoffees ____ 0:
        # Decrement the number of coffees left to buy:
        ____ -= 1

        # If this cup of coffee is free, reset the number to buy until
        # a free cup back to 8:
        if cupsUntilFreeCoffee == ____:
            ____ = 8
        # Otherwise, pay for a cup of coffee:
        else:
            # Increase the total price:
            totalPrice += ____
            # Decrement the coffees left until we get a free coffee:
            cupsUntilFreeCoffee -= ____

    # Return the total price:
    return ____
