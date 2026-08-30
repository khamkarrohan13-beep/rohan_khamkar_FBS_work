# 3. Count the number of spaces in a string (take input from user)
string=input('enter a string:')

count=sum([1 for i in string if i==' '])

print("number of spaces:",count)