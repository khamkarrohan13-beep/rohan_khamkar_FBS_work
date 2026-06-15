# 6. Write a program to calculate profit or loss.

#take cost price and selling price from user
cp=int(input("enter cost price:"))
sp=int(input("enter selling price:"))

#calculate amount
amt=sp-cp

#check conditons
if(amt>0):
    print(f"{amt} is profit")

elif(amt==0):
    print(f'{amt} is no profit no loss')

else:
    print(f'{amt} is loss')    