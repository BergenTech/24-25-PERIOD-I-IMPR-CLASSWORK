# Basic Statistics
import numpy as np
data = np.array([10, 15, 15, 18, 20, 35, 80])
# Central tendency
print("Mean:", np.mean(data))             # 27.57
print("Median:", np.median(data))         # 18.0
# Spread and variation
print("Standard Deviation:", np.std(data))# ~24.36
print("Variance:", np.var(data))          # ~593.67
print("Range:", np.ptp(data))             # 70
# Extremes
print("Min:", np.min(data))               # 10
print("Max:", np.max(data))               # 80
# Aggregation
print("Sum:", np.sum(data))               # 193
print("Product:", np.prod(data))          # 12600000
# Percentiles
print("25th Percentile:", np.percentile(data, 25))  # 15.0
print("75th Percentile:", np.percentile(data, 75))  # 35.0
# Counting
print("Values above 20:", np.sum(data > 20))  # 2
