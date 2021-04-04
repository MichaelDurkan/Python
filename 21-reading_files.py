# Reading from external files, such as txt or csv files

employee_file = open("employees.txt", "r")
# This command opens the employees.txt file in read mode (this is what the "r" stands for).
# This is stored in a variable called "employee_file"
# We can also use the following: "w" (write), "a" (append), "rw" (read/write)
# The file is in the same folder as our Python file, but we can also use a relative path

print(employee_file.readable())
# This checks if the file is readable (this only works with "r")

print(employee_file.read())
# This reads all of the information in the file and outputs it to the screen

print(employee_file.readline())
# This reads the first line in the file. If we copy this line of code to subsequent lines, it will print the next lines in the file

print(employee_file.readlines())
# This takes all of the lines in the file and puts them in a list. You can also refer to a specific line by using [] and referring to the index position
# We can also use a "for loop" to return this information

employee_file.close()
# Whenever we open a file, we always want to close it

