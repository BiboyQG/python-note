# Description: This script demonstrates the correct way to use default argument for class

# Incorrect way to use default argument for class
class Player:
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items

p1 = Player("Alice")
p2 = Player("Bob")
p3 = Player("Charles", ["sword"])

p1.items.append("armor")
p2.items.append("sword")

print(f"Player {p1.name} has items {p1.items}")

# Correct way to use default argument for class
class Player:
    def __init__(self, name, items=None):
        self.name = name
        if items is None:
            self.items = []
        else:
            self.items = items

p1 = Player("Alice")
p2 = Player("Bob")
p3 = Player("Charles", ["sword"])

p1.items.append("armor")
p2.items.append("sword")

print(f"Player {p1.name} has items {p1.items}")