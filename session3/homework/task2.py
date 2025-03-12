# Task 2: Reverse a Word using for loop (please don’t reverse a string using word[::-1])
# Input:
# Enter a word: Python
# Output:
# Reversed Word: nohtyP

# get user's input 
# create an empty string reversed_word to store our result. 
# Without initializing this variable as an empty string first, \n
# we would encounter an error when we try to add characters to it in the line reversed_word += word[i]. \n
# his is because Python can't add a character to a variable that doesn't exist yet.
#
# make a loop which will go down until the first letter
# len(word) - 1: The last index of the word.
# -1: The stopping point (before index -1, which is out of range).
# -1: The step size (moving backward).
# Add each character to reversed_word
# word[i] - This is accessing a specific character from our original word using indexing. 
# The variable i is our loop counter that's moving backward through the word.




word = input("Please enter any word here: ")
reversed_word = ""

for i in range(len(word) - 1, -1, -1):  # Iterate backward
    reversed_word += word[i]

print("Reversed Word:", reversed_word)
