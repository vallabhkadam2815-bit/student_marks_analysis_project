

# ==========================================
# STUDENT MARKS MANAGEMENT SYSTEM
# Mini Project using Python
# ==========================================

import os

# Tuple: Subject names
SUBJECTS = ("Python", "Mathematics", "English",
            "Computer Science", "Physics")

# List: Stores all student records
students = []

FILE_NAME = "students.txt"


# Function to calculate grade
def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# Function to calculate total and percentage
def calculate_result(marks):

    total = sum(marks)
    percentage = total / len(SUBJECTS)
    grade = calculate_grade(percentage)

    return total, percentage, grade


# Function to save records into a file
def save_records():

    with open(FILE_NAME, "w") as file:

        for student in students:

            data = [
                student["roll"],
                student["name"],
                student["marks"]
            ]

            file.write(str(data) + "\n")

    print("\nRecords saved successfully!")


# Function to load records from file
def load_records():

    if not os.path.exists(FILE_NAME):
        return

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:
                if line.strip():
                    data = eval(line)

                    student = {
                        "roll": data[0],
                        "name": data[1],
                        "marks": data[2]
                    }

                    students.append(student)

    except (ValueError, SyntaxError, TypeError):
        print("Error reading student records.")


# Function to add a student
def add_student():

    print("\n--- ADD STUDENT ---")

    try:
        roll = int(input("Enter Roll Number: "))

        for student in students:
            if student["roll"] == roll:
                print("Roll number already exists!")
                return

        name = input("Enter Student Name: ").strip()

        if not name:
            print("Name cannot be empty!")
            return

        marks = []

        for subject in SUBJECTS:

            while True:
                try:
                    mark = float(
                        input(f"Enter marks in {subject}: ")
                    )

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

        student = {
            "roll": roll,
            "name": name,
            "marks": marks
        }

        students.append(student)

        save_records()

        print("Student added successfully!")

    except ValueError:
        print("Please enter a valid roll number.")


# Function to display all students
def display_students():

    print("\n--- STUDENT RECORDS ---")

    if not students:
        print("No student records found!")
        return

    for student in students:

        total, percentage, grade = calculate_result(
            student["marks"]
        )

        print("\nRoll Number:", student["roll"])
        print("Name:", student["name"])

        for i in range(len(SUBJECTS)):
            print(SUBJECTS[i], ":", student["marks"][i])

        print("Total Marks:", total, "/ 500")
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)


# Function to search for a student
def search_student():

    print("\n--- SEARCH STUDENT ---")

    try:
        roll = int(input("Enter Roll Number: "))

        for student in students:

            if student["roll"] == roll:

                total, percentage, grade = calculate_result(
                    student["marks"]
                )

                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Total:", total)
                print("Percentage:", round(percentage, 2), "%")
                print("Grade:", grade)

                return

        print("Student not found!")

    except ValueError:
        print("Invalid roll number!")


# Function to update student marks
def update_marks():

    print("\n--- UPDATE MARKS ---")

    try:
        roll = int(input("Enter Roll Number: "))

        for student in students:

            if student["roll"] == roll:

                print("Student:", student["name"])

                for i in range(len(SUBJECTS)):

                    while True:
                        try:
                            mark = float(
                                input(f"New marks in {SUBJECTS[i]}: ")
                            )

                            if 0 <= mark <= 100:
                                student["marks"][i] = mark
                                break
                            else:
                                print("Marks must be between 0 and 100.")

                        except ValueError:
                            print("Enter a valid number.")

                save_records()

                print("Marks updated successfully!")
                return

        print("Student not found!")

    except ValueError:
        print("Invalid roll number!")


# Function to delete student record
def delete_student():

    print("\n--- DELETE STUDENT ---")

    try:
        roll = int(input("Enter Roll Number: "))

        for student in students:

            if student["roll"] == roll:

                students.remove(student)

                save_records()

                print("Student deleted successfully!")
                return

        print("Student not found!")

    except ValueError:
        print("Invalid roll number!")


# Function to display class topper
def display_topper():

    print("\n--- CLASS TOPPER ---")

    if not students:
        print("No student records found!")
        return

    topper = max(
        students,
        key=lambda student: calculate_result(
            student["marks"]
        )[0]
    )

    total, percentage, grade = calculate_result(
        topper["marks"]
    )

    print("Name:", topper["name"])
    print("Roll Number:", topper["roll"])
    print("Total Marks:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)


# Main menu
def main():

    load_records()

    while True:

        print("\n================================")
        print(" STUDENT MARKS MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Display Class Topper")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_marks()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            display_topper()

        elif choice == "7":
            save_records()
            print("\nThank you for using the application!")
            break

        else:
            print("Invalid choice! Please try again.")


# Program execution
if __name__ == "__main__":
    main()
