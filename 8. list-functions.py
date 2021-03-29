lottery_numbers = [4, 7 ,14, 19, 22, 37]
names = ["Bill", "George", "John", "Paul", "Eric"]
# Creates 2 lists with numbers and names

print(names)
# This will print both lists

names.append("Tony")
print(names)
# Appends a name onto the end of a list and outputs to the screen

names.insert(1, "Laura")
print(names)
# Inserts the name Laura into index position 1 and pushes the remaining elements in the list over

names.remove("George")
print(names)
# Removes George from the list

print(names.index("Paul"))
# Finds the index position for Paul on the list

print(names.count("John"))
# Counts the number of times that John appears on the list

names.sort()
print(names)
# Sorts the list either alpahbetically or numerically

names.reverse()
print(names)
# Sorts the list either alpahbetically or numerically in reverse order

names2 = names.copy()
print(names2)
# Copies all contents of an existing list to another

names.extend(lottery_numbers)
# Appends one list onto the end of another

names.clear
print(names)
# Removes all elements from the list
