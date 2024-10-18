try:
    expense = float(input("Enter your expense amount: "))
    print(f"Your expense amount is: ${expense:.2f}")
except Exception as e:
    print(f"An error occurred: {e}")
print("End of program.")