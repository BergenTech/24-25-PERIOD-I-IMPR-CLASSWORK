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