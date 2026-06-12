#take input from user

print('to calculate area of rectangle enter lenght and breadth')
l=(int(input('enter lenght :')))
b=(int(input('enter breadth :')))

# calculate area of rectangle

area1=l*b

# take input from user 
print('to calculate area of triangle enter base and height')

b=(int(input('enter base of triangle:')))
h=(int(input('enter height of triangle:')))

#calculate area of triangle

area2=(0.5)*b*h

# display results

print(f'area of rectangle is:{area1}')
print(f'area of triangle is:{area2}')