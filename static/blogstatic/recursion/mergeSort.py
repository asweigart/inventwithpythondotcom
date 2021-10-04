import math

def mergeSort(items):
    print('.....mergeSort() called on:', items)

    if len(items) == 0 or len(items) == 1:  # BASE CASE
        # With only zero or one items, `items` is already sorted.
        return items

    # RECURSIVE CASE
    # Round down if `items` doesn't divide in half evenly:
    iMiddle = math.floor(len(items) / 2)

    print('................Split into:', items[:iMiddle], 'and', items[iMiddle:])

    left = mergeSort(items[:iMiddle])
    right = mergeSort(items[iMiddle:])

    # At this point, `left` should be sorted and `right` should be
    # sorted. We can merge them into a single sorted list like a zipper.
    sortedResult = []
    iLeft = 0
    iRight = 0
    while (len(sortedResult) < len(items)):
        # Append the smaller of left & right's value to `sortedResult`.
        if left[iLeft] < right[iRight]:
            sortedResult.append(left[iLeft])
            iLeft += 1
        else:
            sortedResult.append(right[iRight])
            iRight += 1

        # If one of the pointers has reached the end of its list,
        # put the rest of the other list into `sortedResult`.
        if iLeft == len(left):
            sortedResult.extend(right[iRight:])
            break
        elif iRight == len(right):
            sortedResult.extend(left[iLeft:])
            break

    print('The two halves merged into:', sortedResult)

    return sortedResult  # Returns a sorted version of `items`.

myList = [0, 7, 6, 3, 1, 2, 5, 4]
myList = mergeSort(myList)
print(myList)