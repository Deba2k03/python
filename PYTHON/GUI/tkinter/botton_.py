from tkinter import *

from setuptools import Command
root = Tk()
root.geometry("800x600")

def hello():
    print("hello bro")
def name():
    print("my name is Debashish")
f1=Frame(root,borderwidth=8,bg="grey",relief=SUNKEN)
f1.pack(side=TOP,anchor="nw")

b1 = Button(f1,bg="red",text="print now",command=hello)
b1.pack(side=LEFT,padx=23)
b1 = Button(f1,bg="red",text="print name",command=name)
b1.pack(side=LEFT,padx=34)
b1 = Button(f1,bg="red",text="print now")
b1.pack(side=LEFT,padx=23)

root.mainloop()