# 7. Python Program to Find the Intersection of Two Lists

li1=[10, 20, 30, 40]
li2=[30, 40, 50, 60]

inter=[]

for i in range(0,len(li1)):
    if li1[i] in li2 and li1[i] not in inter:
        inter.append(li1[i])

print(inter)        
