import numpy as np
# Create the MeloStream dataset as a NumPy array
# Each row represents a user (1-30)
# Each column represents a day of the week (Monday-Sunday)
data = [
    [35, 42, 28, 30, 65, 87, 92],  # User 1
    [120, 95, 105, 110, 150, 180, 190],  # User 2
    [45, 50, 40, 48, 75, 95, 85],  # User 3
    [75, 68, 80, 72, 95, 125, 130],  # User 4
    [25, 30, 22, 28, 45, 65, 60],  # User 5
    [90, 85, 75, 82, 110, 145, 150],  # User 6
    [55, 60, 52, 58, 85, 105, 110],  # User 7
    [140, 132, 145, 138, 165, 210, 195],  # User 8
    [65, 72, 60, 68, 95, 115, 120],  # User 9
    [15, 18, 12, 16, 30, 45, 40],  # User 10
    [85, 82, 78, 80, 105, 130, 135],  # User 11
    [50, 55, 48, 52, 75, 100, 95],  # User 12
    [110, 105, 115, 108, 140, 170, 180],  # User 13
    [40, 45, 38, 42, 60, 85, 80],  # User 14
    [70, 75, 68, 72, 95, 120, 125],  # User 15
    [20, 25, 18, 22, 40, 55, 50],  # User 16
    [95, 90, 85, 92, 120, 155, 160],  # User 17
    [60, 65, 58, 62, 85, 110, 115],  # User 18
    [130, 125, 135, 128, 160, 200, 205],  # User 19
    [30, 35, 28, 32, 50, 75, 70],  # User 20
    [80, 78, 82, 76, 105, 135, 140],  # User 21
    [45, 52, 42, 48, 70, 95, 90],  # User 22
    [105, 100, 110, 102, 130, 165, 170],  # User 23
    [35, 40, 32, 38, 60, 80, 75],  # User 24
    [65, 70, 62, 68, 90, 115, 120],  # User 25
    [25, 20, 22, 18, 35, 50, 45],  # User 26
    [100, 95, 105, 98, 125, 155, 160],  # User 27
    [55, 60, 52, 58, 80, 105, 110],  # User 28
    [125, 130, 120, 128, 155, 190, 200],  # User 29
    [40, 45, 38, 42, 65, 85, 80]   # User 30
]

# Convert list of lists to a NumPy array
data_array = np.array(data)

# Day names for better readability in output
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
