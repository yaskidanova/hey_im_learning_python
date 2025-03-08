# What is control flow --> how your code will behave \n
# if/else conditions ; for loops ; while loops ; function \n
# makes your code very dynamic 

# print (bin(10))
# print (bin(15))

# print (10 & 15)
# print (bin(100))

# print (100 >> 5)
# print (bin(3))

#left shift divides the number into 2 --> 100 >> 3 devides 3 times

#right shift << 

#### Loops 
#
# for loop 
# print ("hello") * 10 

#for <interable name for loop> in <sequence>:
    # <instructions>
#word="Hello" --> sequence of character
# for char in "Hello":
#     print (char + "lo")

#print number from 1 to 10 
# num = 10, it's just a number , doesn't represent the numbers 1-10

# for num in range (10):                      
#     print(num)

## class task 
#print numbers from 0-100

# for num in range (101):
#     print(num)

#print only even number all the way to 10

# for num in range (11):
#     if num % 2 == 0:
#         print (num)

#Character counter
#take an input of the word/senetence
#calculate how many A characters are in the word/sentece
#input: aKumosolutions

# word = input("Please, provide a word or sentence: ")
# counter = 0
# for char in word:
#     if char == "a":
#         counter = counter + 1
# print(counter)

#instead of taking letter "a" let the user choose the letter
#sentence or character should be cases insensetive (hint: use str.lower or str.upper)

word = input("Please, provide a word or sentence: ")
word2 = input("Choose any letter from your word or sentence: ")
word3 = input("Choose second letter from your word or sentence: ")

counter = 0
counter2 = 0

if len(word2) == 1 and len(word3) == 1:
    for char in word:
        if char == word2:
            counter = counter + 1
        elif char == word3:
            counter = counter2 + 1
    print(f"{word2} = {counter}")
    print(f"{word3} = {couner2}")
    
else:
    print ("Character input is more than 1")

print(counter)

