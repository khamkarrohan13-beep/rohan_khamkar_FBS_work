#10. Write a program to check if entered year is a leap year or not.

def leap():
    year = int(input("Enter year: "))

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

leap()


