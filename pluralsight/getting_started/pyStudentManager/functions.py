students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}    # declare new dictionary
    students.append(student)

#keyword arguments denoted with **
def var_agrs(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])
    print(kwargs)


student_list = get_students_titlecase()

add_student(name="Mark", student_id=5)

var_agrs("Mark", description="Loves Py", feedback=None, pluralsight_subscriber=True)