from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Calculator")
root.resizable(0,0)
root.wm_attributes("-topmost",1)

equa =""
equation = StringVar()
equation.set("(Expression)")

calculation = Label(root, textvariable=equation)
calculation.grid(row=2, columnspan=8, padx=10, pady=10, sticky="nswe")


def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def equalPress():
    global equa
    if equa == "":
        return
    try:
        total =str(eval(equa))
        equation.set(total)
        equa = total
        root.clipboard_clear()
        root.clipboard_append(total)
    except Exception:
        total = "Error: " + equa
        root.bell()

btn = [ 0 for x in range(10)]
btn_pos=[(6,2), (3,1), (3,2), (3,3), (4,1), (4,2), (4,3), (5,1), (5,2), (5,3)]
for i in range(10):
    btn[i] = Button(root, text=str(i), command=Lambda il=i: btnPress(il))
    btn[i].grid(row=btn_pos[i][0], column=btn_pos[i][1],padx=5,pady=5)

Equal = Button(root, text="=", command=equalPress)
Equal.grid(row=6, column=4, padx=5, pady=5)

root.mainloop()
