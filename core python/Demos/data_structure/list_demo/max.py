

def max(li):
    max=li[0]
    for i in range(1,len(li)):
        if (li[i]> max):
            max=li[i]
    return max    

li=[34,56,76,54,98,65,43]
res=max(li)


print('maximum number is',res)

