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

def main():
    student_record = [
        {'Name': 'Bench', 'Id': 10012, 'Course': 'BSIT', 
          'Violation': 'No ID', 'Date': 'January 10, 2025'}
    ]

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")
        
        match choice:
            case '1':
                list_all(student_record)
            case '2':
                #TODO(Serquina): Do add_record.
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