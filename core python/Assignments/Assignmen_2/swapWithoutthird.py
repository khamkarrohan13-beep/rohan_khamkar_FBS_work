# 9. Write a program to swap two numbers without using third variable.

# take input from user
a=(int(input('enter first number a:')))
b=(int(input('enter second number b :')))

print(f'before swaping a={a} b={b}')
#swap numbers

#add both numbers and store in a
a=a+b
#subtract orignal b from new a and store in b
b=a-b
#subtract new b from a and store in a
a=a-b

#display result
print(f'after swaping a={a} b={b}')
