# Task 5: Print a Word in a Pyramid Shape
# Input:
# Enter a word: CODE

# Output:
# C
# CO
# COD
# CODE

# get a user's input 
# make a loop with function rahge where:
# start - the first number 

word = input("Please provide any word here: ")

for i in range(1, len(word) +1):
    print(word[:i])