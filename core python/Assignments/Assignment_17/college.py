class College:

    
    def __init__(self, numberOfStudents):
        self.__numberOfStudents = numberOfStudents
        self.__students = []

   
    def AddStudent(self, student):
        if len(self.__students) < self.__numberOfStudents:
            self.__students.append(student)
            print("Student added successfully")
        else:
            print("College is full")

    
    def GetStudent(self, studentId):
        for student in self.__students:
            if student.getid() == studentId:
                return student

        return None

  
    def RemoveStudent(self, studentId):
        student = self.GetStudent(studentId)

        if student is not None:
            self.__students.remove(student)
            print("Student removed successfully")
        else:
            print("Student not found")

    def __str__(self):
        result = "College Students:\n"

        for student in self.__students:
            result += str(student) + "\n"

        return result