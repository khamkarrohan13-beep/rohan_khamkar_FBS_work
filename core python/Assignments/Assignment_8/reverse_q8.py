#8. Write a program find reverse of a number

def reve(n):
    
    temp=n
    rev=0
    while(temp>0):
        d=temp%10
        rev=rev*10+d
        temp=temp//10
        
    return rev


n=int(input('enter number:'))
res=reve(n)        
print(res)
