# 2D lists are useful for creating groups of numbers and items in list format

number_grid = [
# This is creating our number grid
    [1, 2, 3],
    # This is list one, which has index 0, and inside this the 3 numbers are at position 0, 1, 2
    [4, 5, 6],
    # This is list two, which has index 1, and inside this the 3 numbers are at position 0, 1, 2
    [7, 8, 9],
    # This is list three, which has index 2, and inside this the 3 numbers are at position 0, 1, 2
    [0]
    # This is list one, which has index 0, and inside this the number is at position 0
]

print(number_grid[2][0])
# So here, we are asking to output index 2, position 0 for the number grid, This should return 7


for row in number_grid:
    print(row)
# This is going to print out the entire grid

for row in number_grid:
    for col in row:
        print(col)
# This is going to print out the entire grid in a list format
