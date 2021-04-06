# Inheritance allows us to take all of the functions from one class to use in another class

from chef import Chef
# This is our first class, contained in the "chef.py" file
from otherchef import OtherChef
# This is our second class, contained in the "otherchef.py" file

myChef = Chef()
myChef.make_chicken()

myOtherChef = OtherChef()
myOtherChef.make_salad()
# You can use the options in both the "otherchef.py" and the inherited options from "chef.py" to output
