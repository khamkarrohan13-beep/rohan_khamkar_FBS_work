from SY.symarks import SYMARKS
from TY.tymarks import TYMarks
from STD.student import Student


sy = SYMARKS(35, 40, 45)
ty = TYMarks(40, 35)

s = Student(101, "Rohan", sy, ty)

s.calculate()