# 2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

# take input from user 

c=(int(input('enter temperature celsius:')))

# convert temperature from celsius to fahrenheit

f=(9*c/5) + 32

# display temperature

print(f'temperature in fahrenheit:{f}')