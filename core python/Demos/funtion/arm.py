def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)


def armstrong_sum(n, power):
    if n == 0:
        return 0
    digit = n % 10
    return (digit ** power) + armstrong_sum(n // 10, power)


n = int(input("Enter a number: "))

if n == 0:
    digits = 1
else:
    digits = count_digits(n)

result = armstrong_sum(n, digits)

if result == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")