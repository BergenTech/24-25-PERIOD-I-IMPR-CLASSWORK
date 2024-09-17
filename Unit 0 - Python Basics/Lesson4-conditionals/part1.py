# # Exercise 1 - Even or Odd
# number = int(input("Enter a number:"))
# if number % 2 == 0:
#     print("The number is even!")
# else:
#     print("The number is odd!")
    
# Exercise 2 - Temperature Converter
# convert a temperature from C to F or F to C
t = float(input("Enter the temperature:"))
unit = input("Enter the unit to convert to:").upper()

if unit == "C":
    converted_temp = (t-32)*5/9
    print(f"The temperature in Celcius is {converted_temp:.2f}°C")#alt+0176 °
elif unit == 'F':
    converted_temp = (t*9/5)+32
    print(f"The temperature in Fahrenheit is {converted_temp:.2f}°F")#alt+0176 °
else:
    print("invalid unit!")