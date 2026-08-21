from student import Student
from enggstudent import Enggstudent
from medicalstudent import  Medicalstudent
from college import College

s1 = Student(101, "Rohan", 21, 86)

e1 = Enggstudent(102, "Rahul", 22, 80, "Computer", 18)

m1 =  Medicalstudent(103, "Amit", 23, 85, "Cardiology", 20)

c1 = College(5)

c1.AddStudent(s1)
c1.AddStudent(e1)
c1.AddStudent(m1)

print(c1)
c1.RemoveStudent(101)
print(c1)