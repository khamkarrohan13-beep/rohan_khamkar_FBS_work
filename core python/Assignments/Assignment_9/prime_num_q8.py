# 8. Write a program to check whether a number is prime or not using recursion.

def prime(n,i):
    if n<=0:
        return False
    if n==i:
        return True
    if n%i==0:
        return False
    return prime(n,i+1)

n=int(input('enter number:'))

if prime(n,2):
    print('number is prime')

else:
    print('not prime')    
