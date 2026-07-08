password=(input('enter your password:'))
userID=int(input(' enter your id:'))

existpassword=str('rohan')
existID=int(1771)

if(password==existpassword and userID==existID):
    print('password id correct login sucessfully')

else:
    print('invalid id and password')    

