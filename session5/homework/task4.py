# Task 4
# You are given two dictionaries where the keys represent item names and the values represent their respective counts
# Input: 
# dict1 = {"apple": 3, "banana": 5, "orange": 2}
# dict2 = {"banana": 2, "orange": 4, "grape": 6}

# Output: 
# {
#     "apple": 3,   # Only in dict1
#     "banana": 7,  # 5 (from dict1) + 2 (from dict2)
#     "orange": 6,  # 2 (from dict1) + 4 (from dict2)
#     "grape": 6    # Only in dict2
# }


# we have two dictionaries 
# create an empty directories to store the output
# create a foor loop which will check each value 
# if this value already exists 



dict1 = {
    "apple": 3,
    "banana": 5,
    "orange": 2
}

dict2 = {
    "banana": 2,
    "orange": 4,
    "grape": 6
}

dict3 = {}

def combine_dict(dict1, dict2):
    for key, value in dict1.items():
        dict3[key] = value      # we add a new key value pair to a new dict
    for key, value in dict2.items():
        if key in dict3:
            dict3[key] += value         #add value if key exists in dict1 and 2 
        else:
            dict3[key] = value
    return dict3

dict3 = combine_dict(dict1, dict2)
print(dict3)