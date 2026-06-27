#4. WAP to print factorial of a number .

#take number from user
n=int(input('enter a number you want a factorial of:'))
sum=1
for i in range(1,n+1):
    sum=sum*i
     
print(sum)

#using while loop 
n=int(input('enter a number:'))
i=1
sum1=1
while(i<=n):
    sum1=sum1*i

    i+=1
print(sum1)
   