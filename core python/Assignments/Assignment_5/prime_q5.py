#5. Write a program to print prime numbers between 1 to 100.


for i in range(2, 101):
    flag = 0          # Inside outer loop

    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break

    if flag == 0:     
        print(i)