fruits = ['apple', 'banana', 'cherry']
# Part 2: List Methods
# 2.1 Modification Methods

# Append: Add element to end
fruits.append('orange')
# Insert: Add element at specific position
fruits.insert(1, 'grape')
# Extend: Add multiple elements
more_fruits = ['kiwi', 'melon']
fruits.extend(more_fruits)
# Remove: Remove specific element
fruits.remove('banana')
# Pop: Remove and return element
last_fruit = fruits.pop()  # Removes last element
specific_fruit = fruits.pop(1)  # Removes element at index 1