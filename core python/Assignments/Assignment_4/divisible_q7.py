#7. WAP to print all integers upto n that aren’t divisible by 2 and 3.
#take input from user
n=int(input('enter a number:'))

for i in range(1,n+1):
    if(i%2!=0 and i%3!=0):
        print(i)

