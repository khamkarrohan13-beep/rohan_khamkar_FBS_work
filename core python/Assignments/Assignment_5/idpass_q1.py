#1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

id=1771
password=str('rohan')



for i in range(1,4):
    id1=int(input('enter your id:'))
    passw=str(input('enter your password:'))

    if (id==id1 and password==passw):
        print('login successful')
        break
    else:
        print('re enter id and password')    
        