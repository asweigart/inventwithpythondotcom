### A regular function:
def aRegularFunction(param):
    print('Hello', param)
    return 42

print("Calling aRegularFunction('Alice'):")
returnedValue = aRegularFunction('Alice')
print('Returned value:', returnedValue)



### A generator (aka generator function):
def aGeneratorFunction(param):
    print('Hello', param)
    yield 42
    print('How are you,', param)
    yield 99
    print('Goodbye', param)
    return 86  # Raises StopIteration with value 86.

print("Calling aGeneratorFunction('Bob'):")
generatorObj = aGeneratorFunction('Bob')
print('Calling next():')
yieldedValue = next(generatorObj)
print('Yielded value:', yieldedValue)
print('Calling next():')
yieldedValue = next(generatorObj)
print('Yielded value:', yieldedValue)
print('Calling next():')
try:
    next(generatorObj)
except StopIteration as excObj:
    print('type(excObj) is', type(excObj))
    print('excObj.value is', excObj.value)
    print('type(excObj.value) is', type(excObj.value))



### Using a generator function with a for loop or list() call:
for yieldedValue in aGeneratorFunction('Carol'):
    print('Yielded value:', yieldedValue)

listOfGeneratedValues = list(aGeneratorFunction('David'))
print('List of generated values:', listOfGeneratedValues)



### A practical example of a generator using the Fibonacci sequence:
def fibonacciSequence(maxNum=50):
    a = 0
    b = 1
    yield a
    yield b
    while True:
        a, b = b, b + a
        if b >= maxNum:
            return b  # Raise StopIteration.
        else:
            yield b


for fibNum in fibonacciSequence():
    print('Next number in the Fibonacci sequence:', fibNum)


fibNumsUpTo500 = list(fibonacciSequence(500))
print('List of fib numbers up to 500:', fibNumsUpTo500)



### Using generator functions to re-implement range():
def mySimpleImplementationOfRange(stop):
    i = 0
    while i < stop:
        yield i
        i += 1
    return  # Raise StopIteration.

for i in mySimpleImplementationOfRange(5):
    print(i)



### Using generator functions for a more complete range() re-implementation:
def myImplementationOfRange(firstParam, secondParam=None, thirdParam=None):
    if secondParam is None:
        if not isinstance(firstParam, int):
            raise TypeError("'" + firstParam.__class__.__name__ + "' object cannot be interpreted as an integer")
        start = 0
        stop = firstParam
        step = 1
    elif thirdParam is None:
        if not isinstance(secondParam, int):
            raise TypeError("'" + secondParam.__class__.__name__ + "' object cannot be interpreted as an integer")
        start = firstParam
        stop = secondParam
        step = 1
    else:
        if not isinstance(thirdParam, int):
            raise TypeError("'" + thirdParam.__class__.__name__ + "' object cannot be interpreted as an integer")
        if thirdParam == 0:
            raise ValueError('myImplementationOfRange() arg 3 must not be zero')
        start = firstParam
        stop = secondParam
        step = thirdParam

    i = start
    if step > 0:  # step arg is increasing
        while i < stop:
            yield i
            i += step
        return i
    elif step < 0:  # step arg is decreasing
        while i > stop:
            yield i
            i += step  # Adding a negative to decrease
        return i

for i in myImplementationOfRange(4, 12, 2):
    print(i)
