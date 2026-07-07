# 2. Write a program to check if given number is Armstrong or not using recursive
# function.

def count(n):
    if n==0:
        return 0
    else:
        return 1+count(n//10)
    
def arm(n,power):
    if n==0:
        return 0
    d=n%10
    return (d**power)+arm(n//10,power)


n=int(input('enter number'))

power=count(n)
res=arm(n,power)

if res==n:
    print('number is armstrong number')
else:
    print('number is not armstrong number')    