# def format_email(email):
#     # Step 1: Remove leading and trailing spaces
#     email = email.strip()
#     # Step 2: Remove spaces 
#     email = email.replace(" ", "")
#     # Step 3: Convert to lowercase
#     return email.lower()
#     # Method Chaining
#     return email.strip().replace(" ", "").lower()




# # Test cases
# email1 = " User@Example.com "
# email2 = "user @ example.com"
# email3 = "USER@EXAMPLE.COM"


# print(format_email(email1)) #output: user@example.com
# print(format_email(email2)) #output: user@example.com
# print(format_email(email3)) #output: user@example.com

def find_substring(text:str, sub:str):
    count = text.count(sub)
    first_occurence = text.find(sub)
    last_occurence = text.rfind(sub)
    return f'''
    Count: {count}
    First Occurrence:{first_occurence}
    Last Occurrence:{last_occurence}
    '''

test_string = "apple banana apple cherry apple"
test_substring = "apple"
print(find_substring(test_string,test_substring))