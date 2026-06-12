#take input from user

a=(int(input('enter first number a:')))
b=(int(input('enter second number b :')))

print(f'before swaping a={a} b={b}')
#swap numbers

temp=a

a=b

b=temp

#display result
print(f'after swaping a={a} b={b}')