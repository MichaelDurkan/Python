# If Statements scan help us make decisions based on conditions or input

is_male = False
# Creates a boolean variable

if is_male:
# This creates the "if" definition
    print("You are a male")
    # This is what will be outputted "if" the condition is true. If its not true, nothing will be outputted
else:
# We have now created an "else" condition "if" the above is not true
    print("You are not a male")
    # Now, this is what will be outputted "if" the condition is not true. 

# We can use the "and" or "or" operators with multiple variables to create complex if/else conditions
# This is an example of an "if/and" statement

is_male = False
is_tall = False
# Creates our boolean variables

if is_male and is_tall:
# This creates the "if/and" definition
    print("You are a male and you are tall")
    # This is what will be outputted "if" both the conditions is true. 
else:
    print("You are neither male nor tall")
    # Now, this is what will be outputted "if" the condition is not true. 

# This is an example of an "if/or" statement

is_male = True
is_tall = False
# Creates our boolean variables

if is_male or is_tall:
# This creates the "if/or" definition
    print("You are a male or tall or both")
    # This is what will be outputted "if" both the conditions is true. 
else:
    print("You are neither male nor tall")
    # Now, this is what will be outputted "if" the condition is not true. 


# We can also use "else if" or "elif" with the not" operator

is_male = True
is_tall = False
# Creates our boolean variables

if is_male and is_tall:
    print("You are a tall male")

elif is_male and not(is_tall):
    # The "not" operator negates what is in the brackets
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a tall female")
else:
    print("You are either female or not tall or both")
