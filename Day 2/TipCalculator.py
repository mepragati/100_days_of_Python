#Calculating Tip and splitting equally among all people
print("Welcome to the Tip Calculator!!")
bill_amount = float(input("What was the total bill? $"))
tip_percentage= int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people=int(input("How many people to split the bill? "))
amount_to_pay=(tip_percentage/100)*bill_amount+bill_amount

print(f"Each person should pay: ${round(amount_to_pay/no_of_people,2)}")