# 3. Python Program to Sort the List According to the Second Element in Sublist

li = [[1, 50], [2, 20],[3, 60], [4, 40], [5, 10],[6, 30]]

for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if li[i][1]>li[j][1]:
            li[i],li[j]=li[j],li[i]


print(f'sorted list:{li}')            






