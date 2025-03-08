# Task 3: Three-Number Maximum
# Take three integer inputs and print the largest one using only if-elif-else conditions.

# get 3 user's inputs 
# compare num1 and num 2 using if anf elif, than else for num3

num1 = int(input("Please provide number 1: "))
num2 = int(input("Please provide number 2: "))
num3 = int(input("Please provide number 3: "))

if (num1 >= num2) and (num1 >= num3):
    print("The largest one is", num1)
elif (num2 >= num1) and (num2 >= num3):
    print("The largest one is", num2)
else:
    print("The largest one is", num3) 


