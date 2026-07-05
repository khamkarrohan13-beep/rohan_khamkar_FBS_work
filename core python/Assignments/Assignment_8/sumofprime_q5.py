#5. Sum of all prime numbers between 1 to n

def sum(n):
    sum=0
    
    for i in range(2,n+1):
            flag=0
            for j in range(2,i):
                if i%j==0:
                    flag=1
                    break
            if flag==0:
                 sum+=i
    return sum

n=int(input("enter number:"))

res=sum(n)
print(f'sum of all prime number is {res}')