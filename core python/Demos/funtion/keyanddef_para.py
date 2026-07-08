def emp(id=101,name='ram',dept='it',gender='male',salary=0,address='xyz',number=123456789,email='xyz@.com',experience=0):
    data=f"id:{id}\nNAME:{name}\ndept:{dept}\ngender:{gender}\nsalary:{salary}\naddress:{address}\nnumber:{number}\nemail:{email}\nex:{experience}"
    return data

res=emp(id=102,salary=40000,gender='male')
print(res)