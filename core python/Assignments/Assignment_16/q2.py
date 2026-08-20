# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:

    discount = 0.1  # Static member for discount (10%)

    def __init__(self, pid, pname, price=0, quantity=0):
        self.__pid = pid
        self.__pname = pname
        self.__price = price
        self.__quantity = quantity

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

    @staticmethod
    def apply_discount(price):
        return price * (1 - Product.discount)  # Apply discount to the price
    
    def __str__(self):
        discounted_price = Product.apply_discount(self.__price)
        return f"Product ID: {self.__pid}, Product Name: {self.__pname}, Price: {discounted_price}, Quantity: {self.__quantity}"

p1 = Product(101, "Laptop", 999.99, 10)
print(p1)

print(f"Original Price: {p1.get_price()}, Discounted Price: {Product.apply_discount(p1.get_price())}")