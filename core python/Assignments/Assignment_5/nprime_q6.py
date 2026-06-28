#6. Write a program to print first n prime numbers.

#take input from user 
n = int(input("Enter how many prime numbers you want: "))

count = 0
num = 2

while count < n:
    flag = 0

    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break

    if flag == 0:
        print(num)
        count += 1

    num += 1