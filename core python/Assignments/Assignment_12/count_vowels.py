# 5. Python Program to Count the Number of Vowels in a String
str=(input('enter a string:'))
count=0

for i in range(len(str)):
    if str[i] in 'aeiouAEIOU':
        count+=1
print(f'number of vowels in string is: {count}')        