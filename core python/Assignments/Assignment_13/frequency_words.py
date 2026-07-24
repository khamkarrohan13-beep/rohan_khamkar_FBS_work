# 8. Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary

s=input('enter a string:')

d={}
words=s.split(' ')
for i in words:
    if i in d:
        d[i]+=1
    else:
        d[i]=1      
print(f'frequency of words in string:{d}')        
               