# 7. Python Program to Calculate the Length of a String Without Using a
# Library Function

str=input('enter a string:')

count=0

for i in range(len(str)):
    count+=1

print(f'length of string is {count}')
