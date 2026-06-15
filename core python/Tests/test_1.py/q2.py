# Write a program to calculate simple interest based on Principal, Rate and Time
# (SI = P*R*T/100)


#take input from user

p=int(input('enter principle amount:'))
r=int(input('enter rate of interest:'))
t=int(input('enter time in year:'))

#calculate simple interest
si=(p*t*r)/100

#display result
print(f'simple intrest is {si}')