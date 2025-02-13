# ---------------------------------------------------------------
# PYTHON DICTIONARY METHODS
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# 1. CREATION AND INITIALIZATION
# ---------------------------------------------------------------

# Creating a dictionary using literal syntax
my_dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}

# Creating a dictionary using dict() constructor
my_dict2 = dict(name='John', age=30, city='New York')

# Creating a dictionary from a list of tuples
items = [('name', 'John'), ('age', 30), ('city', 'New York')]
my_dict3 = dict(items)

# Creating a dictionary with dict.fromkeys(seq, value)
# Creates a new dictionary with keys from seq and values set to value
keys = ['name', 'age', 'city']
my_dict4 = dict.fromkeys(keys, 'unknown')
# Result: {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

# ---------------------------------------------------------------
# 2. ACCESS AND RETRIEVAL
# ---------------------------------------------------------------

# get(key[, default])
# Returns the value for key if key is in the dictionary, else default
name = my_dict1.get('name', 'Not Found')  # Returns 'John'
country = my_dict1.get('country', 'Not Found')  # Returns 'Not Found'

# [key]
# Direct access using square brackets (raises KeyError if key doesn't exist)
age = my_dict1['age']  # Returns 30
# age = my_dict1['country']  # Would raise KeyError

# keys()
# Returns a view object that displays all the keys
all_keys = my_dict1.keys()  # dict_keys(['name', 'age', 'city'])

# values()
# Returns a view object that displays all the values
all_values = my_dict1.values()  # dict_values(['John', 30, 'New York'])

# items()
# Returns a view object that displays all key-value pairs as tuples
all_items = my_dict1.items()  # dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# ---------------------------------------------------------------
# 3. MODIFICATION AND UPDATING
# ---------------------------------------------------------------

# update([other])
# Updates the dictionary with the key/value pairs from other
my_dict1.update({'country': 'USA', 'age': 31})
# Result: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

# setdefault(key[, default])
# If key is in the dictionary, return its value.
# If not, insert key with a value of default and return default
email = my_dict1.setdefault('email', 'john@example.com')
# Result: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA', 'email': 'john@example.com'}

# ---------------------------------------------------------------
# 4. REMOVAL AND CLEARING
# ---------------------------------------------------------------

# clear()
# Remove all items from the dictionary
temp_dict = {'a': 1, 'b': 2}
temp_dict.clear()  # Result: {}

# del statement
# Remove specific key or the entire dictionary
del my_dict2['name']  # Removes the 'name' key-value pair
# del my_dict2  # Would delete the entire dictionary

# pop(key[, default])
# Remove specified key and return the corresponding value
# If key is not found, return default if given, otherwise raise KeyError
city = my_dict1.pop("city") # Returns "New York", removes key-value pair
print(my_dict1) # 'city': 'New York' will be removed from the dictionary

# popitem()
# Remove and return the last key-value pair as a tuple
# Raises KeyError if dictionary is empty (in Python 3.7+, removes a random item)
last_item = my_dict1.popitem() #
print(last_item) 



# ---------------------------------------------------------------
# 4. UTILITY METHODS
# ---------------------------------------------------------------

# copy()
# Returns a shallow copy of the dictionary
dict_copy = my_dict3.copy()

# len(d)
# Returns the number of key-value pairs in dictionary d
num_items = len(my_dict4)  # Returns the number of items in the dictionary

# in operator
# Returns True if key is in the dictionary, else False
has_name = 'name' in my_dict1  # Returns True if 'name' is a key in my_dict1

# ---------------------------------------------------------------
# 6. DICTIONARY COMPREHENSIONS (Not a method, but a related feature)
# ---------------------------------------------------------------

# Dictionary comprehension
# Create dictionaries using a compact syntax
squares = {x: x*x for x in range(6)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary comprehension with condition
even_squares = {x: x*x for x in range(6) if x % 2 == 0}
# Result: {0: 0, 2: 4, 4: 16}