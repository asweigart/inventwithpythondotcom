def mergeTwoLists(list1, list2):
    # Create an empty list to hold the final sorted results:
    result = ____

    # Start i1 and i2 at index 0, the start of list1 and list2:
    i1 = ____
    i2 = ____

    # Keeping moving up i1 and i2 until one reaches the end of its list:
    while i1 < len(____) and ____ < len(list2):
        # Add the smaller of the two current items to the result:
        if list1[____] < list2[____]:
            # Add list1's current item to the result:
            result.append(____[i1])
            # Increment i1:
            i1 += ____
        else:
            # Add list2's current item to the result:
            result.append(____[i2])
            # Increment i2:
            i2 += ____

    # If i1 is not at the end of list1, add the remaining items from list1:
    if i1 < len(____):
        for j in range(i1, len(list1)):
            result.append(____[j])
    # If i2 is not at the end of list2, add the remaining items from list2:
    if i2 < len(____):
        for j in range(i2, len(list2)):
            result.append(____[j])

    # Return the merged, sorted list:
    return result
