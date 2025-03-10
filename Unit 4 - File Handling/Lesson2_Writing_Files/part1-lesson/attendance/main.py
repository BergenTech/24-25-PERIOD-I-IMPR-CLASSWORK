def attendance_tracker():
    print("Class Attendance Tracker")
    
    # Sample data
    students = [
        "Emma Smith",
        "Noah Johnson",
        "Olivia Williams",
        "Liam Brown",
        "Ava Jones"
    ]
    
    # Record attendance for each student
    record_attendance(students[0])  # Present
    record_attendance(students[1], False)  # Absent
    record_attendance(students[2])  # Present
    record_attendance(students[3])  # Present
    record_attendance(students[4], False)  # Absent
    
    print("Attendance recorded in attendance.txt")

if __name__ == '__main__':
    attendance_tracker()