#take input from user

p=int(input('enter the principle amount:'))

t=int(input('enter time in year:'))

r=int(input('enter rate of interst:'))

# calculate the simple interest

si=(p*t*r)/100

# display result

print(f'simple interst is {si}')
