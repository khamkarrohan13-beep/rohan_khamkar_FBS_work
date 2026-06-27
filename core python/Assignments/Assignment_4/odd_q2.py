#2. WAP to print all odd numbers until n.

#take number from user

n=int(input('enter a number:'))

i=1
while(i<=n):
    if i%2!=0:
        print(i)
    i+=1

      