# 5. Write a Python program to find the longest common prefix of all
# strings. Use the Python set.

strings = ["flower", "flow", "flight"]

prefix = ""

min_len = min(len(s) for s in strings)

for i in range(min_len):
    chars = {s[i] for s in strings}

    if len(chars) == 1:
        prefix += chars.pop()
    else:
        break

print("Longest Common Prefix:", prefix)