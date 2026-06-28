# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


n=int(input('enter number of passengers:'))
ticket=int(input('enter per person ticket cost: '))

pay=0
for i in range(1,n+1):
    
    age=int(input(f'enter age of passenger {i}:'))
    if age<12:
        pay+=ticket-(ticket*30)/100
    elif age>59:
        pay+=ticket-(ticket*50)/100
    else:
        pay+=ticket
          

print(f'total cost of ticket is {pay}')
