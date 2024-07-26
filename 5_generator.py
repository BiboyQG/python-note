# Description: This script demonstrates the usage and implementation of generator in Python

# Implementation of generator

# Generator function (when yield is used, it is a generator function, thus the return statement is optional)
def gen(num):
    while num > 0:
        yield num
        num -= 1
    return

# Generator object (when calling a generator function, it returns a generator object)
g = gen(5)

# generator is a special type of iterator, thus we can use next() and iter() on it:
first = next(g)

for i in g:
    print(i)

# Sometimes generator is more concise than iterator

class NodeIter:
    def __init__(self, node):
        self.curr_node = node

    def __next__(self):
        if self.curr_node is None:
            raise StopIteration
        node, self.curr_node = self.curr_node, self.curr_node.next
        return node
    
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self):
        return NodeIter(self)

    def __str__(self):
        return str(self.data)
    

node1 = Node('node1')
node2 = Node('node2')
node3 = Node('node3')
node1.next = node2
node2.next = node3

for node in node1:
    print(node.name)

# This can be simplified using generator:

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self):
        curr_node = self
        while curr_node is not None:
            yield curr_node
            curr_node = curr_node.next

    def __str__(self):
        return str(self.data)
    

node1 = Node('node1')
node2 = Node('node2')
node3 = Node('node3')
node1.next = node2
node2.next = node3

for node in node1:
    print(node.name)


# Use of send() method

def gen(num):
    while num > 0:
        received = yield num
        if received is not None:
            num = received
        num -= 1
    return

g = gen(5)

first = next(g) # which is equivalent to g.send(None)
print(f'first: {first}')

second = g.send(10)
print(f'send: {second}')

for i in g:
    print(i)
