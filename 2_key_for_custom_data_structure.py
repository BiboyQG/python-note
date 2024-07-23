# Description: This script demonstrates the correct way to use custom data structure as the key for dictionary

# Correct way to use custom data structure as the key for dictionary
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        # Use hash function to generate hash value for the tuple (self.x, self.y)
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Position({self.x}, {self.y})"
    
d = {}
pos = Position(0, 1)
d[pos] = 1
pos2 = Position(0, 1)
d[pos2] = 2
print(d) # Output: {Position(0, 1): 2}