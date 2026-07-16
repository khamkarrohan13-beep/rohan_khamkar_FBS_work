# 7. Write a program to create a new list from existing list which contains cube of
# each number of list.

li=[1,2,3,4,5,6,7,8,9]
li1=[]
for i in range(0,len(li)):
    li1.append(li[i]**3)

print(li1)

