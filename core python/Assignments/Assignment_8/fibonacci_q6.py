#6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

def fib():

    n=int(input('enter number:'))
    a=-1
    b=1
    for i in range(1,n+1):
        c=a+b
        print(c)
        a=b
        b=c

fib()