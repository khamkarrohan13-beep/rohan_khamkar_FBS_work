# 12. Write a program to create three lists of numbers, their squares
# and cubes

li=[1,2,3,4,5,6,7,8,9]

sqr=[]
cube=[]

for i in range(0,len(li)):
    sqr.append(li[i]**2)
    cube.append(li[i]**3)

print(f'numbers: {li}')    
print(f'squares of numbers: {sqr}')
print(f'cubes of numbers: {cube}')

