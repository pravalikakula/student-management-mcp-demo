def add_student(students, name, marks):
    """Add a student's name and marks to the student list."""
    students.append({"name": name, "marks": marks})


def view_students(students):
    """Print all students and their marks."""
    if not students:
        print("No students have been added yet.")
        return

    print("\nStudents:")
    for number, student in enumerate(students, start=1):
        print(f"{number}. {student['name']} - {student['marks']:.2f} marks")


def calculate_average(students):
    """Return the average marks, or None when there are no students."""
    if not students:
        return None

    total_marks = sum(student["marks"] for student in students)
    return total_marks / len(students)
