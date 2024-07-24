# Description: This script demonstrates the usage and implementation of decorator in Python

import time

# Implementation of decorator

def dec(f):
    pass

@dec
def double(x):
    return x * 2

# which is equivalent to:

double = dec(double)

# Practical example of decorator

def timeit(f):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result

    return wrapper

@timeit
def double(x):
    time.sleep(0.5)
    return x * 2

print(double(2)) # Output: 4

# Decorator with arguments

def timeit(repeat=1):

    def innerDec(f):

        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(repeat):
                start = time.time()
                result = f(*args, **kwargs)
                end = time.time()
                total_time += end - start
            print(f"Average execution time: {total_time / repeat} seconds")
            return result

        return wrapper

    return innerDec

@timeit(repeat=3)
def double(x):
    time.sleep(0.5)
    return x * 2

print(double(2)) # Output: 4