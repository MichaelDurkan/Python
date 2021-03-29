# A function is a collection of code that creates a specific task

def hello():
    # Creates a function called hello. The brackets and colon indicates that all code is now part of the function
    print("Hello Michael")

hello()
# This calls the function and executes it

def hello(name):
    # Creates a function called hello. The brackets and colon indicates that all code is now part of the function. We also define a parameter called "name"
    print("Hello " + name)

hello("George")
# This calls the function and executes it, and  also passes in a value to the parameter

def hello(name, age):
    # We can also define multiple parameters
    print("Hello " + name, ", you are " + str(age))

hello("George", 43)
# This calls the function and executes it, and  also passes in the values to both parameters
