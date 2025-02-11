# Basic Dictionary Comprehension
# Syntax: {key_expression: value_expression for item in iterable}


# 1. Creating a simple dictionary of squares
numbers = range(1, 6)
squares = {num: num**2 for num in numbers}
print("Basic squares dictionary:", squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 2. Converting two lists into a dictionary
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
name_age_dict = {name: age for name, age in zip(names, ages)}
print("\nDictionary from two lists:", name_age_dict)
# Output: {'Alice': 25, 'Bob': 30, 'Charlie': 35}


# 3. Dictionary comprehension with conditions
# Syntax: {key_expression: value_expression for item in iterable if condition}
numbers = range(1, 11)
even_squares = {num: num**2 for num in numbers if num % 2 == 0}
print("\nEven squares only:", even_squares)
# Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# 4. Transforming keys and values of an existing dictionary
original = {'a': 1, 'b': 2, 'c': 3}
transformed = {k.upper(): v*2 for k, v in original.items()}
print("\nTransformed dictionary:", transformed)
# Output: {'A': 2, 'B': 4, 'C': 6}


# 5. Filtering with multiple conditions
numbers = range(1, 11)
filtered = {x: x**3 for x in numbers if x % 2 == 0 and x % 3 == 0}
print("\nFiltered with multiple conditions:", filtered)
# Output: {6: 216}


# 6. Practical example: Word length mapping
sentence = "Python is a powerful programming language"
word_lengths = {word: len(word) for word in sentence.split()}
print("\nWord length mapping:", word_lengths)
# Output: {'Python': 6, 'is': 2, 'a': 1, 'powerful': 8, 'programming': 11, 'language': 8}


# 7. Case-insensitive dictionary
text = "Hello World"
char_count = {char.lower(): text.lower().count(char.lower())
              for char in set(text) if char.isalpha()}
print("\nCharacter frequency (case-insensitive):", char_count)
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}


# 8. Conditional value assignment
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
grades = {name: 'Pass' if score >= 80 else 'Fail'
         for name, score in scores.items()}
print("\nPass/Fail grades:", grades)
# Output: {'Alice': 'Pass', 'Bob': 'Pass', 'Charlie': 'Fail', 'David': 'Pass'}

