# Track your daily expenses by allowing the user to input: a category, an amount, a date 
# Store that in a file and let the user: add new expense, view all expenses, view total and exit

# I need to get a users inputs
expense = input("Please, enter the category here: ")
date = input("Please enter the date: ")
amount = float(input("Please enter an amount: "))

with open("user_data.txt", "a") as file:
    file.write(f"{expense}, {date}, {amount}\n")