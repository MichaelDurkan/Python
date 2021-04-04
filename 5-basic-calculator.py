num1 = input("Enter a number ")
num2 = input("Enter another number ")
result = num1 + num2
# The above code is just going to create a long string. So if the users enters the numbers "5" and "11", 511 will be output on the screen
print(result)

num1 = input("Enter a number ")
num2 = input("Enter another number ")
result = int(num1) + int(num2)
# The "int" function is converting the strings entered to an integer. So it needs to be a whole number - if you use decimals it will give an error. This will add the numbers correctly and 16 will be output on the screen
print(result)

num1 = input("Enter a number ")
num2 = input("Enter another number ")
result = float(num1) + float(num2)
# The "float" function allows us to use numbers with decimals
print(result)
