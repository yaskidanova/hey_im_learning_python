# Task 2: Character Type Identifier
# Ask the user to input a single character. Determine and print:
# "It's a digit" if the character is a number (0-9).
# "It's a letter" if the character is a letter (a-z, A-Z).
# "It's a special character" otherwise.


# get user's input , use 'int' 
# make conditions using identif. options --> isdigit, isalpha \n
# help us determine what type of characters are in a string



num = (input("Please prodive a single character: "))



if num.isdigit():
    print ("It is a digit")
elif num.isalpha():
    print ("It is a letter")
else:
    print ("It's a special character")



