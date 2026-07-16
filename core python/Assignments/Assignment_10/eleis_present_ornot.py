# 5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.


def checkEle(li):
    num=int(input('enter number:'))
    count=0
    for i in range(0,len(li)):
        if num==li[i]:
            count+=1
    return count

li=[10,50,20,30,40,50,50,60,70]
res=checkEle(li)

print(f'element is present {res} times')
    