length = 0
sum = 0
while True:
    number = int(input('Enter Number:'))
    if number == 0:
        print(f'#####################')
        break
    else:
        sum += number
        length +=1
print(f'Length of the  sequence: {length}')
print(f'Average of the  sequence: {sum/length}')

