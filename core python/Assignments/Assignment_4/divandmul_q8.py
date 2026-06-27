#8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

#take input from user
n=int(input('enter a number:'))

for i in range(1,n+1):
    if (i%7==0 and i%5==0):
        print(i)