# 5. Write a program to find factorial using recursion.

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    


res=fact(n=int(input('enter number:')))    
print(res)

