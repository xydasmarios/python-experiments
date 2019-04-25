students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(title, name, student_id=332):
    student = {"title": title, "name": name, "student_id": student_id}

def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readline():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")

read_file()
print_students_titlecase()

while True:
    a = input("Enterrrrrrrrrr yes/no to continue: ")
    if a == "yes":
        student_title = input("Enter student title: ")
        student_name = input("Enter student name: ")
        student_id = input('Enter student id: ')
        add_student(student_title, student_name, student_id)
        print_students_titlecase()
        continue
    elif a == "no":
        break
    else:
        print("Enter either yes or no: ")

add_student(student_name, student_id)
save_file(student_name)
