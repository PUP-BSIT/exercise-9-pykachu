def print_menu():
    print("\n===== Student Violation System =====")
    print("1. List All")
    print("2. Add")
    print("3. Update")
    print("4. Delete")
    print("5. Search")
    print("6. Exit")

def list_all(student):
    if not student:
        print("No student records available.")
    else:
        for num, student in enumerate(student, 1):
            print(f"\nStudent #{num}:")
            for key, value in student.items():
                print(f"  {key}: {value}")    

def add_record(student):
    print("\nAdd a student violation record:")
    name = input("Student Name: ")
    student_id = int(input("Student ID: "))
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

    student.append(student_record)
    print("Violation record added successfully!")

def main():
    student_record = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")
        
        match choice:
            case '1':
                list_all(student_record)
            case '2':
                add_record(student_record)
            case '3':
                #TODO(Besa): Do update_record.
                update_record(student_record)
            case '4':
                #TODO(Maestre): Do delete_record.
                delete_record(student_record)
            case '5':
                #TODO(Salespara): Do search_student.
                search_student(student_record)
            case '6':
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")

main()