# 3. WAP to print sum of series upto n.

#take number from user
n=int(input('enter a number:'))

#if number i is less than or equal to number add in sum
sum=0
i=1


while(i<=n):
    sum=sum+i

    i+=1
print(sum)    

#using for loop

n=int(input('enter a number:'))
sum1=0
for i in range(1,n+1):

    sum1=sum1+i
print(sum)    