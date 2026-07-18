# 2. Python Program to Merge Two Lists and Sort it

li1=[50,70,60,90,80]
li2=[20,10,40,30,100]

merged=[]

for i in li1:
    merged.append(i)

for i in li2:
    merged.append(i)
    
merged.sort()    

print(merged)
