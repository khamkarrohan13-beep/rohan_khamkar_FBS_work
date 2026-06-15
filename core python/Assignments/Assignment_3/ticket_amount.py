# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


#take age and amount from users
ticket=int(input('enter ticket amount per person:'))

age1=(int(input('enter age of first person:')))

#person 1
if (age1<12):
    amount1=ticket -(ticket*30/100)
elif (age1>59):
    amount1=ticket -(ticket*50/100)
else:
    amount1=ticket   

#person 2

p2=(int(input('enter age of second person:')))
if (age1<12):
    amount2=ticket -(ticket*30/100)
elif (age1>59):
    amount2=ticket -(ticket*50/100)
else:
    amount2=ticket   

# person 3
p3=(int(input('enter age of third person:')))
if (age1<12):
    amount3=ticket -(ticket*30/100)
elif (age1>59):
    amount3=ticket -(ticket*50/100)
else:
    amount3=ticket   

#person4

p4=(int(input('enter age of forth person:')))
if (age1<12):
    amount4=ticket -(ticket*30/100)
elif (age1>59):
    amount4=ticket -(ticket*50/100)
else:
    amount4=ticket   

# person5
p5=(int(input('enter age of fifth person:')))
if (age1<12):
    amount5=ticket -(ticket*30/100)
elif (age1>59):
    amount5=ticket -(ticket*50/100)
else:
    amount5=ticket 

#calculate total   
total=amount1+amount2+amount3+amount4+amount5

#display total
print(f'total ticket amount is:{total}')



