# 13. Python Program to count number of digits and letters in a string.
str=input('enter a string:')
digit_count=0
letter_count=0

for i in range(len(str)):
    if str[i].isdigit():
        digit_count+=1
    elif str[i].isalpha():
        letter_count+=1

print(f'number of digits in the string is:{digit_count}')
print(f'number of letters in the string is:{letter_count}')