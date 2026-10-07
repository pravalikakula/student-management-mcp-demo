from students import (
    add_student,
    calculate_average,
    delete_student,
    search_students,
    update_student_marks,
    view_students,
)


def choose_student(students):
    """Find a student by name and ask which one to use if names are duplicated."""
    name = input("Enter the student's name: ").strip()
    matches = search_students(students, name)

    if not matches:
        print(f"No student found with the name '{name}'.")
        return None

    if len(matches) == 1:
        return matches[0]

    print("More than one student has that name:")
    view_students(matches)
    choice = input(f"Choose a student (1-{len(matches)}): ").strip()

    try:
        student_number = int(choice)
    except ValueError:
        print("Please enter a valid student number.")
        return None

    if student_number < 1 or student_number > len(matches):
        print("Please enter a valid student number.")
        return None

    return matches[student_number - 1]


def main():
    students = []

    while True:
        print("\nStudent Management Menu")
        print("1. Add a student")
        print("2. View students")
        print("3. Calculate average marks")
        print("4. Search for a student")
        print("5. Delete a student")
        print("6. Update student marks")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            name = input("Enter the student's name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue

            marks_text = input("Enter the student's marks: ").strip()
            try:
                marks = float(marks_text)
            except ValueError:
                print("Please enter marks as a number.")
                continue

            add_student(students, name, marks)
            print(f"Added {name}.")
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            average = calculate_average(students)
            if average is None:
                print("Add students first to calculate an average.")
            else:
                print(f"Average marks: {average:.2f}")
        elif choice == "4":
            student = choose_student(students)
            if student is not None:
                view_students([student])
        elif choice == "5":
            student = choose_student(students)
            if student is not None:
                delete_student(students, student)
                print(f"Deleted {student['name']}.")
        elif choice == "6":
            student = choose_student(students)
            if student is not None:
                marks_text = input("Enter the new marks: ").strip()
                try:
                    marks = float(marks_text)
                except ValueError:
                    print("Please enter marks as a number.")
                    continue

                update_student_marks(student, marks)
                print(f"Updated marks for {student['name']}.")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option from 1 to 7.")


if __name__ == "__main__":
    main()
