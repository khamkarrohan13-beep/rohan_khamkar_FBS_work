# 11. Write a program to print all numbers which are divisible by m and n in the
# list.


li = [10, 12, 15, 20, 30, 40, 60]
m = 2
n = 5

for i in range(0,len(li)):
    if li[i]%2==0 and li[i]%5==0:
        print(li[i])