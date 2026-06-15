# 10. Write a program to check if person is eligible to marry or not (male age >=21 and
# # female age>=18)

#take age from user
gender=(input('enter your gender:'))
age=int(input('enter your age:'))

#check conditions
if(gender=='F'):
    if(age>=18):
        print('girl is eligible for marrige.')
else:
    if(age>=21):
        print('male is eligible for marrige')    