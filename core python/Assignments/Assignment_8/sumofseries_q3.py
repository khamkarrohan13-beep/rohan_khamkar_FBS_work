#3. Write a program to find sum of following series using functions :

#a. 1+ 2 + 3 + 4+..... + n

def sum1():
    sum=0
    n=int(input('enter number:'))
    
    for i in range(1,n+1):
        sum+=i
    
    return sum

res=sum1()

print(f'sum of series is: {res}')

#b. 1!+ 2! + 3! + 4!+..... + n!

def sum2():
    n=int(input('enter number'))
    
    sum=0
    for i in range(1,n+1):
        fact=1
        for j in range(1,i+1):
           fact=fact*j
        sum+=fact
    return sum
    
res=sum2()
print(f'sum of series is: {res}')    

#c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum3():
    n=int(input('enter number:'))
    sum=0
    for i in range(1,n+1):
        sum+=i**i
    return sum


res=sum3()
print(f'sum of series: {res}')
