num=int(input('enter number:'))

temp=num
sum=0
temp1=num

count=0
while(temp>0):
    d=temp%10
    temp=temp//10
    print(d)
    count+=1
print(count)


while(temp1>0):
    digit=temp1%10
    sum+=(digit**count)
    temp1=temp1//10

if (sum==num):
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")

print(temp)
print(temp1)