# Task 3
# Take an input of list of numbers, find and print the unique numbers.
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: 1, 3, 5


# get user's input 
# covert inout to a list
# defone unique_num using set function
# display output

inp = input("Please enter any numbers here: ").split()

unique_num = set(inp)

print(" ".join(unique_num))