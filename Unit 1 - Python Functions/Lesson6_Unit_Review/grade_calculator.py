def calculate_final_grade(test_score, attendance_percent):
    try:
        # if test_score < 0 or test_score >100:
        if not (0<= test_score <=100):
            raise ValueError("Test score must be between 0-100!")
        if not (0<= attendance_percent <=100):
            raise ValueError("Attendance must be between 0-100!")
        #Weight 80% test score. 20% attendance
        final_grade = (test_score *0.8) + (attendance_percent*0.2)
        return f"Final Grade: {final_grade:.1f}"
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"
    
def test_grade_calculator():
    print("Testing grade calculator!")
    print(calculate_final_grade(85,90))
    print(calculate_final_grade(-90,80))
    print(calculate_final_grade(85,150))
    
if __name__ == "__main__":
    test_grade_calculator()