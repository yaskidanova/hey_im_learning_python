# Task 1: Number Comparison
# Write a program that takes two integer inputs and prints:
# "Both numbers are equal" if they are the same.
# "The first number is greater" if the first number is larger.
# "The second number is greater" if the second number is larger.

# get user's first input 
# get user's second input
# make conditions if numbes are equal , print "they are equal"
# add elif for second coditions 
# add else if both previous conditions are false 

num1 = int(input("Please provide number 1: "))
num2 = int(input("Please provide number 2: "))

if num1 == num2:
    print ("Both numbers are equal")
elif num1 > num2:
    print ("The first number is greater")
else:
    print ("The second number is greater")
