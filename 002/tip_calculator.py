print("Welcome to the tip calculator")

# Getting the bill information
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 15, or 20? "))
split = int(input("How many people to split the bill? "))

# Calculating the bill
total_bill = bill + (bill * tip_percentage / 100)
bill_per_person = total_bill / split

# Round the bill to two decimal places
final_bill = round(bill_per_person, 2)

print(f"Each person should pay: {final_bill}")
