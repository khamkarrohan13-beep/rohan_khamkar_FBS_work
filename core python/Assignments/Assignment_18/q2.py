# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self, d):
        km = self.km + d.km
        m = self.m + d.m
        cm = self.cm + d.cm

        # Convert cm to m
        if cm >= 100:
            m = m + cm // 100
            cm = cm % 100

        # Convert m to km
        if m >= 1000:
            km = km + m // 1000
            m = m % 1000

        return Distance(km, m, cm)

    def __sub__(self, d):
        total1 = self.km * 100000 + self.m * 100 + self.cm
        total2 = d.km * 100000 + d.m * 100 + d.cm

        total = total1 - total2

        km = total // 100000
        total = total % 100000

        m = total // 100
        cm = total % 100

        return Distance(km, m, cm)

    def display(self):
        print(self.km, "km", self.m, "m", self.cm, "cm")


d1 = Distance(5, 800, 70)
d2 = Distance(2, 500, 50)

print("Distance 1:")
d1.display()

print("Distance 2:")
d2.display()

d3 = d1 + d2
print("Addition:")
d3.display()

d4 = d1 - d2
print("Subtraction:")
d4.display()