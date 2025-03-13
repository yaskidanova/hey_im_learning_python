# Task 4: Find the Second Largest Number in a List (No max() or sort())
# Ask the user to enter a list of numbers. Find and print the second largest number without using max() or sort().
# Example:
# Enter numbers: 10 45 78 23 89 56  
# Second largest number: 78


# The heapq.nlargest() function provides a simple and efficient way to find the largest elements in a list. 
# We can use it to find the two largest numbers and access the second largest directly.

# Need to import heapq 
# get user's input
# convert input into a list 
# define top_two numbers by heapq.nlargest() option
# display the second largest


import heapq

numbers = input("Please, enter at least 2 numbers separated by spaces here: ")
user_list = numbers.split()

top_two = heapq.nlargest(2, user_list)      # finding 2 largest in a list

print(top_two[1])   # display the second element 