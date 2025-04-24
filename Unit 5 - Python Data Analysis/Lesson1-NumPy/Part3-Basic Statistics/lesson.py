# # Basic Statistics
# import numpy as np
# data = np.array([10, 15, 15, 18, 20, 35, 80])
# # Central tendency
# print("Mean:", np.mean(data))             # 27.57
# print("Median:", np.median(data))         # 18.0
# # Spread and variation
# print("Standard Deviation:", np.std(data))# ~24.36
# print("Variance:", np.var(data))          # ~593.67
# print("Range:", np.ptp(data))             # 70
# # Extremes
# print("Min:", np.min(data))               # 10
# print("Max:", np.max(data))               # 80
# # Aggregation
# print("Sum:", np.sum(data))               # 193
# print("Product:", np.prod(data))          # 12600000
# # Percentiles
# print("25th Percentile:", np.percentile(data, 25))  # 15.0
# print("75th Percentile:", np.percentile(data, 75))  # 35.0
# # Counting
# print("Values above 20:", np.sum(data > 20))  # 2


# #Exercise 1: Grading Insights – You’re the Teacher!
# import numpy as np


# test_scores = np.array([85, 90, 67, 78, 92, 83, 88, 95, 73, 80])


# mean_score = np.mean(test_scores)
# print(f"Average (mean) score: {mean_score}")  # 83.1


# median_score = np.median(test_scores)
# print(f"Middle score (median): {median_score}")  # 83.5


# min_score = np.min(test_scores)
# max_score = np.max(test_scores)
# print(f"Lowest score: {min_score}, Highest score: {max_score}")  # 67, 95


# score_range = np.ptp(test_scores)
# print(f"Score range: {score_range}")  # 28


# std_dev = np.std(test_scores)
# print(f"Score consistency (standard deviation): {std_dev:.2f}")  # ~8.73


# count_above_80 = np.sum(test_scores > 80)
# print(f"Number of students who scored above 80: {count_above_80}")  # 6


# p25 = np.percentile(test_scores, 25)
# p75 = np.percentile(test_scores, 75)
# print(f"25th percentile: {p25}, 75th percentile: {p75}")  # 75.5, 89.5


#Exercise 2: Weekly Weather Recap for the School Newsletter
import numpy as np
temperatures = np.array([72, 75, 68, 79, 82, 77, 73])


mean_temp = np.mean(temperatures)
print(f"Average temperature: {mean_temp:.2f}°F")  # ~75.14°F


median_temp = np.median(temperatures)
print(f"Middle temperature (median): {median_temp}°F")  # 75°F


min_temp = np.min(temperatures)
max_temp = np.max(temperatures)
print(f"Temperature range: {min_temp}°F to {max_temp}°F")  # 68°F to 82°F


temp_range = np.ptp(temperatures)
print(f"Temperature difference during the week: {temp_range}°F")  # 14°F


std_temp = np.std(temperatures)
print(f"Temperature variation (standard deviation): {std_temp:.2f}")  # ~4.79°F


days_above_75 = np.sum(temperatures > 75)
print(f"Days warmer than 75°F: {days_above_75}")  # 3