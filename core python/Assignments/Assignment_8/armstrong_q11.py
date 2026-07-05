# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

def cou(n):
    count=0
    while(n>0):
        n=n//10
        count+=1
    return count    


def arm(n):
    temp=n
    sum=0
    digits=cou(n)
    while(temp>0):
        d=temp%10
        sum+=d**digits
        temp=temp//10
    if sum==n:
        print('number is armstrong')
    else:
        print('number is not armstrong ')        


n=int(input('enter number:'))
arm(n)
