# Tuples are immutable. This means that they cannot be changed after they are created.
# The difference between lists and tuples is that lists are defined in square brackets, tuples are stored in reglar brackets. This is how Python identifies the differnce.

coordinates = (4, 5)
# This is our tuple called coordinates which has 2 values

print(coordinates[0])
# This outputs hte data in the specified index position to the screen

coordinates[1] = 10
print(coordinates[1])
# This throws the following error because we are trying to change the value:
#   File "c:\Python Course\tuples.py", line 9, in <module>
#   coordinates[1] = 10
#   TypeError: 'tuple' object does not support item assignment
