# Part 1: List Basics
# 1.1 List Creation

# Different ways to create lists
fruits = ['apple', 'banana', 'cherry']
numbers = list(range(1, 6))  # Creates [1, 2, 3, 4, 5]
mixed_list = [1, 'hello', 3.14, True]
# Empty list initialization
empty_list = []
another_empty_list = list()

# 1.2 Accessing List Elements
# Indexing
print(fruits[0])  # First element
print(fruits[-1])  # Last element
# Slicing
print(fruits[1:3])  # Subset of list
print(fruits[:2])   # First two elements
print(fruits[1:])   # From second element to end

