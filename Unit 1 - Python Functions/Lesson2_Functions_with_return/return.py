# Function with a return
def add(a, b):
    return a + b # terminates the function
    return a - b # wont be executed
add(10, 5) # can not be seen in console
sum = add(10, 5) #we can assign the returned value to a variable
print(sum)
print(f"Sum:{add(10, 5)}")