number = int(input("Enter Number:")) #568
hundreds = number // 100 #5 out of 568
tens = number // 10 % 10 #6 out of 568
units = number % 10 #8 out of 568
if number > 99 and number < 1000:
    if hundreds < tens and tens < units:
        print("Yes, digits are ascending!")
    else:
        print("No, digits are not ascending!")
        
else:
    print("Not a three digit number!")