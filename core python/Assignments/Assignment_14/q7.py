# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("Missing numbers in set2:", missing_in_set2)
print("Missing numbers in set1:", missing_in_set1)