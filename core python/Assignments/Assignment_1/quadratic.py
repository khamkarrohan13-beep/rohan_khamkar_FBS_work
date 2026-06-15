# 7. Program to Find the Roots of a Quadratic Equation

# take input from user 
a=int(input('enter the value of a:'))
b=int(input('enter the value of b:'))
c=int(input('enter the value of c:'))

# calculate discriminant
d= b**2 - (4*a*c)

#find roots


x1 = (-b + (d**0.5)) / (2*a)
x2 = (-b - (d**0.5)) / (2*a)

#display roots

print(f'first root={x1}')
print(f'second  root={x2}')



