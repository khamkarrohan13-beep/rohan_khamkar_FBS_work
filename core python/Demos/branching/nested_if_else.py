gender=input('Enter gender(M/f):')
age= int(input('enter age:'))

if(gender=='F'):
    if(age>=18):
        print('girl is eligible for marrige')
    else:
        print('not eligible for marrige')    

else:
    if(age>=21):
        print('boy is eligible for marrige')
    else:
        print('boy is not eligible for marrige') 

        #braching inside branching  