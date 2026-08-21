class Student:
    def __init__(self,studentId,Name,Age,Percentage):
        self.__studentId=studentId
        self.__Name=Name
        self.__Age=Age
        self.__Percentage=Percentage

    def setid(self,stdid):
        self.__studentId=stdid
    def getid(self):
        return self.__studentId
    def setname(self,name):
        self.__Name=name
    def getname(self):
        return self.__Name
    def setage(self,age):
        self.__Age=age
    def getage(self):
        return self.__Age
    def setper(self,per):
        self.__Percentage=per
    def getPer(self):
        return self.__Percentage

    def Accept(self):
        self.setid(int(input('enter student ID:')))
        self.setname(int(input('enter student name:')))
        self.setage(int(input('enter student age:')))
        self.setper(int(input('enter student percentage:')))

    def display(self):
        print("student ID",self.getid())
        print("student name",self.getname())
        print("student age",self.getage())
        print("student percentage",self.getPer())
    def calculaterank(self):
        per=self.getPer()
        if per>=75:
            return "Distinction"
        if per>=60:
            return "first class"
        if per>=50:
            return "second class"

        if per>=35:
            return"pass"
        else:
            return"fail"

    def __str__(self):
            return f"{self.getid()} {self.getname()} {self.getage()} {self.getPer()}"   