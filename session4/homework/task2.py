# Task 2: Remove Duplicates from a List
# Ask the user to enter multiple words separated by spaces. Store them in a list and remove duplicate words while maintaining the original order.
# Example:
# Enter words: apple banana apple cherry banana apple  
# Filtered List: ['apple', 'banana', 'cherry']


# get user's input

# convert input into a list 

# create a new empty list to store the new result 

# how to check if the input contains duplicate word? 
# compare the lenght of the original list with the length of the same list converted to a set 
# ?? duplicates = len(user_list) != len(set(user_list))

# remove duplicates from a list

# display the filtered list 

inp = input("Please, enter multiple words separated by spaces: ")
user_list = inp.split()

new_list = []

for item in user_list:
    if item not in new_list:
        new_list.append(item)
print (" ".join(new_list))