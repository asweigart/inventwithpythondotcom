import timeit
from sys import getsizeof, stderr
from itertools import chain
from collections import deque

# These constants are the size of the grid used in the tests:
WIDTH = 150
HEIGHT = 50

# Function to determine memory usage from https://code.activestate.com/recipes/577504-compute-memory-footprint-of-an-object-and-its-cont/?in=user-178123
def memoryUsage(o, handlers={}, verbose=False):
    dict_handler = lambda d: chain.from_iterable(d.items())
    all_handlers = {tuple: iter,
                    list: iter,
                    deque: iter,
                    dict: dict_handler,
                    set: iter,
                    frozenset: iter,
                   }
    all_handlers.update(handlers)     # user handlers take precedence
    seen = set()                      # track which object id's have already been seen
    default_size = getsizeof(0)       # estimate sizeof object without __sizeof__

    def sizeof(o):
        if id(o) in seen:       # do not double count the same object
            return 0
        seen.add(id(o))
        s = getsizeof(o, default_size)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)


def createAndFillDict():
    # Create a 2D grid from scratch using a dictionary and completely fill it with data.
    dictGrid = {}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            dictGrid[(x, y)] = 'A'
    return dictGrid


def createAndFillDictComp():
    # Create a 2D grid from scratch using a dictionary comprehension and completely fill it with data.
    return {(x, y): 'A' for x in range(WIDTH) for y in range(HEIGHT)}


def createAndFill1DList():
    # Create a 2D grid from scratch using a list and completely fill it with data.
    list1DGrid = []
    for i in range(WIDTH * HEIGHT):
        list1DGrid.append('A')
    return list1DGrid


def createAndFill1DListComp():
    # Create a 2D grid from scratch using a list comprehension and completely fill it with data.
    return ['A' for i in range(WIDTH * HEIGHT)]


def createAndFill2DList():
    # Create a 2D grid from scratch using a list of lists and completely fill it with data.
    list2DGrid = []
    for x in range(WIDTH):
        list2DGrid.append([])
        for y in range(HEIGHT):
            list2DGrid[-1].append('A')
    return list2DGrid


def createAndFill2DListComp():
    # Create a 2D grid from scratch using a list comprehension of list comprehensions and completely fill it with data.
    list2DGrid = [['A' for y in range(HEIGHT)] for x in range(WIDTH)]
    return list2DGrid


def read1DList(grid):
    # Read every coordinate in the list 2D grid.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            data = grid[y * WIDTH + x]


def read2DList(grid):
    # Read every coordinate in the list of lists 2D grid.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            data = grid[x][y]


def readDict(grid):
    # Read every coordinate in the dictionary 2D grid.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            data = grid[x, y]


def write1DList(grid):
    # Write to every coordinate in the list 2D grid.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            grid[y * WIDTH + x] = 'A'


def write2DList(grid):
    # Write to every coordinate in the list to lists 2D grid.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            grid[x][y] = 'A'


def writeDict(grid):
    # Write to every coordinate in the dictionary 2D grid.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            grid[x, y] = 'A'


print('Compare the 1D list and 1D list comprehension creations:')
print(timeit.timeit('createAndFill1DList()', number=10000, globals=globals()))      # 5.796480499964673
print(timeit.timeit('createAndFill1DListComp()', number=10000, globals=globals()))  # 3.3725536999991164
# Conclusion: Using list comprehensions to create the list is faster than a for loop.

print('Compare the 2D list and 2D list comprehension creations:')
print(timeit.timeit('createAndFill2DList()', number=10000, globals=globals()))      # 7.913099199999124
print(timeit.timeit('createAndFill2DListComp()', number=10000, globals=globals()))  # 3.83729699999094
# Conclusion: Using list comprehensions to creat the 2D list is faster than nested for loops.

print('Compare the dictionary and dictionary comprehension creations:')
print(timeit.timeit('createAndFillDict()', number=10000, globals=globals()))      # 9.804479899990838
print(timeit.timeit('createAndFillDictComp()', number=10000, globals=globals()))  # 10.132151499972679
# Conclusion: With repeated trials, there isn't a significant difference.

print('Compare the 1D list, 2D list, and dictionary creations:')
print(timeit.timeit('createAndFill1DListComp()', number=10000, globals=globals()))  # 3.2536532999947667
print(timeit.timeit('createAndFill2DListComp()', number=10000, globals=globals()))  # 3.1561911000171676
print(timeit.timeit('createAndFillDict()', number=10000, globals=globals()))        # 9.759650700027123
# Conclusion: The dictionary is slowest to create, and the 1D and 2D lists are about the same.

print('Compare the memory usage of a full grid of each of the three approaches:')
print(memoryUsage(createAndFill1DListComp()))  # 67274
print(memoryUsage(createAndFill2DListComp()))  # 72282
print(memoryUsage(createAndFillDict()))        # 719246
# Conclusion: The 1D and 2D list use about the same amount, the 1D list less so. The dictionary uses 10x the memory though.

print('Compare the speed of reading grid data:')
list1dGrid = createAndFill1DListComp()
list2dGrid = createAndFill2DListComp()
dictGrid = createAndFillDict()
print(timeit.timeit('read1DList(list1dGrid)', number=10000, globals=globals()))  # 8.444686400005594
print(timeit.timeit('read2DList(list2dGrid)', number=10000, globals=globals()))  # 3.76759669999592
print(timeit.timeit('readDict(dictGrid)', number=10000, globals=globals()))        # 7.19706789997872
# Conclusion: The 2D list is twice as fast as the others at reading data. The 1D list is slower than the dictionary.

print('Compare the speed of writing grid data:')
print(timeit.timeit('write1DList(list1dGrid)', number=10000, globals=globals()))  # 8.487390499969479
print(timeit.timeit('write2DList(list2dGrid)', number=10000, globals=globals()))  # 4.278829399961978
print(timeit.timeit('writeDict(dictGrid)', number=10000, globals=globals()))        # 7.716881500033196
# Conclusion: As with the read test, the 2D list is twice as fast as the others. The 1D list is slower than the dictionary.
