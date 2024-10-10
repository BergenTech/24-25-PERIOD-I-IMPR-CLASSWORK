# Make a function to calculate the temp conversion
def tempConverter(temp, scale):
    if scale == 'C':
        Fahrenheit = round(9/5*temp+32,2)
        return f"{temp}°C = {Fahrenheit}°F"
    elif scale == 'F':
        Celsius = round((temp-32)*5/9,2)
        return f"{temp}°F = {Celsius}°C"
    else:
        return f"Invalid Scale"

# Make a menu and call the the conversion function
while True:
    temp_input = input("Enter the temperature:")
    if temp_input == 'exit':
        print('Exiting the program!')
        break
    scale = input('Current Scale - [F or C]')
    temp = float(temp_input)
    result = tempConverter(temp, scale)
    print(result)
    