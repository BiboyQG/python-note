# Description: This script demonstrates the tips when using conditioned generator comprehensions in Python

# Snippet: Conditioned generator comprehensions

lst = [1, 2, 3, 4, 5]
g = (n for n in lst if n in lst)
lst = [0, 1, 2]
print(list(g)) # Output: [1, 2]

# This is equivalent to:

lst1 = [1, 2, 3, 4, 5]
g = (n for n in lst1 if n in lst2)
lst2 = [0, 1, 2]
print(list(g)) # Output: [1, 2]

# Conclusion: The generator comprehension is evaluated lazily. The condition is evaluated when the generator is consumed.
