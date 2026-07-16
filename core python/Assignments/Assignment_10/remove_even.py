# 13 . Write a program to print list after removing even numbers.
li=[1,2,3,4,5,6,7,8,9]
li1=[]
for i in range(0,len(li)):
    if li[i]%2==0:
        pass
    else:
        li1.append(li[i])

print(f'after removing even numbers: {li1}')        