# Task 4: Reverse a String
# Ask the user to enter a word and print it in reverse. (Hint: Use slicing)

# get user's input 
#The slice notation in Python has the form [start:stop:step]:
# start: The starting index of the slice (inclusive)
# stop: The ending index of the slice (exclusive)
# step: The step or stride between elements
# reverse using [] and ::-1 --> empty than empty and move back 
# print both options

word = input("Please enter any word: ")
reverse = word[::-1]

print(word)
print(reverse)