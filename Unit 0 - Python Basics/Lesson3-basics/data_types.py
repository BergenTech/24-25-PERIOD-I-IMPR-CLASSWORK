#String data type - str
#literal assignment
f_name = 'Emre'
l_name = 'Gemici'
print(type(f_name))
print(type(l_name)==str)
print(isinstance("bagel",str))
print(isinstance(1,str))

#Casting a number to a string
year = str(2024)
print(type(year))

#Boolean data type
val = True
val2 = bool('False')
val3 = bool('')
print(type(val))
print(val2)
print(val3)
print(isinstance(val3, bool))

#float data type
gpa = 3.56
x = float(1)
print(x)
print(type(gpa))
print(isinstance(5,float))

#integer data type
gpa = 3.56
x = int(gpa)
print(x)
print(type(x))
print(isinstance(x,int))

#complex data type
comp_val = 3+2j
print(type(comp_val))
