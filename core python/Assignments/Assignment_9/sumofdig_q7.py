# 7. Write a program to find sum of digits using recursion.

def sumOfdig(n):
    if n==0:
        return 0
    else:
        d=n%10
        return d+sumOfdig(n//10)
    

res=sumOfdig(n=int(input('enter number:')))    

print(res)

