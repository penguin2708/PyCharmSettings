from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import askokcancel, showinfo
from tkinter.filedialog import askopenfile,asksaveasfile

root = Tk(className = 'mein notepad')  # name des fensters.

textPad = ScrolledText(root, width=50, height=40)
textPad.pack()

def exit_command():
    if askokcancel("Quit", "Do you really want to quit?"):
        textPad.delete(1.0, END)


def new_file():
    if askokcancel("New file", "Clear contents?"):
        root.destroy()

def open_file():
    file = askopenfile(parent = root, mode = "rb", title = "Select a file")  # liefert datei-objekt zurück/ rb = read binary
    if file != None:
        contents = file.read()
        textPad.insert('1.0', contents)
        file.close()

def save_file():
   file = asksaveasfile(mode = 'w')
   if file != None:
       contents = textPad.get('1.0',END + '-1c')
       file.write(contents)
       file.close()

def exit_file():
    pass

menu = Menu(root)
root.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu = filemenu)  # aufklappbares Menu
filemenu.add_command(label = "New", command = exit_command)
filemenu.add_command(label = "Quit", command = new_file)
filemenu.add_separator()
filemenu.add_command(label = "Open", command = open_file)
filemenu.add_command(label = "Save", command = save_file)
filemenu.add_command(label = "Exit", command = exit_file)

root.mainloop()


