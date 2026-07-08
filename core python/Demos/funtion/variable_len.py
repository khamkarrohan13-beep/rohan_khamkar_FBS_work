def add(*num):
    sum=0
    for i in num:
        sum+=i

    return sum

res=add(10,20,30,40,50)    
print(res)

res=add(1,2,3,4,3,5,6,7,5,6,4,8,9,5,7,4,3,6,9,8,9,7,)
print(res)