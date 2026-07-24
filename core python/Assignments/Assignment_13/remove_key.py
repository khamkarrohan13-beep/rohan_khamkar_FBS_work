# 7. Python Program to Remove the Given Key from a Dictionary

key=input('enter key you want to remove:')

d={'name':'rohan','age':20,'city':'pune'}

if key in d:
    del d[key]
else:
    print('key not found')    

print(f'after removing key:{d}')    