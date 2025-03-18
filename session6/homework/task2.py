# # Task 2: Convert a Sentence to Abbreviations
# # Write a function that takes a sentence as input and returns an abbreviation using the first letter of each word in uppercase.
# # Example:
# # print(abbreviate("Central Processing Unit"))

# # Output:
# # "CPU"

# inp = ("Central Processing Unit").split()

def abbreviate(sentence):
    temp_lst = []
    # ['Central', 'Processing', 'Unit']
    for i in sentence:
        temp_lst.append(i[0].upper())

    return temp_lst


result=abbreviate(input("Please provide your a sentense: \n").split())
print("".join(result))


