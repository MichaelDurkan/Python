# Writing or appending to external files, such as txt or csv files

employee_file = open("employees.txt", "a")
# We are adding some text to the end of the file
# Using "w" or write overwrites the entire contents of the existing file
employee_file.write("\nKelly - Accountant")
# This adds a new line and then adds "Kelly - Accountant"
employee_file.close()
