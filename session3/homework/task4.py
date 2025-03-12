# Task 4: Password Verification (Limited Attempts)
# secret password = Python123
# Input:

# Enter the password: hello
# Wrong password. Try again.

# Enter the password: python
# Wrong password. Try again.

# Enter the password: Python123
# Access Granted!

# how to define a secret password?

inp = input("Please, provide your password here: ")

secret_password = "Python123"

for attempts in range(3):
    if inp != secret_password:
        inp = input("Hey, wrong password, try again: ")
    else:
        print("Access granted")