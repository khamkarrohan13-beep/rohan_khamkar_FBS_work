# 2. Build a currency converter application that converts between different currencies. The
# user should be able to enter an amount, select the input currency, select the output
# currency, and see the converted amount.


from tkinter import *
from tkinter import messagebox

def convert():
    try:
        amount = float(entry.get())

        from_currency = from_var.get()
        to_currency = to_var.get()

        rates = {
            "USD": 83,
            "EUR": 90,
            "GBP": 105,
            "INR": 1
        }

        result = amount * rates[from_currency] / rates[to_currency]

        output.config(text="Converted Amount: " + str(round(result, 2)))

    except:
        messagebox.showerror("Error", "Enter a valid amount")


root = Tk()
root.title("Currency Converter")
root.geometry("350x300")

Label(root, text="Currency Converter",
      font=("Arial", 18)).pack(pady=15)

Label(root, text="Enter Amount").pack()

entry = Entry(root)
entry.pack(pady=5)

Label(root, text="From Currency").pack()

from_var = StringVar()
from_var.set("INR")

from_menu = OptionMenu(root, from_var, "INR", "USD", "EUR", "GBP")
from_menu.pack(pady=5)

Label(root, text="To Currency").pack()

to_var = StringVar()
to_var.set("USD")

to_menu = OptionMenu(root, to_var, "INR", "USD", "EUR", "GBP")
to_menu.pack(pady=5)

Button(root, text="Convert", command=convert).pack(pady=15)

output = Label(root, text="Converted Amount: ")
output.pack()

root.mainloop()