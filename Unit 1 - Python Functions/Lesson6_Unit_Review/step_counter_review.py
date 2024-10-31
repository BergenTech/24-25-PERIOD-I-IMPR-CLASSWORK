# 1 - Define functions that will be used in the menu
# 2 - Define a main() menu that will include a while True block to continously call the defined functions above
#3 - call the main() in the if __name___ == "__main__": 

# Step 1 - Define Functions
# Adding the step
def add_steps(day, steps):
    print(f"Steps added for {day}: {steps}")
    return steps + total_steps

def set_goal(goal):
    print(f"Weekly goal set to {goal} steps")
    return goal


total_steps = 0
weekly_goal = 0
# Step 2 - Main Menu
def main():
    print("Welcome!")
    while True:
        print("Choose an option:")
        print("1. Add Steps:")
        print("6. Exit:")
        try:
            choice = int(input("Choose an option:"))
            if choice == 6:
                print("Thank you! Exiting the program!")
                break
            elif choice == 1:
                day = input("Enter the day of the week:")
                steps = int(input("Enter number of the steps:"))
                total_steps = add_steps(day, steps)
            elif choice == 3:
                weekly_goal = int(input("Enter your weekly step goal:"))
                weekly_goal = set_goal(weekly_goal)
        except:
            print("Invalid Input. Please try again!")
        
#Step 3 - call the function 
if __name__ == "__main__":
    main()