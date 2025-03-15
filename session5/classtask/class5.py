# Agenda
# learn List index(), split()
# list comprehensions
# tuples
# difference between mutable and immutable data types
# intro to dictionaries 

# index() --> finds element's index
# lst = ["Hello", 10, 1, True]

# print (lst.index(True))


# list comprehensions --> generate a list of elements using single line
# lst = []
# for num in range(1, 11):
#     if num % 2 == 0:
#         lst.append(num)
# print(lst)


# variable = [elelment | for element in siquense]
# lst_num = [i for i in range(1, 21)]
# print (lst_num)

# "aKumoSolutions" --> ['a', 'k'..... 's']
# lst = [char for char in range(1, 11)]
# print(lst_num)

# classtask
# crate a list of square number from 1 - 10 (num * num) using list comprehension
# output [0, 1, 4, 9, 16, 25, 36, 49, 64, 82, 100]

# for num in range(1, 11):
#     print (num*num)

# lst = [num*num for num in range(1, 11)]
# print (lst)


## Mutible and immutable data types

# mutable --> mutate , data type that constantly changes --> append, sort, remove etc.
# string --> immutable --> string cannot be changed , we can rewrite it . define new value

# lst = [1, 2, 3, 4, 5]
# lst[2] = 10 
# print(lst)

# Tuple --> data type , immutable version of list, does not support item assignment
# not necessary use ()

# tpl = (1,2,3,True,10.10, "hello")
# print (tpl)

# tpl = list((1,2,3,True,10.10, "hello")) # convert to list 

# tpl = (1, 0, -10, 8, 7)
# ans = sorted(tpl)
# print(tuple(ans))

# a = "Hello"
# print(tuple(a))

## Intro to dictionaries
# what is the dictionary?

# sring --> 1 key 1 value
# int --> 1 key 1 value
# list --> 1 key multiple values
# tuple --> 1 key multiple values
# dictionary --> multiple keys multiple values

# jan_class = {
#     "beka": "prius",
#     "iana": "cake",
#     "erkin": "coffee",
#     "kostya": "massage",
#     "aibek": "english teacher",
#     "aigerim": "ten years",
#     "cuneyt": "homeworks",
# }
# # print(jan_class["beka"])
# for elelment in jan_class.items(): #.values() for value, ,keys for keys
#     print(elelment)

## create a dictionary with each student
# key is random unique userid
# each key hold values like: first_name, word, phone_number

# new_dict = {
#     1: {"first_name": "beka", 'word': "prius", "phone_number": "123-321-2345"},
#     2: {"first_name": "iana", 'word': "cake", "phone_number": "463-765-4567"},
#     3: {"first_name": "erkin", 'word': "coffee", "phone_number": "543-367-2645"},
# }
# print (new_dict[1]["word"])