# 6. WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.

# take input from user

basic=(int(input('enter your basic salary:')))

# calculate da ta and hra

da=(10/100)*basic
print(da)
ta=(12/100)*basic
print(ta)
hra=(15/100)*basic
print(hra)
total=basic+da+ta+hra

#display total salary

print(f'total salary employee is:{total}')