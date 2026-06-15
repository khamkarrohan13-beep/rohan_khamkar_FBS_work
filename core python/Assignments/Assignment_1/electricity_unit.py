# 13. Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill


# take unit input

unit = int(input('Enter electricity units: '))

# calculate bill

if (unit <= 50):
    bill = unit * 0.50

elif (unit <= 150):
    bill = (50 * 0.50) + ((unit - 50) * 0.75)

elif unit <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + ((unit - 150) * 1.20)

else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((unit - 250) * 1.50)

# add 20% surcharge

total_bill = bill + (bill * 20 / 100)

# display result

print(f'Total electricity bill is: {total_bill}')
