# Python Exception Handling: Lesson Material

## 1. Introduction

Exceptions in Python are events that occur during the execution of a program that disrupt the normal flow of instructions. They are used to handle errors, unusual conditions, or expected issues that may arise during program execution.

Why is exception handling important?
- It prevents programs from crashing when encountering errors
- It allows for graceful error handling and user-friendly error messages
- It helps in debugging by providing informative error traces
- It enables programs to recover from certain error conditions

## 2. Basic Exception Handling

In Python, we use try-except blocks to handle exceptions. The basic structure is:

```python
try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception
```

Example:

```python
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

# Test the function
divide_numbers(10, 2)  # Output: Result: 5.0
divide_numbers(10, 0)  # Output: Error: Cannot divide by zero!
```

Exercise: Modify the `divide_numbers` function to handle a `TypeError` that might occur if non-numeric inputs are provided.

## 3. Multiple Exception Types

You can handle different types of exceptions separately using multiple except blocks:

```python
def process_input(value):
    try:
        num = int(value)
        result = 10 / num
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter a valid number!")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

# Test the function
process_input("5")   # Output: Result: 2.0
process_input("0")   # Output: Error: Cannot divide by zero!
process_input("abc") # Output: Error: Please enter a valid number!
```

Exercise: Add another except block to handle a `TypeError` that might occur if a different type of object is passed to the function.

## 4. Generic Exception Handling

Sometimes, you might want to catch all exceptions without specifying their types. This is done using a generic except block:

```python
def generic_exception_handler(value):
    try:
        num = int(value)
        result = 10 / num
        print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Test the function
generic_exception_handler("5")   # Output: Result: 2.0
generic_exception_handler("0")   # Output: An error occurred: division by zero
generic_exception_handler("abc") # Output: An error occurred: invalid literal for int() with base 10: 'abc'
```

While generic exception handling can be useful, it's generally better to catch specific exceptions when you can anticipate them. This allows for more precise error handling.

Exercise: Convert the `process_input` function from the previous example to use generic exception handling. Then, convert the `generic_exception_handler` function to use specific exception types.

## 5. Try-Except-Else-Finally

The full structure of a try statement includes `else` and `finally` clauses:

```python
def file_operations(filename):
    try:
        file = open(filename, "r")
        content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    else:
        print(f"File contents: {content}")
    finally:
        print("File operation attempt completed.")
        try:
            file.close()
        except:
            pass

# Test the function
file_operations("existing_file.txt")
file_operations("non_existent_file.txt")
```

- The `else` block runs if no exception was raised in the `try` block.
- The `finally` block always runs, regardless of whether an exception was raised.

Exercise: Modify the `file_operations` function to include some operations in the `else` clause, such as writing the content to a new file.

