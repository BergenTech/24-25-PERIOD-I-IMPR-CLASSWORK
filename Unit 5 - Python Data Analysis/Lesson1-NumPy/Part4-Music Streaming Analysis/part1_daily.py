import numpy as np
from data import data_array, days

def analyze_by_day():
    print("\n1. ANALYSIS BY DAY OF WEEK")
    print("-"*30)
    for i, day in enumerate(days):
        day_data = data_array[:, i]
        
        day_mean = np.mean(day_data)
        day_median = np.median(day_data)
        day_range = np.max(day_data) - np.min(day_data)
        day_std = np.std(day_data)
        
        print(f"{day} Statistics:")
        print(f" Mean: {day_mean:.1f} minutes")
        print(f" Median: {day_median:.1f} minutes")
        print(f" Range: {day_range} minutes")
        print(f" Standard Deviation: {day_std:.1f} minutes \n")
        