#Added student search function
#Added student remove funtion
#Did better input validation and updated main

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"\nName: {self.name}")
        print(f"Age = {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_number, gpa):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.gpa = gpa
    
    def describe_student(self):
        super().describe()
        print(f"Roll Number = {self.roll_number}")
        print(f"GPA = {self.gpa}")

    def __str__(self):
        return f"{self.name} | Roll No: {self.roll_number} | GPA: {self.gpa}"

class Teacher(Person):
    def __init__(self, name, age, subject, teacher_id):
        super().__init__(name, age)
        self.subject = subject
        self.teacher_id = teacher_id
    
    def describe_teacher(self):
        super().describe()
        print(f"Subject = {self.subject}")
        print(f"Id = {self.teacher_id}")

    def __str__(self):
        return f"{self.name} | Subject: {self.subject}"

# ===============
# === Storage === 
# ===============
students_list = []
teachers_list = []

# ========================
# === Student Features ===
# ========================
def add_students():
    print("\n=== Add Student===")
    name = get_name("Enter name: ")
    age = get_int("Enter age: ")
    roll_number = get_int("Enter Roll no: ")
    for student in students_list:
        if student.roll_number == roll_number:
            print("Roll number already exists.")
            return
    gpa = get_float("Enter gpa: ")

    student = Student(name, age, roll_number, gpa)

    students_list.append(student)

    print(f"\n{student.name} added successfully!")

def show_students():
    print("\n=== Student List ===")
    if not students_list:
        print("No students added yet.")
        return

    for x in students_list:
        x.describe_student()

def remove_students():
    print("\n=== Remove Student ===")

    if not students_list:
        print("No students added yet.")
        return

    roll_number = get_int("Enter roll number to remove: ")

    removed = False

    for student in students_list:

        if student.roll_number == roll_number:

            students_list.remove(student)

            print(f"\n==== {student.name} removed successfully. ====")
            removed = True
            break

    if not removed:
        print("No student found with that roll number.")

def search_students():
    print("\n=== Search Student ===")

    if not students_list:
        print("No students added yet.")
        return

    roll_number = get_int("Enter roll number to search: ")

    found = False

    for student in students_list:

        if student.roll_number == roll_number:

            print("\n==== Student Found ====")
            student.describe_student()

            found = True
            break

    if not found:
        print("No student found with that roll number.")

# ========================
# === Teacher Features ===
# ========================
def add_teachers():
    print("\n=== Add Teacher===")
    name = get_name("Enter name: ")
    age = get_int("Enter age: ")
    subject = get_name("Enter subject: ")
    teacher_id = get_int("Enter teacher Id: ")  

    teacher = Teacher(name,age, subject, teacher_id)

    teachers_list.append(teacher)

    print(f"\n{teacher.name} added successfully!")

def show_teachers():
    print("\n=== Teacher List ===")
    if not teachers_list:
        print("No teachers added yet.")
        return

    for x in teachers_list:
        x.describe_teacher()

def remove_teachers():
    pass

def search_teachers():
    pass

# =================
# =Helper function=
# =================
def get_name(prompt):
    while True:
        value = input(prompt).strip()

        if not value:
            print("Name cannot be empty.")
            continue

        if not value.replace(" ", "").isalpha():
            print("Name should contain only letters.")
            continue

        return value.title()

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a positive number.")
        except ValueError:
            print("Invalid number.")

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Enter a positive number.")
        except ValueError:
            print("Invalid number.")

def get_choice(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <=8:
                return value
            print("Enter a number between 1-8.")
        except ValueError:
            print("Invalid number.")
# ================
# ==Main Program==
# ================
def main():
    while True:
        print("\n==== School Management System ====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Show Students list")
        print("5. Add Teacher")
        print("6. Remove Teacher")
        print("7. Search Teacher")
        print("4. Show Teachers list")
        print("8. Exit")

        choice = get_choice("\nEnter your choice: ")

        if choice == 1:
            add_students()
        elif choice == 2:
            remove_students()
        elif choice == 3:
            search_students()
        elif choice == 4:
            show_students()
        elif choice == 5:
            add_teachers()
        elif choice == 6:
            search_teachers()
        elif choice == 7:
            show_teachers()
        elif choice == 8:
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice!")
# =================           
# ===Run program===
# =================
if __name__ == "__main__":
    main()