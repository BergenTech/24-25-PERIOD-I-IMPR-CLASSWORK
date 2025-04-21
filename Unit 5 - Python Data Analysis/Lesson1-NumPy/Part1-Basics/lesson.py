import numpy as np
##########1-CREATING NDARRAYS###############
#Lists vs Arrays
my_list = [1,2,3,4,5]
# Creating 1D array from a python list
array1 = np.array(my_list)
print(my_list)
print(type(my_list))
print(array1)
print(type(array1))

#creating 2D array
my_matrix = [[1,2,3],[4,5,6]]
array2 = np.array(my_matrix)
print(array2)

#Creating special arrays
zeros = np.zeros(5) #creates a 1D array of 5 zeroes
print(zeros)
zeros_2d = np.zeros((4,3)) # 2D array 4rows 3 columns with 0s
print(zeros_2d)

ones = np.ones(4) #creates a 1D array of 4 ones
#Identity Matrix (square matrix)

square = np.eye(3) # create a 3x3 matrix 1s on the main diagonal and 0s elsewhere
print(square)

full = np.full((2,2),7) # 2x2 array filled with the 7
print(full)

##########2-CREATING SEQUENCES###############
range_array = np.arange(10) # 0-9 return NumPy array
steps = np.arange(0,10,2) # 0,2,4,6,8
#creating evenly spaced values
linspace = np.linspace(0,1,5) # [0. 0.25 0.5 0.75  1.]
random = np.random.random(4) # 4 random floats

print(f"Range Array: {range_array}")
print(f"Steps: {steps}")
print(f"Linspace: {linspace}")
print(f"Random: {random}")

#ARRAY ATTRIBUTES
arr = np.array([[1,2,3],[4,5,6]])
print(f"Shape: {arr.shape}") # (2,3) 2 rows 3 columns
print(f"Dimensions: {arr.ndim}") # 2 (2D)
print(f"Total Elements: {arr.size}")#6 Total # of elems
print(f"Data Type: {arr.dtype}") #int64 Data types elems

#DATA TYPES in NumPy
#create an array with specific data types
int_array = np.array([1,2,3], dtype=np.int32)
float_array = np.array([1,2,3], dtype=np.float64)

#convert data types
float_array = int_array.astype(np.float64)

