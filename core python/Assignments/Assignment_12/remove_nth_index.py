# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String

str=input('enter a string:')
n=int(input('enter index number which you want to remove:'))
new_str=''

if n>=0 and n<len(str):
    for i in range(len(str)):
        if i!=n:
            new_str+=str[i]

    print('string after removing character:',new_str)
else:
    print('invalid index')    
            



