# 10. Write a program to remove all occurrences of a given element in the list. 

li = [10, 20, 30, 20, 40, 20, 50]
ele = int(input('enter the element to remove: '))
li1=[]
for i in range(0,len(li)):
    if li[i]==ele:
        pass
    else:
        li1.append(li[i])

print(li1)        