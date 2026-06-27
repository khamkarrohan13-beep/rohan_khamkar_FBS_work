#11. WAP to check if given number Strong Number.
n=int(input('enter a number:'))
sum=0
temp=n


while n>0:
    d=n%10
    fact=1
    for i in range(1,d+1):
        fact*=i
    sum+=fact 
    n=n//10

if sum==temp:
    print('strong number') 
else:
    print('not strong number')         
