# take input from user

n=(int(input('enter the theree digit number:')))

last1=n%10

#remove last digit

n=n//10

last2=n%10

#remove last digits
n=n//10


last3=n

sum=last1+last2+last3

print(f'sum of digits is:{sum}')


