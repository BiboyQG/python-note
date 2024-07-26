# Description: Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes.

class A:
    def say(self):
        print("A")

class B:
    def say(self):
        print("B")

class C(A):
    pass

class D(C, B):
    pass

class M(D):
    pass

# Here, due to local precedence ordering, the method of class C is called first.

m = M()
m.say() # Output: A
# The MRO of a class can be accessed using the mro() method or __mro__ attribute.
# print(M.__mro__)
print(M.mro()) # Output: [<class '__main__.M'>, <class '__main__.A'>, <class 'object'>]

# MRO is calculated using C3 linearization algorithm. The algorithm is described in the following link:
# https://en.wikipedia.org/wiki/C3_linearization