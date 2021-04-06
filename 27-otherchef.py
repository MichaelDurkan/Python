from chef import Chef
# This imports or inherits all functions from the "chef" class in our "chef" file to be used in this "otherchef" file
class OtherChef(Chef):
    def make_roast_beef(self):
        print("The chef makes Roast Beef")
