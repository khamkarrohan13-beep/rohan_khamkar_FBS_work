def secondMax(li):
    max1=li[0]
    for i in range(1,len(li)):
        if li[i]>max1:
            max1=li[i]
    max2=0
    for i in range(len(li))  :
        if li[i]!=max1 and li[i]>max2:
            max2=li[i]
    return max2


li=[100,20,30,40,50,60] 
res=secondMax(li)
print("second max element is",res)