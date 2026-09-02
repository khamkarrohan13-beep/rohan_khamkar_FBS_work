# Python Assignment – (Pickling and Unpickling)
# 1. Create a class Emp (eid,ename,basic)
# 2. WAP a menu driven program to perform following operations using
# files :

# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.

import pickle

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print(self.eid, self.ename, self.basic)


def add_record():
    f = open("emp.dat", "ab")

    eid = int(input("Enter employee id: "))
    ename = input("Enter employee name: ")
    basic = float(input("Enter basic salary: "))

    e = Emp(eid, ename, basic)
    pickle.dump(e, f)

    f.close()
    print("Record added successfully")


def search_record():
    eid = int(input("Enter employee id to search: "))
    found = False

    try:
        f = open("emp.dat", "rb")

        while True:
            e = pickle.load(f)

            if e.eid == eid:
                e.display()
                found = True
                break

    except EOFError:
        f.close()

    if not found:
        print("Record not found")


def display_all():
    try:
        f = open("emp.dat", "rb")

        while True:
            e = pickle.load(f)
            e.display()

    except EOFError:
        f.close()


def delete_record():
    eid = int(input("Enter employee id to delete: "))
    records = []
    found = False

    try:
        f = open("emp.dat", "rb")

        while True:
            e = pickle.load(f)

            if e.eid == eid:
                found = True
            else:
                records.append(e)

    except EOFError:
        f.close()

    f = open("emp.dat", "wb")

    for e in records:
        pickle.dump(e, f)

    f.close()

    if found:
        print("Record deleted successfully")
    else:
        print("Record not found")


def edit_record():
    eid = int(input("Enter employee id to edit: "))
    records = []
    found = False

    try:
        f = open("emp.dat", "rb")

        while True:
            e = pickle.load(f)

            if e.eid == eid:
                e.ename = input("Enter new name: ")
                e.basic = float(input("Enter new basic salary: "))
                found = True

            records.append(e)

    except EOFError:
        f.close()

    f = open("emp.dat", "wb")

    for e in records:
        pickle.dump(e, f)

    f.close()

    if found:
        print("Record updated successfully")
    else:
        print("Record not found")


while True:

    print("\n----- EMPLOYEE MENU -----")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_record()

    elif ch == 2:
        search_record()

    elif ch == 3:
        delete_record()

    elif ch == 4:
        edit_record()

    elif ch == 5:
        display_all()

    elif ch == 6:
        break

    else:
        print("Invalid choice")