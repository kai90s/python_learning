from tkinter import *

root = Tk()


def doNothing():
    print("ok ok I won't...")


def doNothingg():
    print("ok I will..")


def doNothinggg():
    print("oh no...")


menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(Label="File", menu=subMenu)
subMenu.add_command(Label="New Project...", command=doNothingg)
subMenu.add_command(Label="New...", command=doNothingg)
subMenu.add_separator()
subMenu.add_command(Label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(Label="Edit", menu=editMenu)
editMenu.add_command(Label="Redo", command=doNothinggg)

root.mainloop()
