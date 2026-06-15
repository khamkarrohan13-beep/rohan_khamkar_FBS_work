# 11. Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.

# take input from user

n=(int(input('enter total amount:')))

# count the notes

twothousand=n//2000
n=n%2000

fivehundred=n//500
n=n%500

twohundred=n//200
n=n%200

hundred=n//100
n=n%100

fifty=n//50
n=n%50

twenty=n//20
n=n%20

ten=n//10
n=n%10

#display notes

print(f'2000 notes:{twothousand} 500 notes:{fivehundred} 200 notes:{twohundred} 100 notes:{hundred} 50 notes:{fifty} 20 notes:{twenty} 10 notes:{ten}')