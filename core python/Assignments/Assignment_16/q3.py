# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class Shirt:
    
    size_price_map = {
        "small": 1.0,
        "medium": 1.1,
        "large": 1.2,
        "xlarge": 1.3
    }

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

    @staticmethod
    def calculate_price(price, size):
        if size in Shirt.size_price_map:
            return price * Shirt.size_price_map[size]
        else:
            return price  # Return original price if size is not recognized

    def __str__(self):
        adjusted_price = Shirt.calculate_price(self.__price, self.__size)
        return f"Shirt ID: {self.__sid}, Shirt Name: {self.__sname}, Type: {self.__type}, Price: {adjusted_price}, Size: {self.__size}"

s1 = Shirt(201, "Formal Shirt", "Formal", 1000, "xlarge")
print(s1)    