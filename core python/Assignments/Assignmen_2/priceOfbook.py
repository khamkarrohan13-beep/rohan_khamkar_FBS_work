# 5. WAP to calculate selling price of book based on cost price and discount.

# take input from user

cp=(int(input('enter cost price of the book:')))

d=(int(input('enter discount percentage:')))

#find discount amount

da=(cp*d)/100

#find selling price

sp=cp-da

#display price
print(f'selling price of the book is:{sp}')