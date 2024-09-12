#check the type of data - str()
school = "Bergen Tech"
print(type(school))
grade = 10
print(type(grade))
gpa = "4"
print(type(gpa))
gpa = int(gpa)
print(type(gpa))
gpa = "4.0"
gpa = float(gpa)
print(type(gpa))
#multiple assignment
course,period = 'IMPR', 1
print(course)
print(course,period)
#deleting a variable
color = 'red'
print(color)
# del color
# print(color)

#Swapping values
x, y = 5, 10
print(x)
x, y = y, x
print(x)
#spanning a string across the lines
state = '''This message will span
several lines
of text
'''
print(state)
# String concatenation
name = 'John'
print('Hello' + name)
print('Hello' + " " + name)
print('Hello',name,name)

#f-strings
print(f"Hello {name}!")