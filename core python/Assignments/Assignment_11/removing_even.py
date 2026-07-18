# 10. Write a program to print list after removing even numbers.

li=[1,2,3,4,5,6,7,8,9]
even=[]
for i in range(len(li)):
    if li[i]%2!=0:
        even.append(li[i])

print(f'list after removing even numbers:{even}')        
