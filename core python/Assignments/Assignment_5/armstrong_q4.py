#4. WAP to print Armstrong number within a given range


#take input from user

start=int(input('enter starting number:'))
end=int(input('enter ending number:'))

for num in range(start,end+1):
    temp=num
    orignal=num
    count=0
    arm=0

    while(temp>0):
        temp=temp//10
        count+=1

    temp=num
    
    while(temp>0):
        d=temp%10
        arm+=d**count
        temp=temp//10

    if arm==orignal:
        print(arm)    

    