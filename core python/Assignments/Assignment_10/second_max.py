# 3. Write a program to find the second largest element in the list.
li=[10,20,30,40,50,60,70]
max1=li[0]
for i in range(1,len(li)):
    if li[i]>max1:
        max1=li[i]
# print(max1)       

max2=li[0]
for i in range(1,len(li)):
    if li[i]!=max1 and li[i]>max2:
        max2=li[i]
print(f'second largest element is: {max2} ')        