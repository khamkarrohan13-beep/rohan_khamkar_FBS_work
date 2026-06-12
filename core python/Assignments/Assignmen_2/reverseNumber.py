# take input from user
n=(int(input('enter the theree digit number:')))

# seprate the numbers

last=n%10
n=n//10

mid=n%10
n=n//10


first=n

print(f'revers is:{last}{mid}{first}')