#6. WAP to check if a given number is prime number or not.

#take input from user
n=int(input("enter a number:"))

#1 is not prime number 
if(n<=1):
    print('number is not prime nor composite')

else:
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is not prime")
            break
    else:
        print(f'{n} is prime')
        
