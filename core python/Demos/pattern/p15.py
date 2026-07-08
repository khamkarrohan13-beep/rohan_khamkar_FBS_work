k=7


for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+i),end=' ')

    for j in range(1,k+1):
        print('_',end=' ')
    k-=2

    for j in range(i,0,-1):
        if(j!=(chr(69))):
            print(chr(64+i),end=' ')
    print()    

