# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String

str=input('enter a string:')

char_count=0
word_count=1

for i in range(len(str)):
    if str[i]==' ':
        word_count+=1
    else:   
        char_count+=1 

print(f'number of characters: {char_count}')
print(f'number of words: {word_count}')