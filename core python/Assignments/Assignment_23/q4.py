# 4. Quiz Game: Create an interactive quiz game with multiple-choice questions. Display
# questions one at a time and allow the user to select an answer. Provide feedback on
# whether the selected answer is correct or incorrect.

from tkinter import *
from tkinter import messagebox

questions = [
    "What is the capital of India?",
    "Which language is used for Tkinter?",
    "What is 5 + 5?"
]

options = [
    ["Mumbai", "Delhi", "Pune", "Chennai"],
    ["Python", "Java", "C++", "HTML"],
    ["8", "9", "10", "11"]
]

answers = ["Delhi", "Python", "10"]

current = 0
score = 0


def check_answer():
    global current, score

    selected = var.get()

    if selected == answers[current]:
        messagebox.showinfo("Result", "Correct Answer!")
        score += 1
    else:
        messagebox.showerror("Result", "Incorrect Answer!")

    current += 1

    if current < len(questions):
        show_question()
    else:
        messagebox.showinfo("Quiz Finished",
                            "Your Score: " + str(score))
        root.destroy()


def show_question():
    question.config(text=questions[current])

    for i in range(4):
        radio[i].config(text=options[current][i],
                        value=options[current][i])

    var.set("")


root = Tk()
root.title("Quiz Game")
root.geometry("400x350")

question = Label(root, text="", font=("Arial", 14),
                  wraplength=350)
question.pack(pady=20)

var = StringVar()

radio = []

for i in range(4):
    r = Radiobutton(root, text="", variable=var,
                    value="", font=("Arial", 12))
    r.pack(anchor="w", padx=50, pady=5)
    radio.append(r)

Button(root, text="Submit", command=check_answer).pack(pady=20)

show_question()

root.mainloop()
