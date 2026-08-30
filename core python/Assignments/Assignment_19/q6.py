# 6. Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)

sentence=input('enter a sentence:')

result={word:len(word) for word in sentence.split()}

print(result)