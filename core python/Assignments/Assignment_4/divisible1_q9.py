#9. WAP to print all numbers in a range divisible by a given number.

#take input from user

n=int(input('enter a number:'))

for i in range(2,n):
    if n%i==0:
        print(i)
