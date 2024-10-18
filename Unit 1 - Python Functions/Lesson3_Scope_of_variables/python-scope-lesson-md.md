# Python Variable Scope Lesson

Variable scope in Python determines where in your code a variable can be accessed or modified. Understanding scope is crucial for writing clean, efficient, and bug-free code. This lesson covers four main concepts related to variable scope in Python functions.

## 1. Local Scope

Variables defined inside a function have a local scope. They can only be accessed within that function.

```python
def local_scope_example():
    x = 10  # x is a local variable
    print(f"Inside function: x = {x}")

local_scope_example()
# print(x)  # This would raise a NameError
```

In this example, `x` is only accessible inside the `local_scope_example()` function. Trying to access it outside the function would result in a `NameError`.

## 2. Global Scope

Variables defined outside of any function have a global scope. They can be accessed from anywhere in the code, including inside functions.

```python
y = 20  # y is a global variable

def global_scope_example():
    print(f"Inside function: y = {y}")

global_scope_example()
print(f"Outside function: y = {y}")
```

Here, `y` is a global variable and can be accessed both inside and outside the `global_scope_example()` function.

## 3. Modifying Global Variables

To modify a global variable inside a function, you need to use the `global` keyword.

```python
z = 30

def modify_global():
    global z
    z = 40
    print(f"Inside function: z = {z}")

print(f"Before function call: z = {z}")
modify_global()
print(f"After function call: z = {z}")
```

In this example, we use the `global` keyword to indicate that we want to modify the global variable `z` inside the `modify_global()` function.

## 4. Nonlocal Variables

The `nonlocal` keyword is used in nested functions to work with variables from the outer (enclosing) function's scope.

```python
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
```

Here, `a` is defined in the `outer_function()`, and we use the `nonlocal` keyword in the `inner_function()` to modify `a` in the outer function's scope.

## Conclusion

Understanding variable scope is essential for writing effective Python code. Local variables provide encapsulation within functions, global variables offer shared state across your program, and nonlocal variables allow for complex nested function interactions. Always be mindful of your variable scopes to prevent unexpected behavior in your code.
