import random as r

li1=[]
li2=[]
li3=[]
for i in range(100000):
    li1.append(r.randint(1,100000))
    li2.append(r.randint(1,100000))

for i in range(100000):
    li3.append(li1[i]+li2[i])

print(li3)

 

