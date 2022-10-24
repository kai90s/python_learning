from tkinter import *
import tkinter
import tkinter.messagebox as tkMessage

top = tkinter.Tk()

def helloCallBack():
   tkMessage.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()

top.mainloop()