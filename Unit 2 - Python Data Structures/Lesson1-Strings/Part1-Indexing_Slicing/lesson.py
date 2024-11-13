# Positive indexing - zero-based
fruit = 'apple'
print(fruit[0]) #first character
print(fruit[4]) #last character
print(fruit[len(fruit)-1]) #last character

#Negative indexing - -1 last element
print(fruit[-1]) #last element
print(fruit[-5]) #first element
print(fruit[-len(fruit)]) #first element

#BASIC SLICING
# Slicing:extract a portion of a sequence
# sequence[start:stop:step]
numbers = '0123456789'
#elements from index 2 to 4
print(numbers[2:4])
#numbers from start to number 5
print(numbers[0:6])
print(numbers[:6])
#numbers from index 3 up to stop
print(numbers[3:9])
#numbers from index 3 up to stop(inclusive)
print(numbers[3:])
#all elements (creating a copy)
print(numbers[:])
# print(numbers[-11])

#ADVANCED SLICING
#Using step values
#every second element
print(numbers[::2])
#every second element starting from index 3
print(numbers[3::2])
#reverse the elements
print(numbers[::-1])
#reverse slice from 8 to 4
print(numbers[8:3:-1])
