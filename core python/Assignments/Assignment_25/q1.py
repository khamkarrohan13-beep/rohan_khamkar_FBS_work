# Python Assignment – (Regular Expression)
# 1. Develop a function that takes a text and a list of forbidden words. Replace all
# occurrences of these forbidden words with asterisks (*) using regular expressions.


import re

def replace_forbidden(text, words):
    for word in words:
        pattern = r"\b" + word + r"\b"
        text = re.sub(pattern, "*" * len(word), text, flags=re.IGNORECASE)

    return text


text = input("Enter text: ")

words = input("Enter forbidden words: ").split()

print("Original text:", text)
print("Modified text:", replace_forbidden(text, words))