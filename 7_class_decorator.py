# Description: Class decorator example

import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start}s")
        return result
    

# Simple way to use the Timer class
@Timer
def add(a, b):
    return a + b

print(add(2, 3)) # Output: 5

# The above code is equivalent to:

add = Timer(add)

print(add(2, 3)) # Output: 5

# Timer class with arguments

class Timer:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{self.prefix}: {end - start}s")
            return result
        return wrapper
    

@Timer("Time taken")
def add(a, b):
    return a + b

print(add(2, 3)) # Output: 5

# The above code is equivalent to:

add = Timer("Time taken")(add)

print(add(2, 3)) # Output: 5

# The above example is more like a decorator class instead of a class decorator. So below we have a class decorator example:

def add_str(cls):
    def __str__(self):
        return str(self.__dict__)
    cls.__str__ = __str__
    return cls

@add_str
class MyObject:
    def __init__(self, a, b):
        self.a = a
        self.b = b

o = MyObject(1, 2)
print(o) # Output: {'a': 1, 'b': 2}

# The above code is equivalent to:

MyObject = add_str(MyObject)

o = MyObject(1, 2)
print(o) # Output: {'a': 1, 'b': 2}