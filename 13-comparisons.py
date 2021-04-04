# Comparisons use if statements within functions to return the requested values based on input

def max_num(num1, num2, num3):
# We create our function "max_num" with 3 parameters
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    # Above if/elif/else statements based on the parameters and use comparison operators (eg ">="")

print(max_num(608,427,579))

    

