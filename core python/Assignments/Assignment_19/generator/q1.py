# Assignment on Generator

# 1. We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def fibonacci(n):
    a = 0
    b = 1

    while a <= n:
        yield a
        a, b = b, a + b


n = int(input("Enter the limit: "))

for num in fibonacci(n):
    print(num)