# 8. Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

import random
# generate random number using random module
captcha=random.randint(1000,9999)

id='1771'
password='rohan'

#take id password and captcha from user
id1=(input('enter your id:'))
passw=(input('enter your password:'))

print(captcha)

captcha1=int(input('enter captcha:'))

#check id password and captch is correct
if(id1==id and password==passw):
    if(captcha==captcha1):
        print('login succesfully')

    else:
        print('invalid credentials or captcha')    