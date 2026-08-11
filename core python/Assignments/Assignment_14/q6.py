# 6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

nums = [2, 5, 7, 9, 4]

s=set(nums)
li=list(s)

max_product=li[0]*li[1]
a=li[0]
b=li[1]

for i in range(len(li)):
    for j in range(i+1,len(li)):
        product=li[i]*li[j]

        if product > max_product:
            max_product=product

            a=li[i]
            b=li[j]
print(f'maximum pair ({a}, {b}) product is {max_product}')

