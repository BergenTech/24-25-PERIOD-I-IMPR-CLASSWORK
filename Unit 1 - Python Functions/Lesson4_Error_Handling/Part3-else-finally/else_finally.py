#1 else clause
"""
print('Example1:Using the else clause')
try:
    x = int(input('Enter a number:'))
    result = 10 / x
except ZeroDivisionError:
    print('Error: Cannot divide by zero!')
else:
    #This only executes if no exception was raised
    print(f'Result: {result}')
print('End of Example 1')
"""
#2 finally clause
# print('Let\'s play a simple game!')
# try :
#     # pass
#     number = int(input('Enter a number:'))
#     # check if number within valid range
#     if 1 <= number <=10: #equivalent 1<=number and number <=10
#         print(f"You entered {number}. That's a valid number!")
#     else:
#         raise ValueError('Number out of range!')    
# except ValueError as e:
#     # pass
#     print(f'Error: {e}')
#     # This block runs if a ValueError occurs
#     print(f'Oops! There was an error {e}')
#     print("Please try again and enter a valid number!") 
# finally:
#     # pass
#     # This block always runs, no matter what happened above
#     print('\nThank you for playing our number game!')
#     print('Remember, always enter a number between 1 and 10')
# print('End of program...')

#Example3 - Combining else-finally
try:
    num = int(input('Enter a positive number:'))
    if num <=0 :
        pass
        raise ValueError('Number must be positive!')
except ValueError as e:
    print(f'Error:{e}')
else:
    result = 10 / num
    print(f"Result:{result}")
finally:
    print('Execution completed!')
print('End of example 3')