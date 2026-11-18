students = []

def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"

def add_student():
    # Validate student name (cannot be empty)
    while True:
        name = input("Enter student name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please try again.")

    # Validate student mark (must be a number between 0 and 100)
    while True:
        raw_mark = input("Enter mark (0-100): ").strip()
        try:
            mark = float(raw_mark)
            if 0 <= mark <= 100:
                # Convert whole numbers like 92.0 to 92 for clean display
                if mark.is_integer():
                    mark = int(mark)
                break
            else:
                print("Invalid mark. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    grade = get_grade(mark)
    students.append({
        "name": name,
        "mark": mark,
        "grade": grade
    })
    print(f"Added {name} (Mark: {mark}, Grade: {grade}).\n")

def show_results():
    if not students:
        print("No students added yet. Add a student first.\n")
        return

    print("\n" + f"{'Name':<15} {'Mark':<8} {'Grade':<5}")
    print("-" * 30)

    marks = []
    for student in students:
        print(f"{student['name']:<15} {student['mark']:<8} {student['grade']:<5}")
        marks.append(student["mark"])

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("-" * 30)
    print(f"Average: {average:.1f}")
    print(f"Highest: {highest}  Lowest: {lowest}\n")

def main():
    while True:
        print("--- Student Grade Manager ---")
        print("1. Add student")
        print("2. Show results")
        print("3. Quit")

        choice = input("Choose an option (1/2/3): ").strip().lower()

        if choice in ("1", "add"):
            add_student()
        elif choice in ("2", "show"):
            show_results()
        elif choice in ("3", "quit", "exit"):
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()