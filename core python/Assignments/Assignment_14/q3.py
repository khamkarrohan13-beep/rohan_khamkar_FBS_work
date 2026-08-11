# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

strings = ["apple", "banana", "apple", "cherry", "banana", "date"]
unique_words = set(strings)
word_freq = {}
for i in unique_words:
    word_freq[i] = strings.count(i)
print(f'Unique words: {unique_words}')
print(f'Frequency of occurrence: {word_freq}')
