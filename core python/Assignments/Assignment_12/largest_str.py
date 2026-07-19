# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions

str1=input('enter first string:')
str2=input('enter second string:')      

count1=0
count2=0
for i in range(len(str1)):      
    count1+=1
for i in range(len(str2)):      
    count2+=1

if count1>count2:
    print(f'larger string is:{str1} length of string is:{count1}')       
else:
    print(f'larger string is:{str2} length of string is:{count2}')    





