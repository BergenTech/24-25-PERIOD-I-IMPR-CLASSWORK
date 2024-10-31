# Purpose: Adds a specified amount of points to the current score
# Returns (int): The updated total score after adding the points
#Args: points (int), current_score (int)
def add_score(points, current_score):
    try:
        new_total = points + current_score
        print(f"{points} points added. New Total:{new_total}")
        return new_total
    except:
        print("Error adding points!")
        return current_score

# purpose:Resets the score to 0
# returns: 0
# Details prints a message confirming the reset
def reset_score():
    print("Score has been reset to 0")
    return 0

# purpose: Displays the current score
# Returns(int): current_score
# Args: current_score(int)
def display_total(current_score):
    print(f"Current total: {current_score}")
    return current_score

# Purpose: The main loop for the program that display a menu and handles user interaction

def main():
    # Initialize score
    total_score = 0
    while True:        
        # Display the menu
        print("1.Add Points")
        print("2.Reset Score")
        print("3.View Total")
        print("4.Exit")
        try:
            # Get user choice
            choice = int(input("\nChoose an option:"))
            if choice == 4:
                print("Thank you for using the Score Keeper!")
                break
            elif choice == 1:
                try:
                    points = int(input("Enter points to add:"))
                    total_score = add_score(points, total_score)
                except ValueError:
                    print("Invalid Input. Please enter a number! ")
            elif choice == 2:
                total_score = reset_score()
            elif choice == 3:
                total_score = display_total(total_score)
        except ValueError:
            print("Invalid Input. Please enter a number!")
    

# Program Entry Point
if __name__ == '__main__':
    main()
    