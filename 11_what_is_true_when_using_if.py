# Description: This script demonstrates the usage of if statement in Python

a = True

if a is True:
    print('a is True')

# Not so common now when using custom objects
if a == True:
    print('a == True')

# Pass when using built-in objects and length/value is not zero
# When using custom objects, __len__ and __bool__ methods need to be defined:
if a:
    print('a')

# This is equivalent to:

if bool(a):
    print('bool(a)')
