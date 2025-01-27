prime_numbers = [2, 3, 5, 7, 11, 13, 17]
perfect_squares = (1, 4, 9, 16, 25, 36, 49)

# Empty Tuple
empty_tuple = ()
# Single Element (note the comma)
single_tuple = (1)
print(type(single_tuple))
single_tuple = (1,)
print(type(single_tuple))
single_tuple = 1,
print(type(single_tuple))
single_tuple = ("a",)

# Multiple elements
mixed_tuple = (1, 'hello', True)
# Tuple packing
implicit_packing = 1,2,3

# Tuple Modification
my_tuple = (1,2,3)
# my_tuple[0] = 0 # TypeError
# my_tuple.append(4) # AttributeError
#Adding an element to tuple
# my_tuple += 4 # can not concatenate int to tuple
my_tuple += 4,
print(my_tuple)
my_tuple += (5,6,7,8,9)
print(my_tuple)

# Iterating over a list
for p in prime_numbers:
    print(f"Prime:{p}")
# Iterating over a Tuple
for n in perfect_squares:
    print(f"Squares:{n}")
    
# Display the length
print(f"Primes = {len(prime_numbers)}")
print(f"Squares = {len(perfect_squares)}")

# List methods
print(dir(prime_numbers))
print(len(dir(prime_numbers)))
# Tuple methods
print(dir(perfect_squares))
print(len(dir(perfect_squares)))

import sys
# utilize sys.getsizeof() to get the memory
prime_list = [2, 3, 5, 7, 11, 13, 17]
prime_tuple = (2, 3, 5, 7, 11, 13, 17)
print(f"List Size: {sys.getsizeof(prime_list)}")
print(f"Tuple Size: {sys.getsizeof(prime_tuple)}")

import timeit
list_test = timeit.timeit(stmt = "[1,2,3,4,5]", number = 1000000)
tuple_test = timeit.timeit(stmt = "(1,2,3,4,5)", number = 1000000)

print(f"List Time: {list_test}")
print(f"Tuple Time: {tuple_test}")

# Methods
# count() - counts occurences of an element
tuple2 = (1,2,3,4,5,2,2,5,6,45,4)
count = tuple2.count(2)
print(count)
# index() - find position of an element
# position = tuple2.index(29) valueError
position = tuple2.index(2) 
print(position) #first occurrence