# Agenda

# - dictionaries --> task based

# - touch functions

students = {
    "101": {
        "name": "Alice Johnson",
        "age": 20,
        "grade": "A",
        "courses": ["Math", "Physics", "Computer Science"],
        "attendance": 95
    },
    "102": {
        "name": "Bob Smith",
        "age": 21,
        "grade": "B",
        "courses": ["History", "Literature", "Political Science"],
        "attendance": 88
    },
    "103": {
        "name": "Charlie Brown",
        "age": 19,
        "grade": "A-",
        "courses": ["Biology", "Chemistry", "Physics"],
        "attendance": 92
    },
    "104": {
        "name": "Diana Adams",
        "age": 22,
        "grade": "C+",
        "courses": ["Economics", "Statistics", "Business"],
        "attendance": 80
    },
    "105": {
        "name": "Ethan Green",
        "age": 20,
        "grade": "B+",
        "courses": ["Computer Science", "Mathematics"],
        "attendance": 90
    }
}

# task1 print the user id and print the name of the student in the following format
# 101: Alise Johnson 

# for key, value in students.items():
#     print (f"{key}: {value['name']}")

#  task 2
#  print only stodents that grades are A (-A, A)

# for key, value in students.items():
#     if 'A' in value['grade']:     #if you want print only print A , use if 'A' == value 
#         print (f"{key}: {value['name']}")


# task 3
# Ask user for an input of course
# Print the studets that are taking this course
# Input: Computer Science
# Output:
# 101: Alice Johnson
# 105: Ethan Green

# inp = input("Please, choose one of the course: ").lower()


# for key, value in students.items():
#     for elem in value ['courses']:
#         if inp == elem.lower():
#             print (f"{key}: {value['name']}")    
    
# Functions - small chunk of repeatable code which can call multiple times in your program
# DRY - Do not repear yourself 

#  How to create?

# def <function_name> ():
    # code

# def helloWorld(inp_arg):
#     print("Hello World") 

# how we can take input to our function? --> argument in ()

# Task1 
# create a function that takes an integer input and prints if it's Odd or Even
# 

# def my_func (inp_arg):
#     if inp_arg % 2 == 0:
#         return ("This is even number")
#     else:
#         return ("This is odd number")

# print (my_func (4))

# my_func (4)
# my_func (5)

# What is the difference between print() and return 
# print() --> to output the values
# return --> only used in functions | the purpose is return outputs data type back

# create a function that takes a list of integers , return the list of even numbers only 

# def my_func(num):
#     even_lst = []
#     for i in num:
#         if i % 2 == 0:
#             even_lst.append(i)
#     return even_lst
        
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst2 = [45, 65, 223, 45, 46, 87]
# lst3 = [311, 71, 65, 87, 8, 54]

# print my_func(lst)
# print my_func(lst2)
# print my_func(lst3)

# index of character

def characterChecker(word, character):
    if character in word:
        return word.index(character)
    else:
        return "No such character"

print (characterChecker("akumosolutions", "g"))
print (characterChecker("akumosolutions", "o"))