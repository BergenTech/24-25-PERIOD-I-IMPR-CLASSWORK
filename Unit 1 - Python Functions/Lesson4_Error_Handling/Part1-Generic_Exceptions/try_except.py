# Generic Exception Syntax
try:
    pass #Code that might raise an exception
except Exception as e:
    pass #Code to handle exception

# number = int(input("Enter a number:"))
# result = 10 / number
# print(f"Result: {result}")
# print("After the result")

# Example 1 - Simple Division
try:
    number = int(input("Enter a number:"))
    result = 10 / number
    print(f"Result: {result}")
except Exception as e:
    print(f"An error occured:{e}")
print("After the try-except block")