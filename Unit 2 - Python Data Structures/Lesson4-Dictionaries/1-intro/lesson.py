# Creating dictionaries
empty_dict = {}
print(type(empty_dict))
simple_dict = {'name':"Roby", 'favorite_class':"compsci", "age": 15, 15 : "age"}
dict_constructor = dict(name="John", age=20)

#1 Basic Operations
person = {'name': "Alice", "age": 15, "city": 'teterboro'}
print(person['name'])  #Access value
person["job"] = "Engineer" #Add new key-value pair
print(person)
person['age'] = 20 # Modify existing value
del person['city'] # remove key-value pair
print(person)

#2 Common Dictionary Methods
sample_dict = {"a":1, "b":2, "c":3}
# Accessing Methods
value = sample_dict.get('a') # Returns 1
value = sample_dict.get('z', 0) # Returns 0 (default value)
value = sample_dict.get('z', "Joel") # Returns 0 (default value)
print(value)
keys = sample_dict.keys() # Returns dict keys as a 'dict_keys'
print(keys)
print(type(keys))
# print(keys[0]) # TypeError: 'dict_keys'
for key in keys:
    print(key)
    
values = sample_dict.values() # Returns dict_calues
print(values)
[print(val) for val in values] # Iterate through the values

items = sample_dict.items() # Returns dict_items
print(items) #dict_items([('a', 1), ('b', 2), ('c', 3)])

# get() method safe access
value = sample_dict.get("a","Not Exist!")
print(value)

# update() - Merge dictionaries
sample_dict2 = {"d":4, "e":5}
sample_dict.update(sample_dict2)
print(sample_dict)

# pop(key, default value) - remove key-val and returns val
value_to_remove = sample_dict.pop("e")
print(sample_dict)
print(value_to_remove)

# Basic Comprehension
squares = [x**2 for x in range(5)]
print(squares)
squares = {x:x**2 for x in range(5)}
print(squares)