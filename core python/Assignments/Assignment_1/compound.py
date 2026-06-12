# take input from user

p=int(input('enter principle amount:'))
r=int(input('enter rate of interst:'))
t=int(input('enter time in year:'))

# calulate final amount

a=p*(1+r/100)**t

#subtract principle amount from final amount to get compound interest
ci= a-p

# display result

print(f'compound interest is :{ci}')
