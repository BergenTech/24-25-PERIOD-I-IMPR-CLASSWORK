#1 Use as a counter
# for i in range(5):
# for i in range(1,5):
# for i in range(1,5,2):
# for i in range(10,5,-2):
#     # print('hello BT!')
#     # print(f'{i}:hello BT!')
#     # print(f'{i+1}:hello BT!')
#     print(f'{i}:hello BT!')

#2 Iterating over a sequence
fruit = 'apple'
# for letter in fruit:
# for letter in "apple":
#     print(letter)
# for i in range(len(fruit)):
#     print(f"index {i}: is {fruit[i]}")
    
#3 When you need both index and the value
# enumerate()
for i, letter in enumerate(fruit):
    print(f"index {i}: is {letter}")  

