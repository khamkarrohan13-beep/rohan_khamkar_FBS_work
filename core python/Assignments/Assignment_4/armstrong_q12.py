#12. Write a program to check if given number is Armstrong number or not.

n=int(input('enter a number:'))
temp=n
temp1=n
count=0
sum=0
while(temp>0):
    d=temp%10

    temp=temp//10
    count+=1


while(temp1>0):
    d1=temp1%10
    sum=sum+(d1**count)
    temp1=temp1//10

if sum==n:
    print('armstrong')
else:
    print('not an armstrong')    


