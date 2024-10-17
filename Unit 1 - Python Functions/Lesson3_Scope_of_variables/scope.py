# Python Variable Scope Lesson

# 1. Local Scope
def local_scope_example():
    x = 10  # x is a local variable
    print(f"Inside function: x = {x}")

local_scope_example()
# print(x)  # This would raise a NameError

# 2. Global Scope
y = 20  # y is a global variable

def global_scope_example():
    print(f"Inside function: y = {y}")

global_scope_example()
print(f"Outside function: y = {y}")

# 3. Modifying Global Variables
z = 30

def modify_global():
    global z
    z = 40
    print(f"Inside function: z = {z}")

print(f"Before function call: z = {z}")
modify_global()
print(f"After function call: z = {z}")

# 4. Nonlocal Variables
def outer_function():
    a = 50
    
    def inner_function():
        nonlocal a
        a = 60
        print(f"Inside inner function: a = {a}")
    
    print(f"Before inner function call: a = {a}")
    inner_function()
    print(f"After inner function call: a = {a}")

outer_function()