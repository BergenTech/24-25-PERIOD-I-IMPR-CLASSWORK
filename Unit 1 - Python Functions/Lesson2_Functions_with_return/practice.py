def checkNumber(num):
    # if num > 0 :
    #     posNeg = 'Positive'
    # else:
    #     posNeg = "Negative"
        
    # if num % 2 == 0:
    #     oddEven = 'Even'
    # else:
    #     oddEven = "Odd"
    # Ternary
    oddEven = 'Even' if num % 2 == 0 else 'Odd'
    posNeg = 'Positive' if num > 0 else 'Negative'
    return f"{num} is {posNeg} and {oddEven}"
print(checkNumber(-7))
print(checkNumber(4))