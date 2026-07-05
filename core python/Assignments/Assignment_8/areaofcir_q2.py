#2. Write a program to calculate area of circle

def area(radius):
    return 3.14*radius*radius

r=int(input('enter radius of circle:'))

res=area(r)

print(f'area of circle is {res}')