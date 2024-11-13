# 'in' keyword in Python checks if a substring exists within a larger string.

# Simple Substring Checking
text = 'Hello, Python Programmer!'
print('Python' in text) # True
print('JavaScript' in text) # False
print('hello' in text) # False (case sensitive)
print('o, P' in text) # True

# Exercise - email validation
def is_valid_email(email):
    if "@" not in email:
        return False
    if "." not in email:
        return False

print(is_valid_email('user@bergen.org'))