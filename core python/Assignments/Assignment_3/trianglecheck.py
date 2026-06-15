#5. Write a program to check whether the triangle is equilateral, isosceles or scalene
# triangle.

# take input as sides of triangle from user

a=int(input('enter first side:'))
b=int(input('enter second side:'))
c=int(input('enter third side:'))

#check every conditon
if(a+b+c==180 and a==b==c):
    print('triangle is valid and it is equilateral triangle.')

elif(a+b+c==180 and a==b or b==c or a==c ):
    print('triangle is valid and it is lsosceles triangle.')

elif(a+b+c==180 and a!=b and b!=c and c!=a):
    print('triangle is valid and it is scalene triangle.')

else:
    print('enter valid sides')
