text = "Python Programming"
#Extract "Python"
print(text[:6])
#Extract "Programming"
print(text[7:])
#Every second character
print(text[::2])
#reverse
print(text[::-1])

# Write a function that checks if a string is a palindrome
def is_palindrome(text):
    return text == text[::-1]
print(is_palindrome("radar")) #should print True
print(is_palindrome("python")) #should print False

# Create a function that extracts every nth character from a string
def extract_nth_character(string, n):
    if n <= 0:
        raise ValueError("The value of n must be a positive integer. ")
    return string[n-1::n]

string = 'Python Programming'
n = 4
print(extract_nth_character(string,n))
# output: "l r!"