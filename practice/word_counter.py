# Write a script thet reads a file and counts how many times each word appears 

# open and read the file 
with open("file.txt","r") as file:
    content = file.read()

# in order to operate with each words I have to convert to lowercase all of them and split 
import string

all_words = content.lower()
words = all_words.split()

# we need to remove all punctuation in order to count 
words = [word.strip(string.punctuation) for word in words]

word_count = {}

# for loops will go through each word in the list and count how many times that word appears

for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
print(word_count)


