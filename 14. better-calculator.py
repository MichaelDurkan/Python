# This is going to create a calculator where we can take both number and operator (+, -, *, /) input

num1 = float(input("Enter first number: "))
op1 = input("Enter operator: ")
num2 = float(input("Enter first number: "))
# This creates our 3 variables

# Now we need to decide what operator we are going to use
if op1 == "+":
    print(num1 + num2)
elif op1 == "-":
    print(num1 - num2)
elif op1 == "/":
    print(num1 / num2)
elif op1 =="*":
    print(num1 * num2)
else:
    print("Invalid operator")

