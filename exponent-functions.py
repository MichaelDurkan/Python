# Exponent functions alow us to raise numbers by power (so 2 to the power of 3 is 8)

print(2**3)
# This is the easy way, and will output 8 to the screen

def raise_to_power(base_num, pow_num):
# This creates a "raise_to_power" function
    result = 1
    # This is a variable
    for index in range(pow_num):
    # We'll loop through the for loop as many times as "pow_num"
        result = result * base_num
    return result

print(raise_to_power(3, 4))
# In this instance, 3 is "base_num", and 4 is "pow_num". So we are running 3***4 and will get 81 as the output
    
