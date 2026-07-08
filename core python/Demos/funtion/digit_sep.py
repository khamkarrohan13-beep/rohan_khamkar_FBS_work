def digits(n):
    if (n>0):
        d=n%10
        print(d)
        digits(n//10)


res=digits(12345)    

    