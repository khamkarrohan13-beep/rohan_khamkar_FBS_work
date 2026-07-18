# 1. Python Program to Put Even and Odd elements of a List into two Different
# Lists

li=[1,2,3,4,5,6,7,8,9]

even=[]
odd=[]
for i in range(0,len(li)):
    if li[i]%2==0:
        even.append(li[i])
    else:
        odd.append(li[i])    

print(even)
print(odd)

