# Calculate the cost of painting the following building’s walls (both interior and
# exterior). You need to accept area (one wall) and cost of both interior and
# exterior wall.
# (Note: 1. Below diagram is of two joint rooms.
# 2. It is upper view of building.)

#take input from user

area=int(input('enter area of one wall :'))
interior=int(input('enter cost of painting of interior wall:'))
exterior=int(input('enter cost of painting exterior walls:'))

#calculate cost for room1 one and room2 
room1=((interior*4)+(exterior*3.5))*area

room2=((interior*4)+(exterior*3.5))*area

totalcost=room1+room2
#display cost of painting
print(f'cost of painting is {totalcost}')

