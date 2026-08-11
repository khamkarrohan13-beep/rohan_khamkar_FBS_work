# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

def find_pairs_with_sum(lst, target):           
    pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs

lst = [1, 2, 3, 4, 5]
target = 5
result = find_pairs_with_sum(lst, target)
print(f'Pairs of elements in the list whose sum is equal to {target}: {result}')
