# Task 6: Age Group Classifier
# Ask the user for their age and classify them into a group: (Age range is from 0 - 120)
# 0 - 12 → "Child"
# 13 - 19 → "Teenager"
# 20 - 59 → "Adult"
# 60 and above → "Senior Citizen"

#When checking if a value is within a range, you need to use the 'in' operator with range()

num = int(input("Please provide your age: "))

if num in range(13):
    print ("You're from Child group")
elif num in range(13, 20):
    print ("You're from Teenager group")
elif num in range(20, 60):
    print ("You're from Adult group")
elif num in range(60, 121):
    print ("You're Senior Citizen")