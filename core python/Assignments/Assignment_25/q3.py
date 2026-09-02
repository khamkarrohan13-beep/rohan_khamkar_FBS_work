# 3. Develop a function that counts the occurrences of each word in a given text. Use regular
# expressions to split the text into words and then count the frequency of each word.

import re

def count_words(text):
    words = re.findall(r'\w+', text)

    count = {}

    for word in words:
        word = word.lower()

        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count


text = input("Enter text: ")

print(count_words(text))