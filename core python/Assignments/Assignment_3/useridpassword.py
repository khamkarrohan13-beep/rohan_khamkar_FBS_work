#supose you have data in database

id='1771'
password='rohan'

#take id and paa from user and compare it with already existed values

id1=(input('enter your id:'))
passw=(input('enter your password:'))

#check the conditon
if(id==id1 and password==passw):
   print('id and password is correct.')

else:
   print('id and password is wrong')

