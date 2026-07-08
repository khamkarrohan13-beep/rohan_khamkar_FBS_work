def sum1(n):
    if n == 0:
        return 0
    return (n % 10) + sum1(n // 10)

rs = sum1(12345)


print(rs)


