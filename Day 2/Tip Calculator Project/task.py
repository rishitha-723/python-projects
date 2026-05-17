print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
#multiple code lines
tip_as_percent = tip/100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
print("Each person should pay:",'$',final_amount )
# shorter version
print((bill * (1+ tip / 100)) / people)
print((bill + (bill * tip / 100)) / people)


