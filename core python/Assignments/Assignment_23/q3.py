# 3. Design a basic calculator to perform +,-,/,*

from tkinter import *

def calculate():
    a = float(entry1.get())
    b = float(entry2.get())
    op = operator.get()

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b

    output.config(text="Result: " + str(result))


root = Tk()
root.title("Calculator")
root.geometry("300x300")

Label(root, text="Enter First Number").pack(pady=5)
entry1 = Entry(root)
entry1.pack()

Label(root, text="Enter Second Number").pack(pady=5)
entry2 = Entry(root)
entry2.pack()

Label(root, text="Select Operator").pack(pady=5)

operator = StringVar()
operator.set("+")

OptionMenu(root, operator, "+", "-", "*", "/").pack()

Button(root, text="Calculate", command=calculate).pack(pady=15)

output = Label(root, text="Result: ")
output.pack()

root.mainloop()