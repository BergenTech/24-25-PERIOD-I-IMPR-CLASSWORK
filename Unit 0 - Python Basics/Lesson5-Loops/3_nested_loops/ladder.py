########solution 1###########
# n = int(input('Enter a number:'))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j,end='')
#     print()
########solution 2###########
n = int(input('Enter a number:'))
output = ''
for i in range(1, n+1):
    for j in range(1, i+1):
        output += str(j)
    output += "\n"
print(output)