n = 5

for i in range(1, n + 1):

    # Print leading spaces
    for j in range(1, n - i + 1):
        print(" ", end=" ")

    # Print numbers
    for j in range(1, 2 * i):
        if i == n:
            if j % 2 != 0:
                print((j + 1) // 2, end=" ")
            else:
                print(" ", end=" ")
        elif j == 1:
            print(1, end=" ")
        elif j == 2 * i - 1:
            print(i, end=" ")
        else:
            print(" ", end=" ")

    print()
      