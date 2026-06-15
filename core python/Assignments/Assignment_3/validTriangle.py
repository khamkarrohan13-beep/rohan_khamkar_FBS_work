# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

#take input from user

angle1=int(input('enter first angel:'))
angle2=int(input('enter second angel:'))
angle3=int(input('enter third angel:'))

#check the condition
if(angle1+angle2+angle3==180):
    print('triangle is valid.')

else:
    print('triangle is not valid.')    