students = []


def read_file():
    try:
        f = open("../pyStudentManager/student.txt",
                 "r")  # access mode r does require the file to be already existing; but is handled with the exception
        for student in read_student(f):
            students.append(student)
        f.close()
    except Exception as error:
        print("Could not read file")
        print(error)


def read_student(f):
    for line in f:
        yield line


read_file()
print(students)
