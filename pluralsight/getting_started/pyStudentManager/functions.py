students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}  # declare new dictionary
    students.append(student)


def save_file(student):
    try:
        f = open("student.txt", "a") # access mode a does not require the file to be already exsisting
        f.write(student + "\n")
        f.close()
    except Exception as error:
        print("Could not save file")
        print(error)


def read_file():
    try:
        f = open("student.txt", "r") # access mode r does  require the file to be already exsisting; but is handled with the exception
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception as error:
        print("Could not read file")
        print(error)

read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student id: ")

add_student(student_name, student_id)
save_file(student_name)
