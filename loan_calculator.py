#Get the loan details from the user

money_owed = float(input("How much do you owe?"))
apr = float(input("What is the annual percentage rate"))
payment = float(input("What will your monthly payment be?\n"))
months= int(input("How many months of loan)"))

monthly_rate = apr/100/12


for i in range(months):
    #Add interest
    interest_paid = money_owed*monthly_rate
    money_owed = money_owed + interest_paid

    #make payment
    money_owed = money_owed - payment

    #print results
    print("Paid", payment, "of which ", interest_paid, "was interst", end=" ")
    print("Now I owe", money_owed)