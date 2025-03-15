# Task 2:
# Take an input and count the occurrences of each character.
# Input: programming
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

# get user's input 
# count the occurances of each character
# create an empty dictionary for store the output
# create a foor loop which will count each character
# add 1 to each character , use += operator for adding a value to a variable 
# display the dictionary


inp = input("Please enter any word here: ")
count = {}

for char in inp:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print (count)