# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product:

    def __init__(self,pid,pname,price=0,quantity=0):
        self.__pid=pid
        self.__pname=pname
        self.__price=price
        self.__quantity=quantity

    def get_pid(self):
        return self.__pid

    def set_pid(self, pid):
        self.__pid = pid

    def get_pname(self):
        return self.__pname

    def set_pname(self, pname):
        self.__pname = pname

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity


    def __str__(self):
        return f"Product ID: {self.__pid}, Product Name: {self.__pname}, Price: {self.__price}, Quantity: {self.__quantity}"

p1=Product(101, "Laptop", 999.99, 10)
print(p1)

print(p1.get_pid())