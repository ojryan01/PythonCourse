
expenses  = []
total = 0

num_expenses = int(input("Enter number of receipts:\n"))

for i in range(7):
    expenses.append(float(input("Enter an expense: \n")))

total = sum(expenses)

total = sum(expenses)

for x in expenses:
    sum = sum + x

print("You spent $", sum, " this week.", sep = "")