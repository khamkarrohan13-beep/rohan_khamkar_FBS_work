#7. Write a program to find sum of digits of a number.

def sum():
    n=int(input('enter number:'))
    sum=0
    while(n>0):
        d=n%10
        sum+=d
        n=n//10
    return sum
res=sum()

print(f"sum of digits is: {res}")
