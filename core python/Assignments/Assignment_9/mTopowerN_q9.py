# 9. Write a program to calculate the m to the power n using recursion.

def cal(m,n):
    if n==0:
        return 1
    else:
        return m*cal(m,n-1)
    
m=int(input('enter base:'))    
n=int(input('enter power:'))    

res=cal(m,n)
print(res)