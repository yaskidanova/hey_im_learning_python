# Task 1: Reverse a List
# Write a program that reverses a list using a for loop.
# Example:
# # Input:
# Enter numbers separated by space: 1 2 3 4 5
# # Output:
# Reversed List: [5, 4, 3, 2, 1]


# get a user's input and covert it as a list. How to do this?
# input_string.split() - split the string

# create an empty list to store reversed elements

# make a for loop with range function 
# The range function takes three arguments: range(start, stop, step). 
# By starting at len(lst) - 1 (the last index), stopping at -1 (just before index 0), and using a step of -1 (moving backward), 
# we iterate through the list from end to beginning.

# using append() we will create a new list with reverse order

# to convert a list of strings into a single formatted string we need to use join() method

inp = input("Please, enter few numbers separated by space: ")
user_list = inp.split()

reversed_list = []

for i in range(len(user_list) -1, -1, -1):
    reversed_list.append(user_list[i])
print (" ".join(reversed_list)) # " " means the space between each element