# # Example 1
# def check_fuel_level(fuel_level):
#     if fuel_level < 10 :
#         raise ValueError("Fuel level is too low!")
# def drive(fuel_level):
#     check_fuel_level(fuel_level)
#     print('Driving...')

# # Use case:
# try:
#     drive(5) # This will raise an exception
#     drive(12) # This will raise an exception
# except ValueError as e:
#     print(f'Warning: {e}')
#     print("Please refuel the car!")
    
# Example 2
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a/b
# Use case:
try:
    result = divide(10,0) # will raise an exception
except ZeroDivisionError as e:
    print(f"Error: {e}")
    result = None
else:
    print(f"Result: {result}")