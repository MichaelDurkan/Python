# A return statement gets information from a function

def cube(num):
    num*num*num
# This creates a function called cube and a parameter called number. We then instruct the function to cube the number
print(cube(3))
# This passes the number 3 to the parameter. But when we run this, the word "None" nothing will be outputted on screen


def cube2(num):
    return num*num*num
# This creates a function called cube and a parameter called number. We then instruct the function to cube the number, and return it to the screen
print(cube2(3))
# This passes the number 3 to the parameter. Now when we run this, the value will be outputted to the screen

# Note - no additional code can be added to a function after a return statement - python will throw an error
