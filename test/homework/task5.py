# Task 5: Number Type Identifier
# Take a single integer input and classify it as follows:
# If it’s positive and even, print "Positive Even"
# If it’s positive and odd, print "Positive Odd"
# If it’s negative and even, print "Negative Even"
# If it’s negative and odd, print "Negative Odd"
# If it’s zero, print "The number is zero"


num = int(input("Please provide a number: "))

if (num % 2 == 0) and (num > 0):
    print ("Positive Even")
elif (num % 2 == 1) and (num > 0):
    print ("Positive Odd")
elif (num % 2 == 0) and (num < 0):
    print ("Negative Even")
elif (num % 2 == 1) and (num < 0):
    print ("Negative Odd")
else:
    print ("The number is zero")