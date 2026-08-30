# 4. Remove all of the vowels in a string (take input from user)

string=input('enter a string:')
result=''.join([i for i in string if i not in 'aeiouAEIOU'])
print('string after removing vowels',result)