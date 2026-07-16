# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.

li = [10, 20, 30, 20, 40, 10, 50]

li1=[]

for i in range(0,len(li)):
    li1.append(li[i])

print(f'new list is: {li1}')