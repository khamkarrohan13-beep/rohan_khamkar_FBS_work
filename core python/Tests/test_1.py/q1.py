# Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:

## take input from user

l=int(input("enter the lenght:"))
b=int(input("enter the breadth:"))
r=int(input("enter the radius:"))

#calculate area

rectanglearea=l*b
semicirclearea=(3.14*r*r)/2
totalarea=rectanglearea+semicirclearea

#calculate perimeter

perimeter=(2*l)+ b + (3.14 * r)

#display result

print(f'area of figure is :{totalarea}')

print(f'perimeter of figure if :{perimeter}')



