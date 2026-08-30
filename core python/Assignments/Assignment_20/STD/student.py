class Student:
    def __init__(self, roll_no, name, sy, ty):
        self.roll_no = roll_no
        self.name = name
        self.sy = sy
        self.ty = ty

    def calculate(self):
        total = self.sy.computer + self.ty.theory

        if total >= 70:
            grade = "A"
        elif total >= 60:
            grade = "B"
        elif total >= 50:
            grade = "C"
        elif total >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Total:", total)
        print("Grade:", grade)