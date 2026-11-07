# Student Management System


import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_NAME = os.path.join(BASE_DIR, "students.json")

# Load student data from file
def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Student file could not be loaded.")
            return []

    return []


# Save student data to file
def save_students():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)

        print("Data saved successfully!")

    except OSError:
        print("Error: Unable to save data.")


# Calculate total and percentage
def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade


# Get valid marks
def get_marks():
    marks = []

    subjects = ["Python", "Mathematics", "OS","DSA","english"]

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter {subject} marks (0-100): "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    return marks


# Add new student
def add_student():
    print("\n========== ADD STUDENT ==========")

    while True:
        roll_no = input("Enter Roll Number: ").strip()

        if not roll_no:
            print("Roll number cannot be empty.")
        elif any(s["roll_no"] == roll_no for s in students):
            print("Roll number already exists!")
        else:
            break

    name = input("Enter Student Name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter Student Name: ").strip()

    age = get_valid_age()

    course = input("Enter Course: ").strip()

    while not course:
        print("Course cannot be empty.")
        course = input("Enter Course: ").strip()

    marks = get_marks()

    total, percentage, grade = calculate_result(marks)

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)
    save_students()

    print("\nStudent added successfully!")


# Validate age
def get_valid_age():
    while True:
        try:
            age = int(input("Enter Age: "))

            if 3 <= age <= 100:
                return age

            print("Please enter a valid age (3-100).")

        except ValueError:
            print("Invalid age! Enter a whole number.")


# Display one student
def display_student(student):
    print("\n--------------------------------")
    print("Roll Number :", student["roll_no"])
    print("Name        :", student["name"])
    print("Age         :", student["age"])
    print("Course      :", student["course"])

    print("Python      :", student["marks"][0])
    print("Mathematics :", student["marks"][1])
    print("OS     :", student["marks"][2])
    print("DSA     :", student["marks"][3])
    print("English     :", student["marks"][4])

    print("Total Marks :", student["total"], "/ ", len(student['marks']) * 100)
    print("Percentage  :", f'{student["percentage"]:.2f}%')
    print("Grade       :", student["grade"])
    print("--------------------------------")


# Display all students
def display_students():
    print("\n========== ALL STUDENTS ==========")

    if not students:
        print("No student records found.")
        return

    for student in students:
        display_student(student)


# Search student
def search_student():
    print("\n========== SEARCH STUDENT ==========")

    roll_no = input("Enter Roll Number to Search: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            display_student(student)
            return

    print("Student not found!")


# Delete student
def delete_student():
    print("\n========== DELETE STUDENT ==========")

    roll_no = input("Enter Roll Number to Delete: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:

            print("\nStudent Details:")
            display_student(student)

            confirm = input("Are you sure? (yes/no): ").strip().lower()

            if confirm == "yes":
                students.remove(student)
                save_students()
                print("Student deleted successfully!")
            else:
                print("Delete operation cancelled.")

            return

    print("Student not found!")


# Main menu
def main():

    while True:
        print("\n")
        print("===================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("===================================")

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        print("===================================")

        try:
            choice = int(input("Enter Your Choice (1-5): "))

            if choice == 1:
                add_student()

            elif choice == 2:
                display_students()

            elif choice == 3:
                search_student()

            elif choice == 4:
                delete_student()

            elif choice == 5:
                print("\nThank you for using Student Management System!")
                break

            else:
                print("Invalid choice! Please select 1-5.")

        except ValueError:
            print("Invalid input! Please enter a number.")


# Program execution
students = load_students()

if __name__ == "__main__":
    main()
