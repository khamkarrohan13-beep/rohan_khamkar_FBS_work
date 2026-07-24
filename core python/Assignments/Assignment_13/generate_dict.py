# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).

# n=int(input("Enter a number: "))
# d1={}   

# for i in range(1, n+1):
#     d1.update({i: i*i})

# print(d1)

def generateDict(d1,n):
    for i in range(1,n+1):
        d1[i] = i*i
    return d1
d1={}
n=int(input('enter number:'))

generateDict(d1,n)

print(d1)

