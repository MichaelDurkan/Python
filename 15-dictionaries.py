# Dictionaries allows us to store infomation in "key value pairs". 
# When you need to refer to something in the dictionary, you refer to it by its key. 
# For example, the word "January" could be converted to "Jan"
# Keys can use strings or numbers

monthConvert = {
    "Jan": "January",
# "Jan" is the key, "January is the value". All keys in a dictionary need to be unique
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConvert["Nov"])
# This goes into the dictionary and references the key to return the value

print(monthConvert.get("Luv", "Key not found"))
# This goes into the dictionary and uses the get function to return the value. If the key does not exist, you can also pass in a default value to return if the key is not found
