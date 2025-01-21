# Basic Syntax
'''
new_list = [expression for item in iterable]
# Equivalent to
new_list = []
for item in iterable:
    new_list.append(expression)
'''

numbers = [1, 5, 3, 8]
numbers2 = []
for num in numbers:
    # print(num**2)
    # num = num ** 2
    numbers2.append(num**2)
# print(numbers2)
numbers = [num**2 for num in numbers]
print(numbers)

# Basic Syntax with Condition
'''
# single condition
new_list = [expression for item in iterable if condition]
# if-else
new_list = [true-block if(condition) else false-block for item in iterable]
'''

# Numbers divisible by both 2 and 3
divisible = [x for x in range(30)] # [0,1,2...29]
divisible = [x for x in range(30) if x % 2 == 0] # [0,2,4..28]
divisible = [x for x in range(1,30) if x % 2 == 0 and x % 3 == 0]
# [6,12,18,24]
print(divisible)

# Create a list of odd numbers from 1-50(inclusive)
print([x for x in range(51) if x%2==1])

words = ['cat', 'dog', 'elephant', 'lion', 'cheetah']
# Filter strings longer than 3 characters and convert to uppercase
filtered = [word.upper() for word in words if len(word)>3]
print(filtered)