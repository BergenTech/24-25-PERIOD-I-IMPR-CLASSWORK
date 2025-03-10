import datetime
# Function to record a student's attendance status for today
def record_attendance(student_name=None, present=True):
    # Get the data as #YYYY-MM-DD
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    # print(today)
    with open("attendance.txt", "a") as file:
        status = "Present" if present else "Absent"
        file.write(f"{today}, {student_name}, {status}\n")
    print(f"Recorded {student_name} as {status} on {today}")
 
#Display formatted attendance records from the file 
def display_attendance():
    try:
        with open("attendance.txt", "r") as file:
            print("\nAttendance Records")
            print("=" * 50)
            print(f"{'Date':<12} {'Student Name':<25} {'Status':<10}")
            print("=" * 50)
            for line in file:
                date, name, status = line.strip().split(",")
                print(f"{date:<12} {name:<25} {status:<10}")
            print("-" * 50)    
    except FileNotFoundError:
        print("No attendance records found! Please record attendance first")
if __name__ == "__main__":
    # record_attendance()
    # record_attendance("Ryan")
    display_attendance()