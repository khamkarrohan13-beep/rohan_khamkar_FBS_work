from student import Student

class Enggstudent(Student):
    def __init__(self, studentId, Name, Age, Percentage,branch,internalmarks):
        super().__init__(studentId, Name, Age, Percentage)
        self.__branch=branch
        self.__internalmarks=internalmarks

    def setbranch(self,bra):
        self.__branch=bra  
    def getbranch(self):
        return self.__branch
    def setinter(self,inter):
        self.__internalmarks=inter
    def getinter(self):
         return self.__internalmarks    
    def Accept(self):
            self.getbranch(input("enter branch:"))
            self.getinter(float("enter internal marks:"))
            return super().Accept()
                
    def display(self):
        super().display()
        print("branch",self.getbranch())
        print("internalmarks",self.getinter())
    
    def calculaterank(self):
        per=self.getPer()
        internal=self.getinter()
        total=per+internal
        if total >= 150:
            return "Distinction"
        elif total >= 120:
            return "First Class"
        elif total >= 100:
            return "Second Class"
        elif total >= 70:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
         return (f"{self.getid()} {self.getname()} {self.getage()} "
                f"{self.getPer()} {self.getbranch()} {self.getinter()}")