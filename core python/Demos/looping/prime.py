# num=int(input('enter the number'))
# flag=0

# for i in range(2,num):
#     if num%i==0:
#         flag=1
     
#     break

# if flag==0:
#     print('number is prime>')
# else:
#     print('number not prime.')

n=int(input('enter the number:'))

if n<=1:
    print('number is not prime nor composite ')

else:
    for i in range(2,n):
        if n%i==0:
            print(f'{n} is not prime ')
            break 
        
    else:   
        print(f'{n} is prime')
                    