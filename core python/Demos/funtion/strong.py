def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact    



def isStrong(num):
    temp=num
    sum=0
    while(temp>0):
        d=temp%10
        print('digits',d)
        temp=temp//10

        fact=factorial(d)
        print('factorial:',fact)
        sum=sum+fact
        print('sum:',sum)

    if sum==num:
        return True
    else:
        return False    

num=int(input('enter number'))

res=isStrong(num)
print(res)



