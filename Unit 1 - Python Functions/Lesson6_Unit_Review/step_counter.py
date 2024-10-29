def add_steps(day, steps, current_steps):
    print(f"Steps added for {day}: {steps}")
    return current_steps + steps
def weekly_total(total_steps):
    return total_steps
def set_goal(goal):
    print(f"Weekly goal set to {goal} steps.")
    return goal
def check_progress(total_steps, goal):
    remaining_steps = goal - total_steps
    if remaining_steps > 0:
        print(f"You’ve walked {total_steps} steps so far. You need {remaining_steps} more steps to reach your goal.")
    else:
        print("Congratulations! You’ve reached your weekly goal!")
def reset_steps():
    print("Weekly steps have been reset.")
    return 0

def main():
    total_steps = 0
    weekly_goal = 0
    print("Welcome to the Step Counter Tracker!")
    while True:
        print("\nChoose an option:")
        print("1. Add Steps")
        print("2. View Weekly Total")
        print("3. Set Weekly Goal")
        print("4. Check Progress")
        print("5. Reset Steps")
        print("6. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                day = input("Enter day of the week (e.g., Monday, Tuesday): ")
                steps = int(input("Enter number of steps: "))
                total_steps = add_steps(day, steps, total_steps)
            elif choice == 2:
                print(f"Weekly Total Steps: {weekly_total(total_steps)}")
            elif choice == 3:
                weekly_goal = int(input("Enter your weekly step goal: "))
                weekly_goal = set_goal(weekly_goal)
            elif choice == 4:
                check_progress(total_steps, weekly_goal)
            elif choice == 5:
                total_steps = reset_steps()
            elif choice == 6:
                print("Thank you for using the Step Counter Tracker!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

