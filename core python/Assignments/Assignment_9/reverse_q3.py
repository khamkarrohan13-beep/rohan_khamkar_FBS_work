# 3. Write a program to reverse a given number using recursive function.

def reverse(n,rev):
    if n==0:
        return rev
    else:
        return reverse(n//10,rev*10+n%10)
    

    
n=int(input('enter number'))
res=reverse(n,0)  

print(res)