# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n=int(input('enter number of students:'))
sum=0
for i in range(1,n+1):
    print(f'enter marks for student {i}:')

    s1=int(input('enter first subject marks:'))
    s2=int(input('enter second subject marks:'))
    s3=int(input('enter third subject marks:'))
    s4=int(input('enter fourth subject marks:'))
    s5=int(input('enter fifth subject marks:'))

    per=(s1+s2+s3+s4+s5)/500*100
    print(f'percentage of student {i} is {per}')
    sum=sum+per

avgper=(sum/n)

print(f'average percentage of students is {avgper}')
