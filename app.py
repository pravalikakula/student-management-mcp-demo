from students import add_student, calculate_average, view_students


def main():
    students = []

    while True:
        print("\nStudent Management Menu")
        print("1. Add a student")
        print("2. View students")
        print("3. Calculate average marks")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

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
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option from 1 to 4.")


if __name__ == "__main__":
    main()
