import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("1000x1000")
root.title("Physics Specialist Calculator")
root.configure(bg="#2b2b2b")

first_number = 0
current_op = ""

    
def update_display(number):
    current = display_label.cget("text")
    if current == "0" or current == "Error":
        display_label.config(text=str(number))
    else:
        display_label.config(text=current + str(number))

def operation_click(op):
    global first_number, current_op
    try:
        first_number = float(display_label.cget("text"))
        current_op = op
        display_label.config(text="0")
    except:
        display_label.config(text="Error")

def clear_click():
    global first_number, current_op
    first_number = 0
    current_op = ""
    display_label.config(text="0")

def equal_click():
    global first_number, current_op
    try:
        second_number = float(display_label.cget("text"))
        
        if current_op == "+":
            result = first_number + second_number
        elif current_op == "-":
            result = first_number - second_number
        elif current_op == "×":
            result = first_number * second_number
        elif current_op == "÷":
            result = first_number / second_number if second_number != 0 else "Nice Try Smartass"
        elif current_op == "^":
            result = first_number ** second_number
        else:
            result = second_number
            
        if isinstance(result, float) and result.is_integer():
            result = int(result)
            
        display_label.config(text=str(result))
    except:
        display_label.config(text="Error")

for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

display_label = tk.Label(root, text="0", font=("Arial", 48), 
                         bg="#2b2b2b", fg="white", anchor="e")
display_label.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)

btns = []
for i in range(10):
    btns.append(tk.Button(root, text=str(i), font=("Arial", 20), 
                          command=lambda x=i: update_display(x)))

btns[1].grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
btns[2].grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
btns[3].grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
btns[4].grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
btns[5].grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
btns[6].grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
btns[7].grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
btns[8].grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
btns[9].grid(row=3, column=2, sticky="nsew", padx=5, pady=5)
btns[0].grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

ops = [("^", 1), ("÷", 2), ("×", 3), ("-", 4), ("+", 5)]
for char, row in ops:
    tk.Button(root, text=char, font=("Arial", 20), bg="#f39c12", fg="white",
              command=lambda c=char: operation_click(c)).grid(row=row, column=3, sticky="nsew", padx=5, pady=5)

btn_clear = tk.Button(root, text="C", font=("Arial", 20), bg="#e74c3c", fg="white", command=clear_click)
btn_equal = tk.Button(root, text="=", font=("Arial", 20), bg="#27ae60", fg="white", command=equal_click)

btn_clear.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
btn_equal.grid(row=4, column=2, sticky="nsew", padx=5, pady=5)

root.mainloop()

