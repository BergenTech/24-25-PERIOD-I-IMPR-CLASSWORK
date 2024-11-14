# Case Manipulation Methods
text = "Python Programming"
print(text.upper())      # Convert to uppercase
print(text.lower())      # Convert to lowercase
print(text.title())      # Capitalize first letter of each word
print(text.capitalize()) # Capitalize first letter of string
print(text.swapcase())   # Swap case of each character

# Whitespace Handling Methods
print(text.strip())      # Remove leading and trailing whitespace
print(text.lstrip())     # Remove leading whitespace
print(text.rstrip())     # Remove trailing whitespace

# Remove specific characters
text2 = "###Python###"
print(text2.strip('#'))  # Remove '#' from both ends

# Search and Replace Methods
text = "Python is amazing, Python is fun"
print(text.count('Python'))          # Count occurrences
print(text.find('is'))               # Find first occurrence (returns index)
print(text.rfind('is'))              # Find last occurrence (returns index)
print(text.replace('Python', 'Java')) # Replace all occurrences
print(text.replace('Python', 'Java', 1)) # Replace first occurrence only

# Character Type Checking
print(f"Original text: '{text}'")
print(f"Is alphanumeric? {text.isalnum()}")
print(f"Is alphabetic? {text.isalpha()}")
print(f"Is numeric? {text.isnumeric()}")
print(f"Is decimal? {text.isdecimal()}")
print(f"Is lower? {text.islower()}")
print(f"Is upper? {text.isupper()}")
print(f"Is title? {text.istitle()}")
print(f"Is space? {text.isspace()}")

# Split Methods
# is used to divide a string into a list of substrings based on a delimiter.
text = "Python,Java,C++,JavaScript"
print(text.split(','))           # Split by comma
print(text.rsplit(',', 2))# Split from right, limit to 2 splits

text2 = "Python Programming\nJava Programming\nC++ Programming"
print(text2.splitlines()) # Split by newlines

text3 = "Python    Programming    Language"
print(text3.split()) # Split by whitespace

# Split Method Chaining
# refers to calling multiple string methods in a single line, where each method is applied to the result of the previous one.
result = " hello world ".strip().upper().replace("WORLD", "Python")
print(result)

'''
strip() removes leading and trailing spaces,
upper() converts the string to uppercase,
replace("WORLD", "Python") replaces "WORLD" with "Python".

'''