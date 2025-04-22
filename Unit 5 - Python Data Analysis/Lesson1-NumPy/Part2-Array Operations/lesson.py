import numpy as np

# ------------------------------
# Part 1: Accessing Array Elements
# ------------------------------

# Indexing 1D Arrays
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])      # 10
print(arr[4])      # 50
print(arr[-1])     # 50
print(arr[-2])     # 40

# Slicing 1D Arrays
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[1:5])    # [20 30 40 50]
print(arr[:3])     # [10 20 30]
print(arr[5:])     # [60 70 80]
print(arr[::2])    # [10 30 50 70]
print(arr[::-1])   # [80 70 60 50 40 30 20 10]

# Indexing 2D Arrays
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(matrix[0, 0])   # 1
print(matrix[2, 3])   # 12
print(matrix[1, -1])  # 8

# Slicing 2D Arrays
print(matrix[1, :])    # [5 6 7 8]
print(matrix[:, 2])    # [3 7 11]
print(matrix[0:2, 1:3])  # [[2 3], [6 7]]

# ------------------------------
# Part 2: Modifying Array Elements
# ------------------------------

arr = np.array([1, 2, 3, 4, 5])
arr[0] = 100
print(arr)  # [100 2 3 4 5]

arr[1:4] = 200
print(arr)  # [100 200 200 200 5]

arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3
arr[mask] = 0
print(arr)  # [1 2 3 0 0]

# ------------------------------
# Exercise 1: Indexing and Slicing
# ------------------------------

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# value_7 = 
# print("Value 7:", value_7)

# last_row = 
# print("Last row:", last_row)

# first_col = 
# print("First column:", first_col)

# center_subarray = arr[1:3, 1:3]
# print("Center 2x2 sub-array:\n", center_subarray)


