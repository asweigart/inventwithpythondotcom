def printHandshakes(people):
    # The total number of handshakes starts at 0:
    numberOfHandshakes = ____
    # Loop over every index in the people list except the last:
    for i in range(0, len(____) - 1):
        # Loop over every index in the people list after index i:
        for j in range(i + ____, len(____)):
            # Print a handshake between the people at index i and j:
            print(people[____], 'shakes hands with', people[____])
            # Increment the total number of handshakes:
            numberOfHandshakes += ____
    # Return the total number of handshakes:
    return numberOfHandshakes
