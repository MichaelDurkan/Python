# Classes and Objects can make programs more organised and powerful
# Classes mean you can define your own data type, outside of the standard data types (strings, integers, lists, arrays)

# An object is an actual representation of a class (in this case, and object is an actual Student)

from student import Student
# This imports the "Student" class from the "student.py" file

student1 = Student("Jim", "Business", 3.1, False)
# This creates a student object called "student1" with these values. When we create this object, we are calling the "__init__" function that is created in the student.py file

print(student1.name)
# This outputs the name of student1
