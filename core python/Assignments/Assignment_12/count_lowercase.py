# 12. Python Program to count number of lowercase characters in a string.

str=input('enter a string:')
count=0

for i in range(len(str)):
    if str[i].islower():
        count+=1    
        
print(f'number of lowercase characters in the string is:{count}')