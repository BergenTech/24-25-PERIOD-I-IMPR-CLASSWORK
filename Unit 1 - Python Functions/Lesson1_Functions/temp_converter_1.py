def CtoF(temp):
    Fahrenheit = round(9.0 / 5.0 * temp + 32, 2)
    print(f"Temperature: {temp}°C = {Fahrenheit}°F")

def FtoC(temp):
    Celsius = round((temp - 32) * 5 / 9, 2)
    print(f"Temperature: {temp}°F = {Celsius}°C")

while True:
    print("TEMPERATURE CONVERTER")
    print("0 - Quit\n1 - CtoF\n2 - FtoC")
    select = input("Select an Option: ")
    select = int(select)
    temp = input("Enter Temperature: ")
   
    if select == 0:
        print("Exiting the Program...")
        break
    if select == 1:
        CtoF(temp)
    elif select == 2:
        FtoC(temp)
