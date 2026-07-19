# 3. Python Program to Detect if Two Strings are Anagrams
str1=input('enter first string:')
str2=input('enter second string')

if sorted(str1)==sorted(str2):
    print('strings are anagrams')
else:
    print('strings are not anagrams')    