# Pandas Series Cheat Sheet

# Installing Pandas
# In terminal: pip install pandas

# Importing Pandas
import pandas as pd

# Creating a Series from a list
numbers = pd.Series([10, 20, 30, 40, 50])

# Creating a Series with custom indexes
fruits = pd.Series([3, 5, 2, 4], index=['apples', 'oranges', 'bananas', 'pears'])

# Creating a Series from a dictionary
student_scores = pd.Series({'Math': 85, 'Science': 92, 'English': 78, 'History': 88})

# Accessing elements by position
print(fruits[0])  # Single element
print(fruits[[0, 2]])  # Multiple elements

# Accessing elements by label
print(fruits['apples'])  # Single element
print(fruits[['oranges', 'pears']])  # Multiple elements

# Series attributes
print(student_scores.index)  # Get index
print(student_scores.values)  # Get values

# Basic statistics
print(student_scores.mean())  # Mean
print(student_scores.max())  # Max
print(student_scores.min())  # Min

# Arithmetic operations
prices = pd.Series([10.99, 5.49, 8.99, 3.99, 7.49], index=['apple', 'banana', 'orange', 'kiwi', 'pear'])
discounted_prices = prices * 0.9  # Apply 10% discount

# Filtering
affordable_fruits = prices[prices < 7]  # Items less than $7

# Handling missing values
data = pd.Series([10, 25, None, 40, 50, None])
print(data.isna())  # Check for missing values
print(data.isna().sum())  # Count missing values
print(data.dropna())  # Drop missing values
print(data.fillna(0))  # Fill with 0
print(data.fillna(data.mean()))  # Fill with mean
