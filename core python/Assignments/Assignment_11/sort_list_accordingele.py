# 5. Python Program to Sort a List According to the Length of the Elements
# within the list.

li = ["10", "200", "3", "4567"]

for i in range(len(li)-1):
    for j in range(len(li)-1):
        if len(li[j])>len(li[j+1]):
            li[j],li[j+1]=li[j+1],li[j]


print(li)