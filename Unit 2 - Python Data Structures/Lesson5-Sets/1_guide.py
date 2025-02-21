# 1. CREATING SETS
# Different ways to create sets in Python
# ---------------------------------------

#1 Create an empty set
# Note: {} creates an empty dictionary, not a set
empty_set = set()
#2 Create a set with initial values
numbers = {5,1,2,3,4,5,5}
numbers = {"7",5,2,3,3,5,5,4,"8"}
print(numbers)

#3 Create a set from a string
letters = set("bergen tech")
print(letters)

# Create a set from a list
numbers_from_list = [1,2,3,4,4,5,2,1]
print(set(numbers_from_list))

# 2. BASIC SET OPERATIONS
# Adding and removing elements
# ---------------------------------------

# Initialize a set of fruits
fruits = {'apple', 'banana', 'orange'}
# Add a single element using add()
fruits.add("grapes")
fruits.add(('watermelon', 'melon'))
# Add multiple elements using update()
# fruits.update(['mango', 'kiwi'])
fruits.update(('mango', 'kiwi'))
print(fruits)


# Remove all elements using clear()
numbers.clear()
print(numbers)
# Remove an element using remove()
# Note: Raises KeyError if element doesn't exist
fruits.remove('mango')
print(fruits)
# fruits.remove('mango') # KeyError
# print(fruits)

# Remove an element using discard()
# Note: No error if element doesn't exist
fruits.discard('mango') # No error
print(fruits)
fruits.discard('apple') # apple removed
print(fruits)

# Remove and return an arbitrary element using pop()
print(fruits.pop())

# 3. SET COMPREHENSION
# Create sets using comprehension
# ---------------------------------------
# Create a set of squares from 0 to 9
squares = {x**2 for x in range(10)}
# Create a set of even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = {x for x in numbers if x % 2 == 0}

# 4. PRACTICAL APPLICATIONS
# Common use cases for sets
# ---------------------------------------

# Remove duplicates from a list
duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(duplicates))
print(unique)  # [1, 2, 3, 4]

# Find unique characters in a string
text = "mississippi"
unique_chars = set(text)
print(unique_chars)  # {'m', 'i', 's', 'p'}
