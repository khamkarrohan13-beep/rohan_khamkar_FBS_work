from student import Student
class Medicalstudent(Student):
    def __init__(self, studentId, Name, Age, Percentage,specialization,marksofinternship):
        super().__init__(studentId, Name, Age, Percentage)
        self.__specialization=specialization
        self.__marksofinternship=marksofinternship

    def setSpecialization(self, specialization):
        self.__specialization = specialization

    def getSpecialization(self):
        return self.__specialization
    
    def setMarksOfInternship(self, marks):
        self.__marksofinternship = marks

    def getMarksOfInternship(self):
        return self.__marksofinternship
    def Accept(self):
        super().Accept()
        self.setSpecialization(input("Enter Specialization: ") )
        self.setMarksOfInternship(float(input("Enter Marks of Internship: ")))
    
    def display(self):
        super().display()

        print("Specialization :", self.getSpecialization())
        print("Internship Marks :", self.getMarksOfInternship())
    def calculaterank(self):
        per = self.getPer()
        internship = self.getMarksOfInternship()

        total = per + internship

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
        return  (f"{self.getid()} {self.getname()} "
                f"{self.getage()} {self.getPer()} "
                f"{self.getSpecialization()} "
                f"{self.getMarksOfInternship()}")