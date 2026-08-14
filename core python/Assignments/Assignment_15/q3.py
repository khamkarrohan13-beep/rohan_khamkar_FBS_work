# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class Shirt:

    def __init__(self, sid, sname, type=None, price=0, size=None):
        self.__sid = sid
        self.__sname = sname
        self.__type = type
        self.__price = price
        self.__size = size

    def get_sid(self):
        return self.__sid

    def set_sid(self, sid):
        self.__sid = sid

    def get_sname(self):
        return self.__sname

    def set_sname(self, sname):
        self.__sname = sname

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size


    def __str__(self):
        return f"Shirt ID: {self.__sid}, Shirt Name: {self.__sname}, Type: {self.__type}, Price: {self.__price}, Size: {self.__size}"
    def display(self):
        print(f"Shirt ID: {self.__sid}, Shirt Name: {self.__sname}, Type: {self.__type}, Price: {self.__price}, Size: {self.__size}")

s1=Shirt(201, "Formal Shirt", "Formal", 49.99, "Large")
print(s1)  
s1.display()  