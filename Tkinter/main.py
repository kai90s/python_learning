from tkinter import *
import tkinter
import tkMessageBox

top = tkinter.Tk()
def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()

top.mainloop()