# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:
    count=0
    def __init__(self, bid, bname, price=None, author=None):
        self.__bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count+=1
        
    def get_id(self):
        return self.__bid
    def set_id(self, bid):
        self.__bid = bid    
    def get_name(self):
        return self.bname
    def set_name(self, name):
        self.bname = name
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author        
    def __str__(self):
        return f"Book ID: {self.__bid}, Book Name: {self.bname}, Price: {self.price}, Author: {self.author}"
    
    # @staticmethod
    # def get_count():
    #     return Book.count
    

b1=Book(1, "Python Programming", 29.99, "John Doe")
# b2=Book(2, "Data Structures", 39.99, "Jane Smith")
print(b1)
# print(b2)
# print(b1.get_id())
# print(Book.get_count())