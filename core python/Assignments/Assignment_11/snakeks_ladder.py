# 8. Print 1 to 100 in snakes and ladder pattern.
start = 1

for row in range(1, 11):

    if row % 2 != 0:
        # Print left to right
        for num in range(start, start + 10):
            print(num, end="\t")
    else:
        # Print right to left
        for num in range(start + 9, start - 1, -1):
            print(num, end="\t")

    start += 10
    print()