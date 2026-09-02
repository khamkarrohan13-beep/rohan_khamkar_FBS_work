# 4. Write a function that extracts all the URLs from a given text using regular expressions.
# Return a list of URLs found in the input text.

import re

def extract_urls(text):
    pattern = r'https?://\w+\.\w+'
    urls = re.findall(pattern, text)
    return urls


text = input("Enter text: ")

print("URLs:", extract_urls(text))