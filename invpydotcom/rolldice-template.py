# Import the random module for its randint() function.
____ random

def rollDice(numberOfDice):
    # Start the sum total at 0:
    total = ____
    # Run a loop for each die that needs to be rolled:
    for i in range(____):
        # Add the amount from one 6-sided dice roll to the total:
        total += random.randint(____, ____)
    # Return the dice roll total:
    return total
