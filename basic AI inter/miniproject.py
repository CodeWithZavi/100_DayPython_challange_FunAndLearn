# ------------- Student Class (OOP) -------------
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Course: {self.course}"

def add_student(student_list):
    try:
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        student = Student(name, age, course)
        student_list.append(student)
        print("Student added successfully!\n")
    except ValueError:
        print("Invalid input! Age must be a number.\n")

def display_students(student_list):
    if not student_list:
        print("No students found.\n")
        return
    print("----- Student List -----")
    for s in student_list:
        print(s.info())
    print("------------------------\n")

def save_students(student_list, filename="students.txt"):
    with open(filename, "w") as file:
        for s in student_list:
            file.write(f"{s.name},{s.age},{s.course}\n")
    print("Students saved to file!\n")

def load_students(filename="students.txt"):
    student_list = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, age, course = line.strip().split(",")
                student_list.append(Student(name, int(age), course))
    except FileNotFoundError:
        print("No saved file found. Starting fresh.\n")
    return student_list

def main():
    students = load_students()
    
    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Save & Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            save_students(students)
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
