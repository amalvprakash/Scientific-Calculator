from tkinter import *
import parser
import math
import tkinter.messagebox
from tkinter import ttk

root = Tk()
root.title('Calculator')
# get the user input and place it in the textfield

i = 0

def get_variable(num):
    global i
    display.insert(i, num)
    i += 1


def clear_field():
    display.delete(0, END)


def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_field()
        display.insert(0, new_string)
    else:
        clear_field()
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def get_operations(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length



def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_field()
        display.insert(0, result)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def fact_clicked():
    try:
        ans = float(display.get())
        ans = math.factorial(ans)
        display.delete(0, END)
        display.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# input field
display = Entry(root, width=40, borderwidth=5,font="Verdana 20", fg="black", bg="#abbab1", bd=0, justify=RIGHT, insertbackground="#abbab1", cursor="arrow")
display.grid(row=1, columnspan=6, sticky=W + E, padx=10, pady=10)

# buttons
ttk.Button(root, text="1", command=lambda: get_variable(1)).grid(row=2, column=0)
ttk.Button(root, text="2", command=lambda: get_variable(2)).grid(row=2, column=1)
ttk.Button(root, text="3", command=lambda: get_variable(3)).grid(row=2, column=2)

ttk.Button(root, text="4", command=lambda: get_variable(4)).grid(row=3, column=0)
ttk.Button(root, text="5", command=lambda: get_variable(5)).grid(row=3, column=1)
ttk.Button(root, text="6", command=lambda: get_variable(6)).grid(row=3, column=2)

ttk.Button(root, text="7", command=lambda: get_variable(7)).grid(row=4, column=0)
ttk.Button(root, text="8", command=lambda: get_variable(8)).grid(row=4, column=1)
ttk.Button(root, text="9", command=lambda: get_variable(9)).grid(row=4, column=2)

# function buttons

ttk.Button(root, text="Ac", command=lambda: clear_field()).grid(row=5, column=0)
ttk.Button(root, text="0", command=lambda: get_variable(0)).grid(row=5, column=1)
ttk.Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2)

ttk.Button(root, text="+", command=lambda: get_operations("+")).grid(row=2, column=3)
ttk.Button(root, text="-", command=lambda: get_operations("-")).grid(row=3, column=3)
ttk.Button(root, text="*", command=lambda: get_operations("*")).grid(row=4, column=3)
ttk.Button(root, text="/", command=lambda: get_operations("/")).grid(row=5, column=3)

# misc operations

ttk.Button(root, text="<-", command=lambda: undo()).grid(row=2, column=4)
ttk.Button(root, text="exp", command=lambda: get_operations("**")).grid(row=3, column=4)
ttk.Button(root, text="(", command=lambda: get_operations("(")).grid(row=4, column=4)
ttk.Button(root, text="^2", command=lambda: get_operations("**2")).grid(row=5, column=4)
ttk.Button(root, text="x!", command=lambda: fact_clicked()).grid(row=5, column=5)

ttk.Button(root, text="pi", command=lambda: get_operations("*3.14")).grid(row=2, column=5)
ttk.Button(root, text="%", command=lambda: get_operations("%")).grid(row=3, column=5)
ttk.Button(root, text=")", command=lambda: get_operations(")")).grid(row=4, column=5)


root.mainloop()
