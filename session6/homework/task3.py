# Task 3: Find Common Elements in Two Lists
# Write a function that takes two lists as input and returns a list containing only the common elements (without duplicates).
# Example:
# print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  
# Output:
# [3, 4]

my_lst1 = [1, 2, 3, 4, 5, 6]
my_lst2 = [2, 3, 3, 4, 6, 8]

def common_elements (my_lst1, my_lst2):
    return list(set(my_lst1) & set(my_lst2))

common_elements(my_lst1, my_lst2)

print (common_elements(my_lst1, my_lst2))