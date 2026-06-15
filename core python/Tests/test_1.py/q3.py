# Write a program to accept distance in km and convert it into meters and
# centimeters both.

#take input from user
k=int(input('enter  distance in km:'))

#calculate meter and centimeter
meter=k*1000

centimeter=meter*100

#display result
print(f'{meter} meter and {centimeter} centimeter')
