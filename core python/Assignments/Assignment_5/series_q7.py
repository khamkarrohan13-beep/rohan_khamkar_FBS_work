# a. 1! + 2! + 3! + 4! + .....n!

# take value of n from user
n1=int(input('enter number:'))

sum1=0

for i in range(1,n1+1):
    
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    sum1+=fact
print(sum1)        

# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

n2=int(input('enter number:'))
sum2=0
for i in range(1,n2+1):
    sum2+=n2**i

print(sum2)    
       
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n3=int(input('enter number:'))
sum3=1
for i in range(1,n3+1):
    sum3+=i*2

print(sum3)    

# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10


a=int(input('enter number:'))
sum4=0
add4=0
for i in range(1,11):
    add4+=(a*i)/i

sum4+=add4

print(sum4)
    

# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input("Enter value of x: "))
n5 = int(input("Enter number of terms: "))

sum5 = x
denominator = 3

for i in range(2, n5 + 1):
    term = (x * i) / denominator

    if i % 2 == 0:
        sum5 = sum5 - term
    else:
        sum5 = sum5 + term

    denominator = denominator + 2

print("Sum =", sum5)
