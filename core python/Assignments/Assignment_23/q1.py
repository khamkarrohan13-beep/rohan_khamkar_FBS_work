# Python Assignment – (Tkinter)
# 1. Develop a simple login system with a username and password field. Implement user
# authentication, and show a success message if the login is successful, or an error
# message if the login fails.

from tkinter import *
from tkinter import messagebox

def login():
    username = entry1.get()
    password = entry2.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")


root = Tk()
root.title("Login System")
root.geometry("300x200")

Label(root, text="Username").pack(pady=10)
entry1 = Entry(root)
entry1.pack()

Label(root, text="Password").pack(pady=10)
entry2 = Entry(root, show="*")
entry2.pack()

Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()