# 8. Write a program to convert days into years, weeks and days.

# take input from user

n=(int(input('enter total days:')))

#convert into year month and days

years=n//365
 
days=n%365 

weeks=days//7

days=days%7

# display result

print(f'year:{years} weeks:{weeks} days:{days}')

