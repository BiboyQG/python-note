# Description: Four main ways to exit from the program

import sys
import os

try:
    raise SystemExit
    quit()
    exit()
    sys.exit()
    os._exit()
except SystemExit:
    print("SystemExit exception is caught!")

print("Yeah!")

# This is the most common way to exit from the program, really similar to exit() function in the second way
# 1. quit()

# This is the most common way to exit from the program, really similar to quit() function in the first way. 
# But they are both included in the site module which is included by default in Python. 
# If you run these two functions using -S option, you will get an error, since -S option disables the site module. 
# Therefore, it is recommended to use these two functions in interactive mode. 
# In almost all formal scripts, you should use sys.exit() instead.
# 2. exit()

# This is the most formal way to exit from the program, really similar to exit() and quit() functions in the first and second ways. They all raise SystemExit exception, which can be caught by try-except block. The exit status is 0 by default. 1 is used to indicate that the program terminated abnormally.
# 3. sys.exit(0)

# This is the most brutal way to exit from the program (do systemcall to shutdown kernal), it will not execute the finally block, thus it is not recommended to use this function in the main process. The 0 argument is the exit status. 1 is used to indicate that the program terminated abnormally.
# 4. os._exit(0)

# You can also use shortcuts to exit from the program, such as Ctrl+C, Ctrl+D under Windows, Ctrl+Z under unix system(Linux, MacOS, etc.), or Ctrl+\ under unix system.