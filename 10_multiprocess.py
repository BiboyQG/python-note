# Description: This script demonstrates the usage and implementation of multiprocessing in Python

import multiprocessing
import os

print(os.cpu_count()) # Output: 10, this is the number of logical cores
print(os.getpid()) # Output: this is the process ID

def f():
    print('Process PID:', os.getpid())

# Create a process
p = multiprocessing.Process(target=f)
p.start()
p.join()

# Create a process pool
pool = multiprocessing.Pool()
pool.map(f, range(10))
pool.close()
pool.join()

# Create a process class:
class MyProcess(multiprocessing.Process):
    def run(self):
        f()

p = MyProcess()
p.start()
p.join()