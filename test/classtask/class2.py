#session2

# Numeric data type 
# - binary - 0b ---> 00010101
# - octal - 0o ---> 0-7 (8 in sum)
# - hexidecimal - 0x --> 16 --> 0-9 abcdf

#prints 21
# print(0b010101)

#convert 21 to binary
# print(bin(21))
# print(oct(21))
# print(hex(21))

# word1 = "Hello"
# word2 = "Word"

# combined = word1 + word2 
# print(word1 * 3)

##### Boolean 
# Boolean data types has only two options: true or false
# usage - if/else conditions 

# if 1==1:
#         print("It one")

# Operators
# <
# <=
# > 
# >=
# == - equal 
# != - not equal 

#print(10<5) --> false

# inp = int(input("Please provide a anumber: "))
# if inp < 10:
#     print ("The number is less than 10")
# elif inp == 10:
#     print("The number is equal to 10")
# else: 
#     print ("The number is bigger than 10")

####Class task 1

# take the word input (string)
# find the lenght of the word
# if the lenght is more than 10
#print ("That is a long word")
# else  
# print ("The word has {the lenght of the word} word")

# word = input("Please provide a word: ")
# lenght = len(word)
# if lenght > 10:
#     print ("That is long word")
# else:
#     print ( f"The word has {lenght} letters")

# indentations - part of th python syntax, backspace
# f string - gives ability to insert variable to your string

# Boolean operators
# not , and , or
# and | or --> combiens 2 or more booleans together
# if num < 10 and number > 0 (0-10)
# any false given to true would result false 
# and --> true and true == true 
#     --> true and false == false
#     --> false and false == false

# or will try to find true 
# or --> true and true == true 
#     --> true and false == true
#     --> false and false == false

# not - will turn boolean to opposite 
# not --> true --> false 
#     --> false --> true 


# (True and True or False or False) ---> True 
# (False and False or not True or True) --> True
# (not True or not False and True and not True) --> 
 


# num = 5
# if num < 10 and num > 0 and :
#     print ("Inside of is condition")
# else:
#     print ("Inside of else condition")


#### Class task2 
# Takes integer input
# CHecks if inter is positive ( If the number is negative , print : Hey give me positive number)
# Checks if the integer is even or odd ( even 22/2 | odd 21/2 )
# Print "The number is even or odd"
# example :
# num = 10
# Output: the number is even


num = int(input("Please, provide a number: "))

if num >= 0:
    if num % 2 == 0:
        print ("The number is Even")
    else:
        print ("The number is Odd")
else:
    print ("Hey, give me a positive number!!!")