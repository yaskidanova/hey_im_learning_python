# Task 4: Password Strength Checker
# Ask the user for a password input. Check and print:
# "Strong password" if the length is at least 8 characters and contains both letters and numbers.
# "Weak password" otherwise.

# get user's input
# make conditions if the password is strong using '.isdigit' and '.isalpha'
# DOESN'T WORK ((((
#

password = (input("Please provide your password here: "))

if (password.isdigit()) and (password.isalpha()) and (len(password) >= 8):
    print ("Cool! This is a strong password")
else:
    print ("Meh, this is a weak password")