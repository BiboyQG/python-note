# Description: This file demonstrates how to create an iterable and iterator class in Python

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

# In case someone does this:

# it = iter(node1)
# first = next(it)

# for node in it:
#     print(node.name)

# We also need to implement __iter__ in NodeIter class:

class NodeIter:
    def __init__(self, node):
        self.curr_node = node

    def __next__(self):
        if self.curr_node is None:
            raise StopIteration
        node, self.curr_node = self.curr_node, self.curr_node.next
        return node

    def __iter__(self):
        return self
    
# Now, the above code will work as expected.

it = iter(node1)
first = next(it)

for node in it:
    print(node.name)