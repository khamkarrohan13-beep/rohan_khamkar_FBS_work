# 1. Write a program to calculate the percentage of student based on marks of any 5
# subjects.

# take input from user 

s1=int(input('enter first subject marks:'))
s2=int(input('enter second subject marks:'))
s3=int(input('enter third subject marks:'))
s4=int(input('enter forth subject marks:'))
s5=int(input('enter fifth subject marks:'))

#percentage calculation

per=(s1+s2+s3+s4+s5)/500*100

# display percentage

print(f'percentage is : {per}')