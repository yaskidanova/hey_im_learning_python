# What is for loop?
# It is a way to iterate through collections of items. 
# It allows us to repeat a block of code for each item in a seqience (string, list, range of numbers)

# Basic syntax :
# for item in sequence:
# print(item)

# This loop will print output for each item 

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(f"I like {fruit}s")

# If you want to loop a specific number of times :

# for i in range(5):
#     print(f"Count: {i}")

# for num in range(1, 11):    #from 1 to 10
#     print(num)

# Loop control statements 

# for i in range (10):
#     if i == 3:
#         continue 
#     if i == 7:
#         break
#     print (i)


# y = 2 + 3 * 5
# print (y)



### Task 1: Simple Loop and Conditional

# Write a program that:

# - Starts with `count = 15`
# - Uses a while loop to decrease `count` by 3 each iteration
# - Prints `"*"` if `count` is even, `"#"` if `count` is odd
# - Stops when `count` is 0 or negative
# - Expected output: `# * # *`

# for i in range(15, 0, 3):
#     if i % 2 == 0:
#         print("*", end= "")
#     else:
#         print("#", end= "")


### Task 2: Nested Loops with Accumulation

# Write a program that:

# - Uses nested for loops with `i` in `range(3)` and `j` in `range(2)`
# - Adds 1 to a variable `total` (starting at 0) if `i + j` is greater than 2
# - Adds 2 to `total` otherwise
# - Prints the final value of `total`


# total = 0
# for i in range(3):
#     for j in range(2):
#         if i + j > 2:
#             total+=1
#         else:
#             total+=2
# print(total)



### Task 3: Dictionary and String Indexing

# Write a program that:

# - Defines a dictionary `items = {"apple": 0.5, "banana": 0.75, "cherry": 1.25}`
# - Loops through the keys of the dictionary
# - Prints the third character (index 2) of each key, without a newline
# - Expected output: `pne`


# items = {"apple": 0.5, "banana": 0.75, "cherry": 1.25}

# for key in items.keys():
#     print((key)[2], end="") 


