def student_menu():
    # Display student menu
    print("------------------------------------------")
    print("    Student Violation Management System   ")
    print("------------------------------------------")
    print("1. List All")
    print("2. Add")
    print("3. Update")
    print("4. Delete")
    print("5. Search")
    print("6. Exit")
    print("------------------------------------------")

def list_all_records(students):
    if not students:
        print("No student records available.")
    else:
        for num, student in enumerate(students, 1):
            print(f"\nStudent #{num}:")
            for key, value in student.items():
                print(f"{key}: {value}")

def add_record(students):
    print("\nAdd a student violation record:")
    name = input("Student Name: ")
    student_id = (input("Student ID: "))
    course_year = input("Course & Year: ")
    violation = input("Violation: ")
    date = input("Date of Violation (YYYY-MM-DD): ")

    student_record = {
        "Student Name": name,
        "Student ID": student_id,
        "Course & Year": course_year,
        "Violation": violation,
        "Date": date
    }

    students.append(student_record)
    print("Student record added successfully!")

def update_record(students):
    list_all_records(students)

    try: 
        record_id = int(input("\nEnter the student number to update: "))
        if 1 <= record_id <= len(students):
            print("Leave blank to keep current value.")

            for key in students[record_id - 1]:
                new_value = input(f"{key} ({students[record_id - 1][key]}): ")
                if new_value:
                    students[record_id - 1][key] = new_value

            print("Student record updated successfully!")
        else:
            print("No record found.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_record(student):
    list_all_records(student)

    try:
        idx = int(input("\nEnter the student number to delete: "))
        if 1 <= idx <= len(student):
            del student[idx - 1]
            print("Student record deleted successfully!")
        else:
            print("No student number/records found.")
    except ValueError:
        print("Please enter a valid number.")

def search_student(student): 
    keyword = input("\nEnter student number, name, "
                     "or violation to search: ").lower()
    found = False

    for idx, students in enumerate(student, 1):
        if (keyword in str(idx) or 
            keyword in students["Student Name"].lower() or
            keyword in students["Violation"].lower()):
            print("\n--- Record Found ---")
            print(f"Student #{idx}:")
            for key, value in students.items():
                print(f"{key}: {value}")
            found = True

    if not found:
        print("No matching record found.")

def main():
    student_record = []    

    while True:
        student_menu()
        choice = input("Enter your choice (1-6): ")
        
        match choice:
            case '1':
                list_all_records(student_record)
            case '2':
                add_record(student_record)
            case '3':
                update_record(student_record)
            case '4':
                delete_record(student_record)
            case '5':
                search_student(student_record)
            case '6':
                print("Program Terminated.")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")

main()