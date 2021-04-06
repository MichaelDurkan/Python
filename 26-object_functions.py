# A class function can be used inside a class to modify or give specific information about the class

from student2 import Student

student1 = Student("Mike", "Business", 3.1)
student2 = Student("Laura", "Business", 3.8)

print(student2.on_honor_roll())
# This uses the "on_honor_roll" class function to get the grade info and return either True/False
