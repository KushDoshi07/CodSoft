from tkinter import *

operator = ''
default_font_size = 16

def buttonClick(numbers):
    global operator
    operator = operator + numbers
    calculatorField.delete(0, END)
    calculatorField.insert(END, operator)

def clear():
    global operator
    operator = ''
    calculatorField.delete(0, END)

def answer():
    global operator
    try:
        result = str(eval(operator))
        calculatorField.delete(0, END)
        calculatorField.insert(0, result)
        operator = ''
    except Exception as e:
        calculatorField.delete(0, END)
        calculatorField.insert(0, "Error")

def adjust_font_size(event):
    width = event.width
    new_font_size = max(int(default_font_size * width / 600), 8)
    calculatorField.config(font=("Helvetica", new_font_size, "bold"))
    for child in calculatorFrame.winfo_children():
        if isinstance(child, Button):
            child.config(font=("Helvetica", new_font_size, "bold"))

root = Tk()
root.title("Calculator")
root.configure(bg="#d9d9d9")

calculatorFrame = Frame(root, bg="#d9d9d9")
calculatorFrame.pack(fill=BOTH, expand=True)

calculatorField = Entry(calculatorFrame, font=("Helvetica", default_font_size, "bold"), width=30, bd=4, bg="#f3f3f3", fg="#333333", insertbackground="#333333")
calculatorField.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("Ans", 4, 0), ("Clear", 4, 1), ("0", 4, 2), ("/", 4, 3)
]

for (text, row, col) in buttons:
    button = Button(calculatorFrame, text=text, font=("Helvetica", default_font_size, "bold"), fg="#333333", bg="#bfbfbf", bd=0,
                    width=6, command=lambda t=text: buttonClick(t) if t != "Ans" and t != "Clear" else answer() if t == "Ans" else clear())
    button.grid(row=row, column=col, sticky="nsew")

for i in range(5):
    calculatorFrame.grid_rowconfigure(i, weight=1)
for i in range(4):
    calculatorFrame.grid_columnconfigure(i, weight=1)

root.bind("<Configure>", adjust_font_size)

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", toggle_fullscreen)

root.mainloop()
