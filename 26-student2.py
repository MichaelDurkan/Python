class Student:
    def __init__(self, name, course, grade):
        self.name = name
        self.course = course
        self.grade = grade

    def on_honor_roll(self):
    # This is our object function which can get information based on the class data types and info contained within these
        if self.grade >= 3.5:
            return True
        else:
            return False
