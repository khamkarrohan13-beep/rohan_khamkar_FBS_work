# 12. Write a program to check if given 3 digit number is a palindrome or not.

#take number from user
num=int(input('enter 3 digit number:'))

#take one temperory variable to store orignal value
temp=num

#calulate reminder using % and seperate digit using //
d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10
num=num//10

#shit positon of unit to hundred by mutiplying by 100 shift tens position to  by mutiplying 10  
rev=(d1*100)+(d2*10)+(d3*1)

# display result
if(temp==rev):
    print('palindrome number.')
else:
    print('not palindrome.')   

