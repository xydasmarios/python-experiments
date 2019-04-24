# print("Hello")
#
#
# def add_mumbers(a, b);
#
#
# print(a + b)
# add_mumbers(5, 11)
#
#
# def add_number(a: int, b: int);
#
#
# print(a + b)
# add_mumbers(5, 11)
#
# answer = 42
# pi = 3.1
# answer + pi = 45.1
#
# int(pi) == 3
# float(answer) == 3.1
#
# "Hello".replace("e", "a")
#
# name = "Marios"
# machine = "HALO"
# "Nice to meet you {0}. I am {1}".format(name, machine)
# f"Nice to meet you {name}. I am {machine}"
#
# number = 5
#
# if number == 5:
#     print("x")
# else:
#     print("xx")
#
# number = 5
#
# if number != 5:
#     print("x")
#
#     python_course = True
#     if not python_course:
#         print("xx")
#
# number = 3
# python_course = True
#
# if number == 3 and python_course:
#     print("xx")
#
# if number == 3 or python_course:
#     print("xxx")
#
# student_names = ["xx", "xxx"]
#
# student_names[0] == "xx"
#
# student_names = ["x", "xx"]
# student_names[3] = "xxx"
# student_names.append("xxx")
# student_names == ["x", "xx", "xxx"]
#
# -------------------------------------------
#
# student_names = ["x", "xx"]
# print(student_names[0])
#
# student_names = ["x", "xx"]
# for x in student_names:
#     print("hello {0}".format(x))
#
# for name in student_names:
#     print("hello {0}".format(name))
#
# x = 0
# for i in range(10):
#     x += 10
#     print("the values of x is {0}".format(x))
#
# -------------------------------------------
# --list
# student_names = ["marios", "ian", "bran"]
# for name in student_names:
#     if name == "ian":
#         break
#         --stops
#         print("found him " + name)
#     else:
#         print("testing " + name)
#
# student_names = ["marios", "ian", "bran"]
# for name in student_names:
#     if name == "ian":
#         continue
#         --exclude
#         print("found him " + name)
#     else:
#         print("testing " + name)
#
# num = 10
# while True:
#     if num == 2:
#         --
#         break
#         infinitive
#         loop
#     print("hello")
#
# ----------------------------------------------
# --dictionaries
# student = {
#     "name": "Mark",
#     "id": 1222,
#     "feedback": None
# }
#
# all_students = [
#     {"name": "Mark", "student_id": 1111},
#     {"name": "Xydas", "student_id": 2222}
# ]
#
# ---------------------------------------------
#
# --exceptions
# student = {
#     "name": "Mark",
#     "id": 1111
# }
# student["last_name"] = "Kolinski"
# try:
#     last_name = student["last_name"]
#     xxx = 3 + last_name
# except KeyError:
#     print("error")
# except TypeError:
#     print("i cant add these two together")
# except TypeError as error:
#     print("2 i cant add these two together")
#     print(error)
# except Exception:
#     print("Unknown")
#
# --------------------------------------
#
# print("hello")
# str(3) == "3"
# int("15") == 15
# username = input("enter the users name: ")
#
# ---------------------------------------------
# --functions
#
#
# def hello():
#     name = str(input("Enter your name: "))
#     if name:
#         print("Hello" + str(name))
#     return
#
#
# hello()
#
# ---------------------------------------------
#
# students = []
#
#
# def add_student(name, student_id=332):
#     student = {"name": name, "student_id": student_id}
#     students.append(name)
#
#
# def var_args(name, *args):
#     print(name)
#     print(args)
#
#
# add_student(name="Mark", student_id=15)
#
# var_args("Mark", "world", None, "something", True)
#
# --
#
# students = []
#
#
# def add_student(name, student_id=332):
#     student = {"name": name, "student_id": student_id}
#     students.append(name)
#
#
# def var_args(name, **kwargs):
#     print(name)
#     print(kwargs["description"], kwargs["feedback"])
#
#
# add_student(name="Mark", student_id=15)
#
# var_args("Mark", description="world", feedback=None, subscribe=True)
#
# --------------------------------------
#
# students = []
#
#
# def get_students_titlecase():
#     students_titlecase = []
#     for student in students:
#         students_titlecase = student.title()
#     return students_titlecase
#
#
# def print_students_titlecase():
#     students_titlecase = get_students_titlecase()
#     print(students_titlecase)
#
#
# def add_student(name, student_id=332):
#     student = {"name": name, "student_id": student_id}
#     students.append(name)
#
#
# def var_args(name, **kwargs):
#     print(name)
#     print(kwargs["description"], kwargs["feedback"])
#
#
# student_list = get_students_titlecase()
#
# add_student(name="Mark", student_id=15)
#
# var_args("Mark", description="world", feedback=None, subscribe=True)
#
# ------------
#
# students = []
#
#
# def get_students_titlecase():
#     students_titlecase = []
#     for student in students:
#         students_titlecase = student.title()
#     return students_titlecase
#
#
# def print_students_titlecase() -> object:
#     students_titlecase = get_students_titlecase()
#     print(students_titlecase)
#
#
# def add_student(title, name, student_id=332):
#     student = {"title": title, "name": name, "student_id": student_id}
#     students.append(name)
#
#
# student_list = get_students_titlecase()
#
# while True:
#     a = input("Enter yes/no to continue: ")
#     if a == "yes":
#         student_title = input("Enter student title: ")
#         student_name = input("Enter student name: ")
#         student_id = input('Enter student id: ')
#         add_student(student_title, student_name, student_id)
#         print_students_titlecase()
#         continue
#     elif a == "no":
#         break
#     else:
#         print("Enter either yes or no: ")
#
# ----------------------------------------------------------------
#
# students = []
#
#
# def get_students_titlecase():
#     students_titlecase = []
#     for student in students:
#         students_titlecase.append(student["name"].title())
#     return students_titlecase
#
#
# def print_students_titlecase():
#     students_titlecase = get_students_titlecase()
#     print(students_titlecase)
#
#
# def add_student(title, name, student_id=332):
#     student = {"title": title, "name": name, "student_id": student_id}
#
#
# def save_file(student):
#     try:
#         f = open("students.txt", "a")
#         f.write(student + "\n")
#         f.close()
#     except Exception:
#         print("Could not save file")
#
#
# def read_file():
#     try:
#         f = open("students.txt", "r")
#         for student in f.readline():
#             add_student(student)
#         f.close()
#     except Exception:
#         print("Could not read file")
#
#
# read_file()
# print_students_titlecase()
#
# while True:
#     a = input("Enter yes/no to continue: ")
#     if a == "yes":
#         student_title = input("Enter student title: ")
#         student_name = input("Enter student name: ")
#         student_id = input('Enter student id: ')
#         add_student(student_title, student_name, student_id)
#         print_students_titlecase()
#         continue
#     elif a == "no":
#         break
#     else:
#         print("Enter either yes or no: ")
#
# add_student(student_name, student_id)
# save_file(student_name)
#
# ----------------------------------------------
#
# students = []
#
#
# def get_students_titlecase():
#     students_titlecase = []
#     for student in students:
#         students_titlecase.append(student["name"].title())
#     return students_titlecase
#
#
# def print_students_titlecase():
#     students_titlecase = get_students_titlecase()
#     print(students_titlecase)
#
#
# def add_student(title, name, student_id=332):
#     student = {"title": title, "name": name, "student_id": student_id}
#
#
# def save_file(student):
#     try:
#         f = open("students.txt", "a")
#         f.write(student + "\n")
#         f.close()
#     except Exception:
#         print("Could not save file")
#
#
# def read_file():
#     try:
#         f = open("students.txt", "r")
#         for student in read_students(f):
#             students.append(student)
#         f.close()
#     except Exception:
#         print("Could not read file")
#
#
# def read_students(f):
#     for line in f:
#         yield line
#
#
# read_file()
# print(students)
#
# while True:
#     a = input("Enter yes/no to continue: ")
#     if a == "yes":
#         student_title = input("Enter student title: ")
#         student_name = input("Enter student name: ")
#         student_id = input('Enter student id: ')
#         add_student(student_title, student_name, student_id)
#         print_students_titlecase()
#         continue
#     elif a == "no":
#         break
#     else:
#         print("Enter either yes or no: ")
#
# add_student(student_name, student_id)
# save_file(student_name)
#
# ---------------------------------------
#
# x = 5
# y = x * 2
#
#
# def double(x):
#     return y
#
#
# print("result {0}".format(y))
#
# x = 5
# y = x * 2
# double = lambda x: x * y
# print("result {0}".format(y))
#
# --------------------------------------
#
# students = []
#
#
# class Student:
#     def add_student(self, name, student_id=332):
#         student = {"name": name, "student_id": student_id}
#         students.append(student)
#
#
# student = Student()
# student.add_student("Mark")
#
# print(students)
#
# --
#
# students = []
#
#
# class Student:
#     def __init__(self, name, student_id=332):
#         student = {"name": name, "student_id": student_id}
#         students.append(student)
#
#     def __str__(self):
#         return "Student"
#
#
# mark = Student("Mark")
#
# print(mark)
#
# ------------------------------------
#
# students = []
#
#
# class Student:
#     school_name = "Elementary"
#
#     def __init__(self, name, student_id=332):
#         student = {"name": name, "student_id": student_id}
#         students.append(student)
#
#     def __str__(self):
#         return "Student"
#
#     def get_name_capitalize(self):
#         return self.name_capitalize()
#
#     def get_school_name(self):
#         return self.school_name
#
#
# # mark = Student("Mark")
# # print(mark)
#
# print(Student.school_name)
#
# -----
#
# students = []
#
#
# class Student:
#     school_name = "Elementary"
#
#     def __init__(self, name, student_id=332):
#         self.name = name
#         self.student_id = student_id
#         students.append(self)
#
#     def __str__(self):
#         return "Student" + self.name
#
#     def get_name_capitalize(self):
#         return self.name.capitalize()
#
#     def get_school_name(self):
#         return self.school_name
#
#
# class HighSchoolStudent(Student):
#     school_name = "High School"
#
#     def get_school_name(self):
#         return "This is a high school student"
#
#     def get_name_capitalize(self):
#         original_value = super().get_name_capitalize()
#         return original_value + "--HS"
#
#
# james = HighSchoolStudent("james")
# print(james.get_name_capitalize())
