# For loops allow us to loop over different collections of items, such as arrays, letters in a string, groups of numbers, ranges

# Below is using a for loop with a string
for letter in "Dublin Ireland":
# This defines a variable called "letter" and is saying for every letter in "Dublin Ireland", I want to do something
    print(letter)
    # This outputs every letter in the variable each time it loops


# Below is using a for loop with an array
friends = ["Alan", "Peter", "Jason"]
for friend in friends:
# This defines an array called "friends" and is saying for every element in "friends", I want to do something
    print(friend)
    # This outputs each element in the array each time it loops

# Below is using a for loop with an range
friends = ["Alan", "Peter", "Jason"]

for index in range(len(friends)):
# # This gets the length of the array for use as a range
    print(friends[index])
    # This outputs each element in the array each time it loops


# You can use all sorts of complex logic inside for loops. A common scenario is to do something different in different runs of the loop
for index in range(5):
# # This gets the length of the array for use as a range
    if index == 0:
        print("First run")
    else:
        print("subsequent runs")
    # This outputs each element in the array each time it loops
