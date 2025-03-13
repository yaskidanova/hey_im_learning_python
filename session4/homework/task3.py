# Task 3: Find the Longest Word in a List
# Ask the user to enter a list of words. Find and print the longest word from the list.
# Example:
# Enter words: Python Java JavaScript C  
# Longest word: JavaScript  


# get user's input

# convert input into a list 

# create an empty string for longest word

# check the lenght of each word by for loop 

# print the longest one 


words = input("Please, enter multiple words separated by spaces: ")
user_list = words.split()

longest_word = ""
max_lenght = 0

for word in user_list:
    if len(word) > max_lenght:
        longest_word = word 
        max_lenght = len(word)
print (f"The longest word is : {longest_word}")



# there is a function max() with key=len parameter
# When you use key=len, 
# Python applies the len() function to each item before comparing. So it's comparing the lengths, not the words themselves.

words = input("Please, enter multiple words separated by spaces: ")
user_list = words.split()
longest_word = max(user_list, key=len)
print (f"The longest word is: {longest_word}")