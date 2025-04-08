
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.attendance = 0
        self.subjects = {}
        
    def add_subject(self, subject, marks):
        if 0 <= marks <= 100:
            self.subjects[subject] = marks
        else:
            raise ValueError("Marks should be between 0 and 100")
            
    def set_attendance(self, attendance):
        if 0 <= attendance <= 100:
            self.attendance = attendance
        else:
            raise ValueError("Attendance should be between 0 and 100")
            
    def get_average_marks(self):
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)
        
    def check_eligibility(self):
        is_eligible = True
        reasons = []
        
        if self.attendance < 75:
            is_eligible = False
            reasons.append(f"Low attendance: {self.attendance}% (minimum required: 75%)")
            
        avg_marks = self.get_average_marks()
        if avg_marks < 60:
            is_eligible = False
            reasons.append(f"Low average marks: {avg_marks:.2f}% (minimum required: 60%)")
            
        failed_subjects = [subject for subject, marks in self.subjects.items() if marks < 50]
        if failed_subjects:
            is_eligible = False
            reasons.append(f"Failed subjects: {', '.join(failed_subjects)} (minimum required: 50%)")
            
        return is_eligible, reasons

def main():
    print("Student Exam Eligibility System")
    
    try:
        # Get student details
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        student = Student(name, roll_number)
        
        # Get attendance
        attendance = float(input("Enter attendance percentage (0-100): "))
        student.set_attendance(attendance)
        
        # Get subject marks
        num_subjects = int(input("Enter number of subjects: "))
        for i in range(num_subjects):
            subject = input(f"Enter subject {i+1} name: ")
            marks = float(input(f"Enter marks for {subject} (0-100): "))
            student.add_subject(subject, marks)
            
        print("\nEligibility Report")
        print(f"Student Name: {student.name}")
        print(f"Roll Number: {student.roll_number}")
        print(f"Attendance: {student.attendance}%")
        print(f"Average Marks: {student.get_average_marks():.2f}%")
        print("\nSubject-wise Marks:")
        for subject, marks in student.subjects.items():
            print(f"{subject}: {marks}%")
            
        eligible, reasons = student.check_eligibility()
        print("\nFinal Status:", "ELIGIBLE" if eligible else "NOT ELIGIBLE")
        
        if not eligible:
            print("\nReasons for Ineligibility:")
            for reason in reasons:
                print(f"- {reason}")
                
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()