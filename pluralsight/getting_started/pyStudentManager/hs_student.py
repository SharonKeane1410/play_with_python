from play_with_python.pluralsight.getting_started.pyStudentManager.student import Student


class HighSchoolStudent(Student):
    # overwrite attributes from parent class
    school_name = "Springfield High School"

    def get_school_name(self):
        return "This is a High School Student from " + self.school_name

    def get_name_capitalised(self):
        original_value = super().get_name_capitalised()
        return original_value + "-HS"
