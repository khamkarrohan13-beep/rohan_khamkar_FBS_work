#5. WAP to print Fibonacci series upto n.

#take input form user
n=int(input('enter a number:'))
#initial value of two varibles will be 1 and -1
a=-1
b=1

i=1
while(i<=n):
    c=a+b
    print(c)
    a=b
    b=c
    i+=1
#using for loop
n1=int(input('enter a number:'))

a1=-1
b1=1


#using for loop
for i1 in range(n1):

    c1=a1+b1
    print(c1)
    a1=b1
    b1=c1




