
# Task 1:
# Given a dictionary of students and their scores, print only the students who scored more than 50.
# Dictionary: students = {"Alice": 45, "Bob": 78, "Charlie": 52, "David": 33}
# Output: Bob : 78, Charlie : 52


# make a dictionary
# for loop with conditions if num > 50
# display students with score more than 50 

students_dict = {
    "Alice": 45,
    "Bob": 78,
    "Charlie": 52,
    "David": 33,
    "John": 50,
}

for name, score in students_dict.items():
    if score >= 50:
        print (f"{name}: {score}")