# Task 1: Count Down from input number to 1

# get user's input 
# count down until 1 using for loop 
# Create a sequence of numbers starting from num, going down to (but not including) 0, 
# decreasing by 1 each time (-1 parameter)

num = int(input("Provide number here: "))

if num > 0:
    for i in range(num, 0, -1):
        print(i)
else:
    print("Please, provide a positive number")