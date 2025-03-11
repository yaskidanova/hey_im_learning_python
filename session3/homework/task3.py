# Task 3: Factorial of a Number (use for loop)
# Input:
# Enter a number: 5

# Output:
# Factorial of 5 is 120

# The factorial of a number is the product of all positive integers less than or equal to that number. 
# For example, factorial of 5 (written as 5!) is 5 × 4 × 3 × 2 × 1 = 120.

# get user's input 

# We initialize a variable called factorial to 1. This is important because we'll be multiplying numbers together, 
# and starting with 0 would give us a result of 0 for any number.

# then for loop 
# use range(1, num + 1) to create a sequence from 1 up to and including the input number. 
# for example, if the user enters 5, this range would be [1, 2, 3, 4, 5].

# Inside the loop, we multiply our running factorial value by the current number in the sequence (i). 
# This builds up the factorial step by step.

num = int(input("Please provide a number: "))

factorial = 1
for i in range(1, num +1):
    factorial = factorial * i
print (f"Factorial of {num} is {factorial}")