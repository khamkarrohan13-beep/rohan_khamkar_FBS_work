def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

strong = list(filter(lambda n: n == sum(fact(int(d)) for d in str(n)), range(1, 1001)))

print(strong)