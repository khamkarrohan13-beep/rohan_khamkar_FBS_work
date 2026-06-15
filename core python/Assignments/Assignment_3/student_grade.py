#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

# take input from user

s1=int(input('enter first subject marks:'))
s2=int(input('enter second subject marks:'))
s3=int(input('enter third subject marks:'))
s4=int(input('enter forth subject marks:'))
s5=int(input('enter fifth subject marks:'))
#calculate percentage

per=(s1+s2+s3+s4+s5)/500*100

#check conditions
if(per>=80):
    print('first class.')

elif(per>=60 and per<79):
    print('second class')

elif(per>=35 and per<59 ):
    print('pass')   

elif(per<35):
    print('fail')

else:
    print('enter valid marks')
    