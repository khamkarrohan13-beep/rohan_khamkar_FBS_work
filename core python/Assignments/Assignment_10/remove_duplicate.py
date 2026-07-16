# 6. Write a program to remove duplicates from the list.

li = [10, 20, 30, 20, 40, 10, 50]

res=[]

for i in range(0,len(li)):
    if li[i] not in res:
        res.append(li[i])

print(res)        