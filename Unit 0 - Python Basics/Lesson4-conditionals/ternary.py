# true_val if condition else false_val
# x = 10
# if x > 5:
#     result = "Greater"
# else:
#     result = "Smaller"
# result = "Greater" if x > 5 else "Smaller"

# Movie Ticket Pricing
#Determine the price of a movie based on age and time of the day

age = 17
time = 14
price = 5 if age < 12 else 7 if age <= 18 else 10
price -= 2 if time <16 else 0 #Discount before 4pm
result = f"Ticket Price: ${price}"
print(result) 