s = "abc123xyz456"
str=''

for ch in s:
    if ch.isdigit():
        str+=ch

print(str)


s = "abc123xyz456"

str=''

for ch in s:
    if ch.isalpha():
        str+=ch

print(str)

# print(s.isalnum())