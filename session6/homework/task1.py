# Task 1: Filter and Count Students by Attendance
# Write a function that takes a dictionary of students and a minimum attendance percentage. 
# The function should return a dictionary containing only the students who meet or exceed the attendance requirement.
# Example:
# students_data = {
#     "101": {"name": "Alice", "attendance": 95},
#     "102": {"name": "Bob", "attendance": 88},
#     "103": {"name": "Charlie", "attendance": 92},
#     "104": {"name": "Diana", "attendance": 80},
#     "105": {"name": "Ethan", "attendance": 90},
# }

# print(filter_students_by_attendance(students_data, 90))

# Output:
# {
#     "101": {"name": "Alice", "attendance": 95},
#     "103": {"name": "Charlie", "attendance": 92},
#     "105": {"name": "Ethan", "attendance": 90}
# }
import pprint
p = pprint.PrettyPrinter(indent=4)  # function to make an output prettier 

students_data = {
    "101": {"name": "Alice", "attendance": 95},
    "102": {"name": "Bob", "attendance": 88},
    "103": {"name": "Charlie", "attendance": 92},
    "104": {"name": "Diana", "attendance": 80},
    "105": {"name": "Ethan", "attendance": 90},
}


filter_students_by_attendance = {}

def students(data:dict, att:int):
    for i in data:
        if data[i]['attendance'] >= att:
            filter_students_by_attendance[i] = data[i]

students(data=students_data, att=90)

p.pprint((filter_students_by_attendance))