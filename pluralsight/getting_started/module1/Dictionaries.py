student = {
    "name": "Mark",
    "Student_id" : 15163,
    "feedback": None
}
all_students = [
    {"name": "Mark", "Student_id" : 15163},
    {"name": "Katarina", "Student_id" : 54732},
    {"name": "Jessica", "Student_id" : 13255}

]

student["name"] == "Mark"
student.keys() ==['name', 'Student_id', 'feedback']
student.values() == ['Mark', 15163, None]
all_students[2].values() == ['Jessica', 13255]
student["name"] = "James"
del student["name"]