# 4. Write a program to input all sides of a triangle and check whether triangle is valid or
# not.

#take input as sides of triangle from user

a=int(input('enter first side:'))
b=int(input('enter second side:'))
c=int(input('enter third side:'))

#check the conditions
if(a+b > c and c+a>b and b+c>a):

    print('based on sides triangle is valid.')

else:
    print('triangle is valid.')
