# Task 3: Simple Calculator
# Create a calculator that takes two numbers and an operator (+, -, *, /, //, %, **) 
# as input and performs the appropriate calculation.

# get a user's input number 1 , i'm using 'float' in case if user'll provide decimal number
# get the user's input number 2
# get the user's input about operator 
# the 'f' and curly braces tell python to replace variable values and procces it 
# 'eval' convert string as operator 
 

num1 = float(input("Please provide number 1: "))
num2 = float(input("Please provide number 2: "))
operator = input("Please provide an operator +, -, *, /, //, %, **: ")

answer = f"{num1} {operator} {num2}"
print(eval(answer))

