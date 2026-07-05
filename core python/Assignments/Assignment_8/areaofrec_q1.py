#1. Write a program to calculate area of rectangle

#fuction for area of rectangle

def area(lenght,breadth):
    return lenght*breadth

#take input from user
l=int(input('enter lenght of rectangle:'))
b=int(input('enter breadth of rectangle:'))

#store fuction return value in variable
res=area(l,b)
print(f'area of rectangle is {res}')
