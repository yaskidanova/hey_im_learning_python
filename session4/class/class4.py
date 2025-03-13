# Agenda
# while loops

### for loops --> sequence --> it has an start and end point
### while loop takes only boolean data type, it will run until condition is false

#syntax
#while <condition>:
#   <code>    

# secret_password = "Python123"
# inp = input("Provide your password: ")
# max_attempts = 3
# attempts = 0

# while attempts < max_attempts:
#     if secret_password != inp:
#         attempts = attempts + 1
#         inp = input("Wrong password, Please try agin: ")
#     else:
#         print("Access Granted")
#         break 

# max_attempts = 3
# attempts = 0

# while attempts < max_attempts:      # runs infinetely until it runs to false
#     print(attempts)
#     attempts = attempts +1

# continue and break 
# break --> keyword that stops the loop 
# 

# for i in range (3):
#     for j in range (4)
#         if j == 2:
#             break
#         else:
#             print(i, j)

# continue --> 
# for has iterators --> range(3) --> 0, 1, 2

# for i in range (10):
#     if i == 5:
#         continue
#     else:
#         print(i)

#pass  --> it can be used with if conditions , for/while loops, functions --> filter --> it does nothing

# for i in range (10):
#     pass 

# print ("Hello")

# Data types that can handle multiple values 
# Lists -- Data type 
# - sets
# - tuples
# - dictionaries 

# Lists can hadle multiple values and multiple data type 

# lst_names = [ "Yana","Esen","Erkin","Beka" ]
# print (lst_names [::1])

## class task 
# ask for input of character, print names that contains this character (Note:the program should be case intensitive)
# input: r
# Output: 
#Erkin 
#Aigerim

# lst_names = [
#     "Esen",
#     "Beka",
#     "Iana",
#     "Erkin",
#     "Aigerim",
#     "Kostya",
#     "Jyldyz",
#     "Cuneyt",
#     "Gulnaz",
#     "Aibek",
# ]


# inp = input("Please provide any character A-Z here: ")
# for name in lst_names:
#     if inp.lower() in name.lower():
#         print (name)    
#     else: 
#         print (f"No student that has letter {inp}")
#         break

# lst_names = [
#     "Esen",
#     "Beka",
#     "Iana",
#     "Erkin",
#     "Aigerim",
#     "Kostya",
#     "Jyldyz",
#     "Cuneyt",
#     "Gulnaz",
#     "Aibek",
# ]
# filtered_names = []

# for name in lst_names
#     if inp.lower() in name.lower():
#         foltered_names.append(name)
# print (filtered_names)

#lists functions
# append () --> add the value to the back of a list 
# insert () --> add to the list and you define the place 
# pop ()    --> removes from the end of the list 
# remove ()
# sort ()

# fruits = ["banana", "apple", "pineapple"]
# fruits.append("cherry")
# print (fruits)

# fruits = ["banana", "apple", "pineapple"]
# fruits.insert(1, "cherry")
# print (fruits)

# fruits = ["banana", "apple", "pineapple"]
# fruits.pop(1)
# print (fruits)

# fruits = ["banana", "apple", "pineapple"]
# fruits.remove("apple")
# print (fruits)

# fruits = ["banana", "apple", "pineapple"]
# fruits.sort()
# print (fruits)

# fruits = ["banana", "apple", "pineapple"]
# fruits.sort(reverse=True)  # back
# print (fruits)

## class task

# filter the list to have only string data type

# lst = ["banana", True, False, "apple", 10, "pineapple", "cherry", "apple", 1, 10.3, True]
# #(isinstance(lst, str))
# filtered_lst = []

# for element in lst:
#     if isinstance(element, str):
#         filtered_lst.append(element)
# print (filtered_lst)