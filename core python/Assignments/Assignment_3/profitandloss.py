cp=int(input("enter cost price:"))
sp=int(input("enter selling price:"))

amt=sp-cp

if(amt>0):
    print(f"{amt} is profit")

elif(amt==0):
    print(f'{amt} is no profit no loss')

else:
    print(f'{amt} is loss')    