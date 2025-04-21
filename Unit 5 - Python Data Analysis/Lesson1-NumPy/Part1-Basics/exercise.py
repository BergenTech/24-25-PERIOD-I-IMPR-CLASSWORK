import numpy as np
# ------------------------------------------
# Exercise: Creating Arrays
# ------------------------------------------

# 1. Create an array of integers from 10 to 49
arr1 = np.arange(10, 50)

# 2. Create a 3x3 array of random integers between 1 and 100
arr2 = np.random.randint(1, 101, size=(3, 3))

# 3. Create a 5x5 identity matrix
arr3 = np.eye(5)

# 4. Create 20 linearly spaced points between 0 and 1
arr4 = np.linspace(0, 1, 20)

# Display exercise outputs
print("\n1D array from 10 to 49:\n", arr1)
print("\n3x3 random integers between 1 and 100:\n", arr2)
print("\n5x5 identity matrix:\n", arr3)
print("\n20 linearly spaced points between 0 and 1:\n", arr4)


# ------------------------------------------
# Exercise: Array Attributes
# For each array below:
# 1. Predict its shape, size, and number of dimensions
# 2. Check your prediction using NumPy attributes

a = np.zeros(10)
print("Array a:")
print(f"Shape: {a.shape}, Size: {a.size}, Dimensions: {a.ndim}")  # Shape: (10,), Size: 10, Dimensions: 1

b = np.ones((3, 4))
print("\nArray b:")
print(f"Shape: {b.shape}, Size: {b.size}, Dimensions: {b.ndim}")  # Shape: (3, 4), Size: 12, Dimensions: 2

c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nArray c:")
print(f"Shape: {c.shape}, Size: {c.size}, Dimensions: {c.ndim}")  # Shape: (2, 2, 2), Size: 8, Dimensions: 3
