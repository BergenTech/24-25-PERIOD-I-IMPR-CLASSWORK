# 1. Basic List Creation
### Traditional Method
# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)
#2 Alternative Traditional MEthod
# def square(x):
#     return x**2
# for x in range(10):
#     squares.append(square(x))
# print(squares)

#3. List Comprehension Method
# squares = [x**2 for x in range(10)]
# print(squares)
# numbers = [25, 36, 80, 126, 66, 3]
# print([number%3 for number in numbers])
print([n for n in range(5,1001,5)])
