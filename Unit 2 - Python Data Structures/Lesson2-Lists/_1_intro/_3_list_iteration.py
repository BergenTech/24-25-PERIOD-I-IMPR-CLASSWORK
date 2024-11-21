# dir() - directory of attributes and methods
# numbers = [1,2,3]
# print(dir(numbers))
# Part3: Iteration
# 3.1 For Loop
fruits = ["apple", "banana", "cherry"]
# Standard Iteration
for fruit in fruits:
    print(fruit)
    
# Iterating with index
for i in range(len(fruits)):
    print(fruits[i])
    
# Iterating with index and element
for i in range(len(fruits)):
    print(f"{i+1}:{fruits[i]}")
    
#enumerate function - index, element
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
    
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
    
#3.2 Reverse Iteration
# Iterating in reverse order - reversed() method
for fruit in reversed(fruits):
    print(fruit)
# Reverse enumeration
for i, fruit in enumerate(reversed(fruits)):
        print(f"Reversed Index {i}: {fruit}")

# 3.3 Iterating with multiple lists
names = ["Alice", "Roby", "Edward"]
ages = [12,14,15]

# zip function
for name, age in zip(names, ages):
    print(f"{name} is {age} years old!")