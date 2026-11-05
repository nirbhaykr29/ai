class Student:

    # Constructor
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    # Calculate Result
    def calculate_result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

    # Display Student Details
    def display(self):
        print("\n===== STUDENT RESULT =====")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print("Result:", self.calculate_result())


# Take User Input
name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
marks = float(input("Enter marks: "))

# Create Student Object
student1 = Student(name, roll_number, marks)

# Display Result
student1.display()