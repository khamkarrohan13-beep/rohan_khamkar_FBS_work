# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

li=[1,2,3,4,5,6,7,8,9,10,11,12,13]
even=[]
odd=[]

for i in range(0,len(li)):
    if li[i]%2==0:
        even.append(li[i])
    else:
        odd.append(li[i]) 
print(f'even elemets list is {even}')    
print(f'even elemets list is {odd}')    




