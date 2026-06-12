# take input from the user

f=(int(input('enter foot:')))
i=(int(input('enter inches:')))

# calculate meter and centimeter

total_inches=(f*12)+i

cm=total_inches*2.45

meter=cm/100

# display results

print(f'meter:{meter} centimeter:{cm}')
