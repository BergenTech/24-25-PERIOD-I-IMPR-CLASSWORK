cart = ["bread", "milk"]
# Adding and Removing Elements
def manage_shopping_cart():
    #Add a new Item
    cart.append("eggs")
    #Remove an item
    cart.remove("milk")
    return cart
print(manage_shopping_cart())
#pop() removes the element at the specified location default(-1)
print(cart.pop())
print(cart)
cart = ["bread", "milk", "eggs"]
print(cart.pop(1))
print(cart)

# Transforming list elements
def square_number(numbers:list)->list:
    squared = []
    for number in numbers:
        squared.append(number**2)
    return squared
    
result = square_number([1,2,3,4])
print(result) #Output:[1,4,9,16]

# Generate Random Numbers
import random
def generate_random_numbers(count, range_start, range_end):
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(range_start, range_end))
    return numbers

print(generate_random_numbers(10, 25, 75))

# Filter elements in a list
# def filter_even(numbers:list) -> list:
#     even_numbers = []
#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)
#     return even_numbers

# return both the list of even numbers and the modified original list containing only the odd numbers
def filter_even(numbers:list) -> list:
    even_numbers = []
    odd_numbers = numbers.copy()
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(numbers)
            odd_numbers.remove(number)
    return even_numbers, numbers

# example
example_numbers = generate_random_numbers(15, 10, 99)
even, odd = filter_even(example_numbers)
print(f"List of even numbers:{even}")
print(f"List of odd numbers:{odd}")
# print(filter_even(example_numbers)) #Output will be a list of even numbers
