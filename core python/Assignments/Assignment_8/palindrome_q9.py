#9. Write a program to check if entered number is a palindrome or
# not.

def pal(n):
   
    temp=n
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    if rev==temp:
        print(f'number is palindrome {rev}')   
    else:
        print('number is not palindrom')     

n=int(input('enter number:'))
pal(n)        