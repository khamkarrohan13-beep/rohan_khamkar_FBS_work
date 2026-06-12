num=int(input('enter 3 digit number:'))

temp=num

d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10
num=num//10

rev=(d1*100)+(d2*10)+(d3*1)

if(temp==rev):
    print('palindrome number.')
else:
    print('not palindrome.')   

